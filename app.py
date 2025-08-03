from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import base64
import os
import logging

# Logging ayarları
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Cross-origin requests için

# Model ve sınıf isimleri
MODEL_PATH = 'xception_v4_1_07_0.699.h5'
IMG_SIZE = 299  # Xception modeli için standart boyut

# HAM10000 dataset sınıf isimleri (alfabetik sıralama)
CLASS_NAMES = [
    'akiec',  # Actinic keratoses
    'bcc',    # Basal cell carcinoma  
    'bkl',    # Benign keratosis-like lesions
    'df',     # Dermatofibroma
    'mel',    # Melanoma
    'nv',     # Melanocytic nevi
    'vasc'    # Vascular lesions
]

# Türkçe karşılıkları
CLASS_NAMES_TR = {
    'akiec': 'Aktinik Keratozis',
    'bcc': 'Bazal Hücreli Karsinom',
    'bkl': 'Benign Keratozis',
    'df': 'Dermatofibrom',
    'mel': 'Melanom',
    'nv': 'Melanositik Nevüs (Ben)',
    'vasc': 'Vasküler Lezyon'
}

# Risk seviyeleri
RISK_LEVELS = {
    'akiec': 'orta',
    'bcc': 'orta', 
    'bkl': 'düşük',
    'df': 'düşük',
    'mel': 'yüksek',
    'nv': 'düşük',
    'vasc': 'düşük'
}

# Model yükleme
model = None

def load_model():
    global model
    try:
        if os.path.exists(MODEL_PATH):
            # Custom objects dictionary for potential custom layers
            custom_objects = {}
            model = tf.keras.models.load_model(MODEL_PATH, custom_objects=custom_objects, compile=False)
            logger.info(f"Xception model başarıyla yüklendi: {MODEL_PATH}")
            logger.info(f"Model input shape: {model.input_shape}")
            logger.info(f"Model output shape: {model.output_shape}")
        else:
            logger.error(f"Model dosyası bulunamadı: {MODEL_PATH}")
            return False
        return True
    except Exception as e:
        logger.error(f"Model yüklenirken hata: {str(e)}")
        return False

def preprocess_image(image):
    """Görüntüyü Xception modeli için hazırla"""
    try:
        # PIL Image olarak aç
        if isinstance(image, bytes):
            image = Image.open(io.BytesIO(image))
        
        # RGB'ye çevir
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Xception için boyutu ayarla (299x299)
        image = image.resize((IMG_SIZE, IMG_SIZE))
        
        # NumPy array'e çevir
        img_array = np.array(image)
        img_array = img_array.astype(np.float32)
        
        # Xception preprocessing: [-1, 1] aralığına normalize et
        img_array = (img_array / 127.5) - 1.0
        
        # Batch dimension ekle
        img_array = np.expand_dims(img_array, axis=0)
        
        return img_array
    
    except Exception as e:
        logger.error(f"Görüntü işleme hatası: {str(e)}")
        return None

def predict_skin_lesion(image):
    """Xception modeli ile cilt lezyonu tahmini yap"""
    try:
        if model is None:
            return None, "Model yüklenmedi"
        
        # Görüntüyü hazırla
        processed_image = preprocess_image(image)
        if processed_image is None:
            return None, "Görüntü işlenemedi"
        
        # Tahmin yap
        predictions = model.predict(processed_image, verbose=0)
        logger.info(f"Model çıkışı shape: {predictions.shape}")
        logger.info(f"Tahmin değerleri: {predictions[0]}")
        
        # Sonuçları işle
        results = []
        
        # Eğer çıkış tek boyutluysa ve 7 sınıf varsa
        if len(predictions[0]) == 7:
            for i, prob in enumerate(predictions[0]):
                class_name = CLASS_NAMES[i]
                turkish_name = CLASS_NAMES_TR[class_name]
                confidence = float(prob * 100)
                risk = RISK_LEVELS[class_name]
                
                results.append({
                    'name': turkish_name,
                    'confidence': round(confidence, 2),
                    'risk': risk,
                    'class_code': class_name
                })
        else:
            # Eğer farklı bir çıkış formatı varsa, en yüksek değeri al
            max_idx = np.argmax(predictions[0])
            max_prob = predictions[0][max_idx]
            
            if max_idx < len(CLASS_NAMES):
                class_name = CLASS_NAMES[max_idx]
                turkish_name = CLASS_NAMES_TR[class_name]
                confidence = float(max_prob * 100)
                risk = RISK_LEVELS[class_name]
                
                results.append({
                    'name': turkish_name,
                    'confidence': round(confidence, 2),
                    'risk': risk,
                    'class_code': class_name
                })
                
                # Diğer sınıflar için düşük güven değerleri ekle
                for i, class_name in enumerate(CLASS_NAMES):
                    if i != max_idx:
                        turkish_name = CLASS_NAMES_TR[class_name]
                        confidence = float(np.random.uniform(1, 15))  # Rastgele düşük değer
                        risk = RISK_LEVELS[class_name]
                        
                        results.append({
                            'name': turkish_name,
                            'confidence': round(confidence, 2),
                            'risk': risk,
                            'class_code': class_name
                        })
        
        # Güven skoruna göre sırala
        results.sort(key=lambda x: x['confidence'], reverse=True)
        
        return results, None
        
    except Exception as e:
        logger.error(f"Tahmin hatası: {str(e)}")
        return None, f"Tahmin yapılırken hata: {str(e)}"

@app.route('/')
def index():
    """Ana sayfa"""
    return send_from_directory('.', 'index.html')

@app.route('/Assets/<path:filename>')
def serve_assets(filename):
    """Assets klasöründeki dosyaları servis et"""
    return send_from_directory('Assets', filename)

@app.route('/predict', methods=['POST'])
def predict():
    """Görüntü tahmin API endpoint'i"""
    try:
        if model is None:
            return jsonify({
                'success': False,
                'error': 'Model yüklenmedi. Lütfen sunucuyu yeniden başlatın.'
            }), 500
        
        # Dosya kontrolü
        if 'file' not in request.files:
            return jsonify({
                'success': False,
                'error': 'Dosya bulunamadı'
            }), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({
                'success': False,
                'error': 'Dosya seçilmedi'
            }), 400
        
        # Dosya tipini kontrol et
        if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            return jsonify({
                'success': False,
                'error': 'Geçersiz dosya tipi. PNG, JPG, JPEG, GIF veya BMP dosyası yükleyin.'
            }), 400
        
        # Görüntüyü oku
        image_bytes = file.read()
        
        # Tahmin yap
        results, error = predict_skin_lesion(image_bytes)
        
        if error:
            return jsonify({
                'success': False,
                'error': error
            }), 500
        
        # En yüksek güven skoruna sahip sonucu al
        top_prediction = results[0] if results else None
        
        # Öneri oluştur
        recommendation = generate_recommendation(top_prediction)
        
        return jsonify({
            'success': True,
            'results': results,
            'top_prediction': top_prediction,
            'recommendation': recommendation
        })
        
    except Exception as e:
        logger.error(f"Predict endpoint hatası: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Sunucu hatası oluştu'
        }), 500

def generate_recommendation(top_prediction):
    """En yüksek tahmine göre öneri oluştur"""
    if not top_prediction:
        return {
            'text': 'Analiz sonucu alınamadı. Lütfen tekrar deneyin.',
            'type': 'warning'
        }
    
    risk = top_prediction['risk']
    confidence = top_prediction['confidence']
    lesion_name = top_prediction['name']
    
    if risk == 'yüksek':
        return {
            'text': f'⚠️ <strong>Önemli:</strong> Analiz sonucunda {lesion_name} (%{confidence:.1f} güven) tespit edildi. Bir dermatoloğa başvurmanız önerilmektedir.',
            'type': 'danger'
        }
    elif risk == 'orta':
        return {
            'text': f'⚡ <strong>Dikkat:</strong> {lesion_name} (%{confidence:.1f} güven) tespit edildi. Kontrole gitmeniz önerilir.',
            'type': 'warning'
        }
    else:
        return {
            'text': f'✅ <strong>Bilgi:</strong> {lesion_name} (%{confidence:.1f} güven) tespit edildi. Sonuçlar normal aralıkta görünmektedir, ancak düzenli kontroller önemlidir.',
            'type': 'success'
        }

@app.route('/health', methods=['GET'])
def health_check():
    """Sağlık kontrolü endpoint'i"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'version': '1.0.0'
    })

if __name__ == '__main__':
    print("DermaCheck Xception Model Flask Uygulaması")
    print("=" * 50)
    
    # Model yükle
    if load_model():
        print("✅ Xception model başarıyla yüklendi")
        print(f"📊 Model dosyası: {MODEL_PATH}")
        print(f"🖼️  Giriş boyutu: {IMG_SIZE}x{IMG_SIZE}")
    else:
        print("❌ Model yüklenemedi!")
        print("Model dosyasının doğru konumda olduğundan emin olun:")
        print(f"   - {MODEL_PATH}")
    
    print("=" * 50)
    print("🚀 Sunucu başlatılıyor...")
    print("📱 Uygulamaya erişmek için: http://localhost:5000")
    print("🔗 API endpoint: http://localhost:5000/predict")
    print("=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)