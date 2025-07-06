# 🚀 DermaCheck

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)  
![Sprint-1](https://img.shields.io/badge/Sprint-1-blue)  
![Tarih-20%20Haziran–6%20Temmuz](https://img.shields.io/badge/Date-20%20Haziran–6%20Temmuz-red)  

---

## 📜 Proje Açıklaması

**DermaCheck**, CutisAI çatısı altında geliştirilen; kullanıcıların yükledikleri cilt görüntülerini derin öğrenme tabanlı bir modelle analiz ederek potansiyel lezyonları yedi farklı sınıfa ayıran ve riskli bulunan durumlarda “dermatoloğa başvurmanız önerilir” yönlendirmesi sunan web tabanlı bir ön değerlendirme aracıdır.

- **Amaçlar**  
  1. **Erken farkındalık**: Ciltteki anormallikleri mümkün olan en erken aşamada kullanıcıya bildirmek.  
  2. **Tıbbi rehberlik**: Yüksek riskli sınıflandırmalarda kullanıcıya pozitif şekilde hatırlatmak ve bir dermatologa danışmayı teşvik etmek.  
  3. **Erişilebilirlik**: Hızlı, ücretsiz ve mobil uyumlu bir arayüz ile herkesin kullanımına açık olmak.

- **Nasıl Çalışır?**  
  1. **Görsel Yükleme**: Kullanıcı web arayüzünden lezyon fotoğrafını yükler.  
  2. **Ön İşleme**: Görüntü, 224×224’e ölçeklenir, normalize edilir ve basit augmentasyonlardan (flip, rotate) geçirilir.  
  3. **Model İnference**: Transfer öğrenme tabanlı ResNet50 CNN modeli, yedi sınıftan birine olasılıkla atama yapar.  
  4. **Sonuç Sunumu**:  
     - Sınıf adı ve güven skorları  
     - “Derhal dermatoloğa başvurmanızı öneririz.” tarzı rehber mesajı  
     - (Opsiyonel) Grad-CAM ile lezyon üzerindeki “dikkat alanı” ısı haritası  
     
- **Kullanılan Veri Seti**  
  - **HAM10000**: “Skin Cancer MNIST: HAM10000” (Kaggle)  
  - Toplamda yedi cilt lezyon sınıfı:  
    1. Benign keratosis  
    2. Melanom  
    3. Basal hücre karsinomu  
    4. Aktinik keratoz  
    5. Dermatofibroma  
    6. Vasküler lezyon  
    7. Melanositik nevüs  

- **Teknik Yığını**  
  - **Model & API**: Python, TensorFlow/Keras, Flask  
  - **Frontend**: React (başlangıç şablonu)  
  - **Containerization**: Docker (ileri aşamada)  

- **Ekip (4 Kişi)**  
  - **Erdoğan Başer** – Scrum Master, ML & Frontend  
  - **Gizem Erpek** – ML & Backend  
  - **Emir Ayyıldız** – ML & Backend  
  - **Eminenur Yıldız** – ML & Frontend  

> ⚠️ **Uyarı:** DermaCheck bir tanı aracı değildir. Son teşhis ve tedavi planlaması yalnızca yetkin sağlık uzmanları tarafından yapılmalıdır.

---

## 🎯 Sprint 1: Veri Hazırlığı & Keşif

**Tarih: 20 Haziran – 6 Temmuz**  
**Hedef:** HAM10000 veri setini indirip ön işleme ve EDA pipeline’ını tamamlayarak model eğitimi öncesi altyapıyı oluşturmak.

| # | Görev                                                                 | Sahip               | Puan |
|:-:|-----------------------------------------------------------------------|---------------------|:----:|
| 1 | HAM10000 dataset’i indirme & klasör yapısı oluşturma                  | **Gizem Erpek**     |  5   |
| 2 | Görüntü ön işleme pipeline’ı (resize, normalize, augment)            | **Erdoğan Başer**   |  8   |
| 3 | Eksik etiket ve class dengesini analiz etme; oversampling stratejisi | **Emir Ayyıldız**   |  5   |
| 4 | Keşifsel Veri Analizi (EDA): sınıf dağılımı, örnek görseller          | **Eminenur Yıldız** |  8   |
| 5 | Veri kalitesi dashboard’u (Pandas Profiling veya notebook)           | **Gizem Erpek**     |  5   |
| 6 | Scrum setup & Daily Scrum ayarları (Slack, board template)          | **Erdoğan Başer**   |  3   |

### 📅 Zaman Çizelgesi

- **20–22 Haziran**: Data indirme & klasör hiyerarşisi  
- **23–26 Haziran**: Ön işleme pipeline geliştirme  
- **27–29 Haziran**: Etiket kontrolü & denge analizi  
- **30 Haziran–3 Temmuz**: EDA notebook tamamlama  
- **4–6 Temmuz**: Dashboard & Scrum ayarları  

### 📦 Çıktılar

- `notebooks/data_exploration.ipynb`: EDA bulguları ve grafikler  
- `preprocessing.py`: Ön işleme modülü  
- `screenshots/board_sprint1_*.png`: Sprint board güncellemeleri  
- `docs/sprint1_review.md`, `docs/sprint1_retro.md`: Review ve Retrospective notları  

> 📝 **Not:** İlk commit ve placeholder dosyalar 20 Haziran’da eklenecek.  

---

CutisAI / DermaCheck • Sprint 1 • 20 Haziran – 6 Temmuz  
