# DermaCheck - AI Destekli Cilt Analizi Sistemi

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/CutisAI/DermaCheck/actions)
[![Version](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/CutisAI/DermaCheck/releases)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/tensorflow-2.x-orange)](https://tensorflow.org)

<p align="center">
  <img src="https://placeholder-link.com/dermacheck-logo.png" alt="DermaCheck Logo" width="200">
</p>

## 📑 İçindekiler

- [Takım İsmi](#-takım-ismi)
- [Takım Elemanları](#-takım-elemanları)
- [Ürün İsmi](#-ürün-ismi)
- [Product Backlog URL](#-product-backlog-url)
- [Ürün Açıklaması](#-ürün-açıklaması)
- [Ürün Özellikleri](#-ürün-özellikleri)
- [Sprint 1 Dokümantasyonu](#-sprint-1-dokümantasyonu)
- [Teknik Özellikler](#-teknik-özellikler)
- [Dataset Bilgisi](#-dataset-bilgisi)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)
- [İletişim](#-iletişim)

---

## 👥 Takım İsmi

**CutisAI**

---

## 🧑‍💻 Takım Elemanları

| Rol | İsim | Sorumluluklar |
|-----|------|---------------|
| **Scrum Master & ML Developer** | **Erdoğan Başer** | Proje koordinasyonu, ML model geliştirme, Frontend |
| **ML Developer & Frontend** | **Emir Ayyıldız** | ML model optimizasyonu, Kullanıcı arayüzü |
| **ML Developer & Backend** | **Eminenur Yıldız** | ML pipeline, Backend API geliştirme |
| **ML Developer & Backend** | **Gizem Erpek** | Veri işleme, Backend altyapı |

---

## 🎯 Ürün İsmi

**DermaCheck - AI Destekli Cilt Analizi Sistemi**

---

## 📋 Product Backlog URL

🔗 **[Product Backlog](https://github.com/CutisAI/DermaCheck/projects/1)**

*Not: Placeholder link - gerçek backlog URL'si buraya eklenecek*

---

## 📖 Ürün Açıklaması

DermaCheck, kullanıcıların yüklediği cilt görüntülerini yapay zekâ yardımıyla analiz ederek, potansiyel cilt rahatsızlıklarını ön değerlendirme amacıyla sınıflandıran, erişilebilir ve kullanıcı dostu bir web tabanlı yapay zekâ uygulamasıdır.

### 🔍 Projenin Amacı

- **Erken farkındalık yaratmak**: Kullanıcıların ciltlerinde oluşan değişiklikleri daha erken fark etmelerine yardımcı olmak
- **Tıbbi yönlendirme sağlamak**: Riskli sınıflandırmalar için "bir dermatoloğa başvurmanız önerilir" gibi açıklayıcı, rehber mesajlar sunmak
- **Halk sağlığına katkı**: Mobil uyarlanabilir, hızlı ve ücretsiz bir ön tarama aracı sağlayarak cilt sağlığı konusunda farkındalığı artırmak

### 🔬 Nasıl Çalışır?

1. Kullanıcı bir cilt görseli yükler
2. Sistem, bu görüntüyü önceden eğitilmiş bir Convolutional Neural Network (CNN) ile analiz eder
3. Görüntü, yedi ana sınıftan birine atanır
4. Sonuç, kullanıcıya sade ve anlaşılır bir şekilde sunulur
5. (Opsiyonel) Görselleştirme katmanı ile modelin lezyon üzerinde en dikkat çekici alanı nasıl yorumladığı gösterilir (Grad-CAM)

### ⚠️ Önemli Not

> **DermaCheck bir tanı aracı değildir.** Sunulan sonuçlar yalnızca bilgilendirme ve yönlendirme amaçlıdır. Nihai teşhis ve tedavi planlaması yalnızca uzman hekimler tarafından yapılmalıdır.

---

## ✨ Ürün Özellikleri

### 🎨 Kullanıcı Arayüzü
- Modern ve sezgisel web arayüzü
- Mobil uyumlu responsive tasarım
- Türkçe dil desteği
- Kolay dosya yükleme sistemi

### 🧠 Yapay Zeka Özellikleri
- **7 farklı cilt lezyon sınıfı** analizi:
  - Benign keratosis (iyi huylu)
  - Melanom (riskli)
  - Basal hücre karsinomu
  - Aktinik keratoz
  - Dermatofibroma
  - Vasküler lezyon
  - Melanositik nevüs (ben)

### 📊 Analiz Özellikleri
- Gerçek zamanlı görüntü analizi
- Güven skorları ve olasılık dağılımları
- Grad-CAM görselleştirmesi (ilgili alanları vurgulama)
- Risk seviyesi değerlendirmesi

### 🛡️ Güvenlik ve Gizlilik
- Güvenli dosya yükleme
- Veri gizliliği koruma
- GDPR uyumlu veri işleme

---

## 🚀 Sprint 1 Dokümantasyonu

### 📝 Sprint Notları

**Sprint Hedefi:** Proje temellerinin atılması ve geliştirme ortamının hazırlanması  
**Sprint Süresi:** 2.5 hafta (20 Haziran - 6 Temmuz 2024)  
**Sprint Planlaması:** 20 Haziran 2024, 10:00  
**İlk Commit Tarihi:** 7 Temmuz 2024

#### Sprint Kapsamı
- Proje repository kurulumu ve GitHub organizasyonu
- Geliştirme ortamının kurulması ve dokümantasyon
- Takım koordinasyonu ve iş akışının belirlenmesi
- Temel proje yapısının oluşturulması
- Sprint 2 için hazırlık çalışmaları

---

### 📊 Tahmin Edilen Tamamlanacak Puan

**Toplam Sprint Kapasitesi:** 25 Hikaye Puanı  
**Taahhüt Edilen Puan:** 20 Hikaye Puanı

*Sprint 1 kapsamında temel proje kurulumu ve dokümantasyon işlerine odaklanılacaktır. Detaylı puan dağılımı Sprint 2'de ML geliştirme aşamasında belirlenecektir.*

---

### 📈 Tahmin Mantığı

**Planning Poker Tekniği** kullanılarak tahminler yapıldı:

- **Fibonacci Serisi** (1, 2, 3, 5, 8, 13, 21) kullanıldı
- **Karmaşıklık faktörleri:**
  - Teknik zorluk seviyesi
  - Bağımlılıklar
  - Takım deneyimi
  - Risk faktörleri

**Tahmin Örnekleri:**
- Basit frontend bileşenleri: 3-5 puan
- Orta düzey backend API: 8 puan
- Karmaşık ML model implementasyonu: 13 puan

---

### 🗣️ Daily Scrum

#### 📅 Son Daily Scrum - 2 Temmuz 2024

**Katılımcılar:** Erdoğan Başer, Emir Ayyıldız, Eminenur Yıldız, Gizem Erpek

**Erdoğan Başer (Scrum Master)**
- ✅ **Dün:** GitHub repository yapısı ve README dokümantasyonu tamamlandı
- 🎯 **Bugün:** Takım koordinasyonu ve Sprint 2 planlaması yapılacak
- 🚫 **Engel:** Yok

**Emir Ayyıldız (ML Developer)**
- ✅ **Dün:** ML teknolojileri araştırması tamamlandı
- 🎯 **Bugün:** Geliştirme ortamı kurulumu başlanacak
- 🚫 **Engel:** Yok

**Eminenur Yıldız (ML/Backend Developer)**
- ✅ **Dün:** Proje gereksinimleri analizi yapıldı
- 🎯 **Bugün:** Backend teknoloji seçimi sonuçlandırılacak
- 🚫 **Engel:** Yok

**Gizem Erpek (Backend Developer)**
- ✅ **Dün:** API yapısı tasarımı başlandı
- 🎯 **Bugün:** Proje klasör yapısı oluşturulacak
- 🚫 **Engel:** Yok

---

### 📋 Sprint Board Updates

**Board URL:** [Sprint Board](https://github.com/CutisAI/DermaCheck/projects/1)

#### 📊 Güncel Sprint Durumu (2 Temmuz 2024)

```
📋 Backlog      🔄 In Progress    👀 Review       ✅ Done
   (3)             (2)              (1)            (2)
```

**Detaylı Durum:**
- **Backlog (3 item):** Teknoloji araştırması, Ortam kurulumu, Sprint 2 planlama
- **In Progress (2 item):** README dokümantasyonu, Proje yapısı tasarımı
- **Review (1 item):** GitHub repository kurulumu
- **Done (2 item):** Sprint planlama, Takım organizasyonu

#### 🔥 Burndown Chart
```
Kalan İş Yükü (Story Points)
20 |●
18 |  ●
16 |    ●
14 |      ●
12 |        ●
10 |          ○ ← Mevcut durum
 8 |            ○
 6 |              ○
 4 |                ○
 2 |                  ○
 0 |____________________○
   1  3  5  7  9  11 13 15 17 (Gün)
   
● Planlanan  ○ Gerçek
```

---

### 📷 Screenshot

#### 🖼️ Mevcut İlerleme Görüntüleri

**1. Dataset Ön İşleme Dashboard**
![Dataset Dashboard](https://placeholder-link.com/dataset-dashboard.png)

**2. Model Eğitim Pipeline**
![Model Training](https://placeholder-link.com/model-training.png)

**3. Web Arayüzü Mockup**
![Web UI Mockup](https://placeholder-link.com/web-mockup.png)

**4. Sprint Board Durumu**
![Sprint Board](https://placeholder-link.com/sprint-board.png)

---

### 🎉 Sprint Review

**📅 Tarih:** 6 Temmuz 2024, 14:00  
**📍 Konum:** Online (Google Meet)  
**👥 Katılımcılar:** Tüm takım + Product Owner + Stakeholders

#### ✅ Tamamlanan İşler (Demo)

1. **Proje Organizasyonu ve Dokümantasyon**
   - GitHub repository başarıyla kuruldu
   - Kapsamlı README dokümantasyonu oluşturuldu
   - Takım rolleri ve sorumlulukları netleştirildi
   - **Demo:** Repository yapısı ve dokümantasyon sunumu

2. **Sprint Planlama ve Metodoloji**
   - Scrum framework belirlendi ve uygulandı
   - Sprint planlaması tamamlandı
   - Daily standup süreci kuruldu
   - **Demo:** Proje yönetimi araçları tanıtımı

3. **Teknoloji Araştırması**
   - ML teknolojileri araştırıldı
   - Backend/Frontend teknoloji seçimleri yapıldı
   - Geliştirme ortamı gereksinimleri belirlendi
   - **Demo:** Teknoloji stack sunumu

#### 📊 Sprint Metrikleri

- **Taahhüt Edilen:** 20 story point
- **Tamamlanan:** 18 story point
- **Velocity:** 18 points
- **Başarı Oranı:** %90

#### 💭 Stakeholder Geri Bildirimi

**Pozitif Geri Bildirimler:**
- Kapsamlı ve profesyonel dokümantasyon kalitesi
- Takım koordinasyonu ve rol dağılımının netliği
- Sprint planlama sürecinin sistematik yapısı

**Geliştirme Önerileri:**
- Sprint 2'de teknik implementasyon odaklı çalışma
- Dataset entegrasyonu için daha detaylı planlama
- Model geliştirme milestone'larının belirlenmesi

#### 🎯 Sonraki Sprint İçin Giriş Kriterleri

- [x] Sprint 2 backlog'u hazır
- [x] Teknoloji stack onaylandı
- [x] Geliştirme ortamı gereksinimleri belirlendi
- [x] Takım kapasitesi Sprint 2 için planlandı

---

### 🔄 Sprint Retrospective

**📅 Tarih:** 6 Temmuz 2024, 15:30  
**📍 Konum:** Online (Miro Board)  
**⏱️ Süre:** 1 saat

#### 😊 İyi Giden Şeyler

1. **Takım Koordinasyonu**
   - Sprint planlama toplantıları verimli geçti
   - Rol ve sorumluluklar net şekilde belirlendi
   - Takım içi iletişim kanalları etkin kuruldu

2. **Dokümantasyon Kalitesi**
   - Kapsamlı ve profesyonel README oluşturuldu
   - Proje standartları belirlendi
   - Şeffaf sprint tracking sistemi kuruldu

3. **Metodoloji**
   - Scrum framework başarıyla adapte edildi
   - Daily standup rutini oturdu
   - Sprint hedefleri net tanımlandı

#### ⚠️ Geliştirilebilir Alanlar

1. **Teknoloji Hazırlığı**
   - Geliştirme ortamı kurulumu daha hızlı olabilir
   - ML araçları ve framework'lerin daha detaylı araştırılması gerekli
   - Development setup rehberleri hazırlanmalı

2. **Planlama Detayı**
   - Sprint 2 için daha granüler task breakdown'u yapılmalı
   - Teknik risklerin daha detaylı analizi gerekli
   - Capacity planning daha gerçekçi olmalı

3. **Araç Kullanımı**
   - GitHub project boards daha aktif kullanılmalı
   - Code review süreçleri tanımlanmalı
   - CI/CD pipeline planlaması yapılmalı

#### 🎯 Aksiyon Maddeleri

| Aksiyon | Sorumlu | Termin | Durum |
|---------|---------|---------|---------|
| Geliştirme ortamı setup rehberi yazma | @emir | 10 Temmuz | 🆕 Yeni |
| Sprint 2 detaylı task breakdown | @erdogan | 8 Temmuz | 🆕 Yeni |
| GitHub project board kurulumu | @gizem | 9 Temmuz | 🆕 Yeni |
| ML teknolojileri karşılaştırma raporu | @eminenur | 12 Temmuz | 🆕 Yeni |
| Code review guidelines oluşturma | Takım | 15 Temmuz | 🆕 Yeni |

#### 📈 Takım Sağlığı Skoru

```
İletişim        █████████░ 9/10
Motivasyon      █████████░ 9/10
Beceri Seviyesi ████████░░ 8/10
İş Tatmini      █████████░ 9/10
Stres Seviyesi  ███░░░░░░░ 3/10 (düşük = iyi)

Genel Skor: 8.8/10 🌟
```

---

## 🔧 Teknik Özellikler

### 🏗️ Sistem Mimarisi

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Frontend  │────│   Backend API   │────│   ML Pipeline   │
│   (React.js)    │    │   (Flask)       │    │  (TensorFlow)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### 🤖 Model Özellikleri

- **Algoritma:** Convolutional Neural Network (CNN)
- **Framework:** TensorFlow 2.x
- **Sınıf Sayısı:** 7 cilt lezyon tipi
- **Giriş Boyutu:** 224×224×3 RGB görüntü

### 🛠️ Teknoloji Yığını

**Frontend:**
- React.js
- TypeScript
- Material-UI

**Backend:**
- Python 3.9+
- Flask
- PostgreSQL

**Machine Learning:**
- TensorFlow 2.x
- NumPy, Pandas
- OpenCV

**DevOps:**
- Docker
- GitHub Actions

*Detaylı teknik dokümantasyon Sprint 2 ve 3'te genişletilecektir.*

---

## 📊 Dataset Bilgisi

### 🩺 HAM10000 Dataset

HAM10000 ("Human Against Machine with 10000 training images") dataset'i, International Skin Imaging Collaboration (ISIC) tarafından sağlanan kapsamlı bir dermoskopik görüntü koleksiyonudur.

#### 📈 Dataset Özellikleri

- **Toplam Görüntü:** 10,015 dermoskopik görüntü
- **Çözünürlük:** Değişken (minimum 600×450)
- **Format:** JPG
- **Toplam Boyut:** ~1.8 GB

#### 🏷️ Sınıf Dağılımı

| Sınıf | Kısaltma | Görüntü Sayısı | Yüzde |
|-------|----------|----------------|-------|
| Melanocytic nevi | nv | 6,705 | 66.9% |
| Melanoma | mel | 1,113 | 11.1% |
| Benign keratosis | bkl | 1,099 | 11.0% |
| Basal cell carcinoma | bcc | 514 | 5.1% |
| Actinic keratoses | akiec | 327 | 3.3% |
| Vascular lesions | vasc | 142 | 1.4% |
| Dermatofibroma | df | 115 | 1.1% |

#### 🔍 Veri Kalitesi

- **%50+ histopatoloji doğrulamalı** - altın standart
- **Kalan veriler:**
  - Follow-up examination
  - Expert consensus
  - Confocal microscopy

#### 📚 Kaynak

- **Orijinal Yayın:** [Nature Scientific Data](https://www.nature.com/articles/sdata2018161)
- **Kaggle Dataset:** [HAM10000](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000)
- **Harvard Dataverse:** [Dataset Link](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T)

---

## 💻 Kurulum

### 📋 Sistem Gereksinimleri

**Minimum Gereksinimler:**
- Python 3.8+
- 8GB RAM  
- 10GB boş disk alanı
- İnternet bağlantısı

### 🚀 Hızlı Başlangıç

#### 1. Repository'yi Klonlayın

```bash
git clone https://github.com/CutisAI/DermaCheck.git
cd DermaCheck
```

#### 2. Sanal Ortam Oluşturun

```bash
# Python venv kullanarak
python -m venv dermacheck_env

# Linux/Mac
source dermacheck_env/bin/activate

# Windows
dermacheck_env\Scripts\activate
```

#### 3. Bağımlılıkları Yükleyin

```bash
# Temel bağımlılıklar
pip install -r requirements.txt
```

#### 4. Uygulamayı Başlatın

```bash
# Development server
python app.py

# Tarayıcıda açın: http://localhost:5000
```

*Detaylı kurulum talimatları Sprint 2'de eklenecektir.*

---

## 🎮 Kullanım

### 🌐 Web Arayüzü

#### Temel Kullanım

1. **Ana Sayfaya Gidin:** `http://localhost:5000`
2. **Görüntü Yükleyin:** "Görüntü Seç" butonuna tıklayın
3. **Analiz Başlatın:** "Analiz Et" butonuna tıklayın
4. **Sonuçları İnceleyin:** Analiz sonuçları ve önerileri görüntüleyin

#### 📤 Desteklenen Dosya Formatları

- **JPG/JPEG** (önerilen)
- **PNG**
- **Maximum boyut:** 10MB

*Detaylı kullanım kılavuzu ve API dokümantasyonu Sprint 2 ve 3'te eklenecektir.*

---

## 🤝 Katkıda Bulunma

Projeye katkıda bulunmak istediğiniz için teşekkürler! Katkılarınız projenin gelişimi için çok değerli.

### 🔄 Katkı Süreci

1. **Repository'yi Fork Edin**
   ```bash
   # GitHub'da fork butonuna tıklayın
   git clone https://github.com/your-username/DermaCheck.git
   ```

2. **Feature Branch Oluşturun**
   ```bash
   git checkout -b feature/yeni-ozellik
   ```

3. **Değişikliklerinizi Yapın**
   - Kod standartlarına uygun geliştirme yapın
   - Test yazın ve çalıştırın
   - Dokümantasyonu güncelleyin

4. **Commit ve Push**
   ```bash
   git add .
   git commit -m "feat: yeni özellik eklendi"
   git push origin feature/yeni-ozellik
   ```

5. **Pull Request Oluşturun**
   - Açıklayıcı başlık ve açıklama yazın
   - İlgili issue'ları link edin
   - Screenshot ekleyin (UI değişiklikleri için)

### 📝 Kodlama Standartları

**Python Kodlama Standartları:**
- PEP 8 stil rehberini takip edin
- Fonksiyonlar için docstring yazın
- Type hints kullanın
- 80 karakter satır limiti

```python
def analyze_image(image_path: str) -> Dict[str, Any]:
    """
    Cilt görüntüsünü analiz eder.
    
    Args:
        image_path (str): Analiz edilecek görüntünün yolu
        
    Returns:
        Dict[str, Any]: Analiz sonuçları
    """
    pass
```

**JavaScript/TypeScript Standartları:**
- ESLint kurallarını takip edin
- Prettier code formatting
- Camel case isimlendirme

### 🧪 Test Yazma

```python
import unittest
from dermacheck.analyzer import DermaAnalyzer

class TestDermaAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = DermaAnalyzer()
    
    def test_analyze_image_success(self):
        result = self.analyzer.analyze_image("test_image.jpg")
        self.assertIn("prediction", result)
        self.assertIn("confidence", result)

if __name__ == "__main__":
    unittest.main()
```

### 🐛 Issue Raporlama

Issue oluştururken lütfen şu template'i kullanın:

```markdown
## 🐛 Bug Raporu

### Açıklama
Kısa ve net bug açıklaması

### Tekrar Etme Adımları
1. Şu sayfaya git
2. Şu butona tıkla
3. Şu hatayı gör

### Beklenen Davranış
Ne bekleniyordu

### Ekran Görüntüleri
Varsa screenshot ekle

### Ortam Bilgileri
- OS: [Ubuntu 20.04]
- Browser: [Chrome 95.0]
- Python Version: [3.9.7]
```

### 🌟 Feature İsteği

```markdown
## ✨ Feature İsteği

### Sorun
Hangi problemi çözüyor?

### Çözüm
Önerilen çözüm nedir?

### Alternatifler
Başka ne düşündünüz?

### Ek Bilgiler
Başka eklemek istediğiniz var mı?
```

---

## 📄 Lisans

Bu proje **MIT Lisansı** altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

```
MIT License

Copyright (c) 2024 CutisAI Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 İletişim

### 👥 Takım İletişim

- **Scrum Master:** Erdoğan Başer
  - 📧 Email: erdogan.baser@cutisai.com
  - 🐱 GitHub: [@erdogan-baser](https://github.com/erdogan-baser)

- **ML Developer:** Emir Ayyıldız
  - 📧 Email: emir.ayyildiz@cutisai.com
  - 🐱 GitHub: [@emir-ayyildiz](https://github.com/emir-ayyildiz)

- **Backend Developer:** Eminenur Yıldız
  - 📧 Email: eminenur.yildiz@cutisai.com
  - 🐱 GitHub: [@eminenur-yildiz](https://github.com/eminenur-yildiz)

- **Backend Developer:** Gizem Erpek
  - 📧 Email: gizem.erpek@cutisai.com
  - 🐱 GitHub: [@gizem-erpek](https://github.com/gizem-erpek)

### 🏢 Proje İletişim

- **Website:** [https://dermacheck.cutisai.com](https://placeholder-link.com)
- **Repository:** [https://github.com/CutisAI/DermaCheck](https://github.com/CutisAI/DermaCheck)
- **Issue Tracker:** [GitHub Issues](https://github.com/CutisAI/DermaCheck/issues)
- **Dokümantasyon:** [Docs](https://docs.dermacheck.cutisai.com)

### 💬 Topluluk

- **Discord:** [CutisAI Community](https://discord.gg/cutisai)
- **Slack:** [Workspace](https://cutisai.slack.com)
- **Twitter:** [@CutisAI](https://twitter.com/CutisAI)

---

<div align="center">

## ⭐ Projeyi Beğendiyseniz Star Vermeyi Unutmayın!

**🚀 Birlikte daha sağlıklı bir gelecek inşa ediyoruz!**

![DermaCheck Logo](https://placeholder-link.com/dermacheck-footer.png)

---

**Made with ❤️ by CutisAI Team**

</div>
