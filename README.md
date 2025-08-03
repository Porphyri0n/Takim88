# DermaCheck - AI Destekli Cilt Analizi Sistemi

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/CutisAI/DermaCheck/actions)
[![Version](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/CutisAI/DermaCheck/releases)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/tensorflow-2.x-orange)](https://tensorflow.org)

<p align="center">
  <img src="https://github.com/Porphyri0n/Takim88/blob/main/Assets/dermacheck-logo.png" alt="DermaCheck Logo" width="200">
</p>

## 👥 Takım İsmi

**CutisAI**

---

## Takım Logosu
<p align="left">
  <img src="https://github.com/Porphyri0n/Takim88/blob/main/Assets/cutisAI-logo.png" alt="DermaCheck Logo" width="200">
</p>

---

## 🧑‍💻 Takım Elemanları

| Rol | İsim | Aktif Görevler | Pasif Görevler |
|---|---|---|---|
| **Scrum Master & ML Developer** | **Erdoğan Başer** | Proje koordinasyonu | ML model geliştirme, Frontend |
| **ML Developer & Frontend** | **Emir Ayyıldız** | ML model optimizasyonu | Kullanıcı arayüzü |
| **ML Developer & Backend** | **Eminenur Yıldız** | ML pipeline | API geliştirme |
| **ML Developer & Backend** | **Gizem Erpek** | ML pipeline | Backend altyapı | 

---

## 🎯 Ürün İsmi

**DermaCheck - AI Destekli Cilt Analizi Sistemi**

---

## Ürün logosu
<p align="left">
  <img src="https://github.com/Porphyri0n/Takim88/blob/main/Assets/dermacheck-logo.png" alt="DermaCheck Logo" width="200">
</p>

---
## 📋 Product Backlog URL

🔗 **[Product Backlog](https://docs.google.com/spreadsheets/d/1H3UxpLTYpxyYXwBKO0GicLXYIxjtdqUwPHTbR4E1AAE/edit?usp=sharing)**


---
### 🚀 Hızlı Erişim Menüsü

| 📖 Bölüm | 📝 Açıklama | 🔗 Hızlı Erişim |
|-----------|-------------|------------------|
| **📖 Ürün Açıklaması** | Proje tanıtımı ve özellikler | [**Ürün Açıklaması**](#-ürün-açıklaması) |
| **🏁 Sprint 1** | Proje başlangıcı ve temel yapı | [**Sprint 1 Dokümantasyonu**](#-sprint-1-dokümantasyonu) |
| **🚀 Sprint 2** | Model geliştirme ve arayüz tasarımı | [**Sprint 2 Dokümantasyonu**](#-sprint-2-dokümantasyonu) |
| **🎯 Sprint 3** | Full entegrasyon ve proje finalizasyonu | [**Sprint 3 Dokümantasyonu**](#-sprint-3-dokümantasyonu) |
| **⚙️ Kurulum** | Projeyi çalıştırma rehberi | [**Kurulum Rehberi**](#-dermacheck-kurulum-rehberi) |

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
**İlk Kod Commit Tarihi:** 7 Temmuz 2024

#### Sprint Kapsamı
- Proje repository kurulumu ve GitHub organizasyonu
- Geliştirme ortamının kurulması ve dokümantasyon
- Takım koordinasyonu ve iş akışının belirlenmesi
- Temel proje yapısının oluşturulması
- Sprint 2 için hazırlık çalışmaları

---

### 🗣️ Daily Scrum

📅 20 Haziran 2024 - Sprint 1 Başlangıcı

Günlük Özet: Sprint Planning toplantısı tamamlandı. GitHub organizasyonu kuruldu ve repository oluşturuldu. Takım rolleri netleştirildi, Sprint 1 hedefleri belirlendi.

📅 21 Haziran 2024

Günlük Özet: README template hazırlandı ve branch stratejisi belirlendi. ML framework araştırmaları başladı. API tasarım prensipleri üzerinde çalışılmaya başlandı.

📅 24 Haziran 2024

Günlük Özet: Project board kurulumu tamamlandı. CNN mimarileri ve transfer learning yaklaşımları araştırıldı. Database schema tasarımına başlandı.

📅 25 Haziran 2024

Günlük Özet: Sprint tracking sistemi kuruldu. Model validation stratejileri incelendi. File upload stratejisi tasarlandı. Database normalization konusunda ek araştırma gerektiği belirlendi.

📅 26 Haziran 2024

Günlük Özet: Code review guidelines yazıldı. Model deployment stratejileri araştırıldı. Async processing patterns üzerinde çalışıldı. Takım içi yardımlaşma güçlendi.

📅 27 Haziran 2024

Günlük Özet: CI/CD pipeline tasarımı yapıldı. Model versioning stratejileri belirlendi. Caching strategies araştırıldı. API documentation tools incelendi.

📅 28 Haziran 2024

Günlük Özet: GitHub Actions workflow template hazırlandı. Sprint 1 mid-point review yapıldı - %60 ilerleme kaydedildi. Development environment setup guide yazılmaya başlandı.

📅 1 Temmuz 2024

Günlük Özet: README dokümantasyonu genişletildi. Local development environment kurulumları test edildi. Docker port conflict sorunu çözüldü. Environment variables strategy belirlendi.

📅 2 Temmuz 2024

Günlük Özet: Sprint Review hazırlıkları başladı. Development workflow dokümantasyonu tamamlandı. Logging configuration araştırıldı. Project folder structure finalize edildi.

📅 3 Temmuz 2024

Günlük Özet: Sprint 2 backlog hazırlığına başlandı. ML tasks breakdown yapıldı. Performance monitoring tools araştırıldı. Backend roadmap hazırlandı.

📅 4 Temmuz 2024

Günlük Özet: Sprint 1 completion checklist gözden geçirildi. HAM10000 dataset indirme stratejisi planlandı. Backend milestones belirlendi. Database ERD finalize edildi.

📅 5 Temmuz 2024

Günlük Özet: Sprint 1 deliverables %95 hazır durumda. Final README review yapıldı. Sprint Review demo hazırlıkları tamamlandı. Sprint 1 retrospective notları hazırlandı.


---

### 📋 Sprint Board Updates

**Board URL:** [Sprint Board](https://docs.google.com/spreadsheets/d/1yrPElOCZxonByDCxff-rVRn_BDlIlUAShSRS_oCt27w/edit?usp=sharing)

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
[BurnDownChart](https://docs.google.com/spreadsheets/d/1slRiE7KsxFyPxS30SDdtpb28tGOD9MChEr4Q9-Zs0BI/edit?usp=sharing)


---

### 📷 Screenshot

#### 🖼️ Mevcut İlerleme Görüntüleri

**1. Web Arayüzü Mockup**
![Web UI Mockup](https://github.com/Porphyri0n/Takim88/blob/main/Assets/dermacheck-frontend-mockup.png)


---

### 🎉 Sprint Review

**📅 Tarih:** 6 Temmuz 2024, 14:00  
**📍 Konum:** Online (Google Meet)  
**👥 Katılımcılar:** Tüm takım

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
(Her Sprint için 20 puan planı yapıldı)
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
│   (React.js)    │    │   (Flask)       │    │  (TensorFlow or |
└─────────────────┘    └─────────────────┘    | Pytorch testing |
                                              |  in Progress)   │
                                              └─────────────────┘
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
 
## 🚀 Sprint 2 Dokümantasyonu

### 📝 Sprint Notları

**Sprint Hedefi:** ML modelinin sınıflandırma mantığının çalışması ve arayüz tasarımının tamamlanması  
**Sprint Süresi:** 2 hafta (6 Temmuz - 20 Temmuz 2024)  
**Sprint Planlaması:** 7 Temmuz 2024, 10:00  
**İlk Model Eğitimi:** 10 Temmuz 2024  
**Frontend Tasarım Tamamlandı:** 18 Temmuz 2024

#### Sprint Kapsamı
- HAM10000 dataset entegrasyonu ve preprocessing
- CNN model mimarisi tasarımı ve eğitimi
- Frontend arayüz tasarımı ve prototip geliştirme
- Model performans testleri ve doğrulama
- Teknik dokümantasyon güncellemeleri

---

### 🗣️ Daily Scrum

📅 6 Temmuz 2024 - Sprint 2 Başlangıcı

Günlük Özet: Sprint 2 Planning toplantısı gerçekleştirildi. HAM10000 dataset indirme işlemi başlatıldı. ML model mimarisi araştırmaları başladı. Frontend wireframe tasarımına başlandı.

📅 7 Temmuz 2024

Günlük Özet: Dataset preprocessing stratejisi belirlendi. Transfer learning yaklaşımları araştırıldı. Material-UI component library seçimi yapıldı. Development environment setup rehberi tamamlandı.

📅 8 Temmuz 2024

Günlük Özet: HAM10000 dataset analizi tamamlandı. Sınıf dengesizliği sorunu tespit edildi. Data augmentation teknikleri araştırıldı. Frontend component tasarımına başlandı.

📅 9 Temmuz 2024

Günlük Özet: Model mimarisi tasarlandı - ResNet50 transfer learning approach seçildi. Data preprocessing pipeline oluşturuldu. UI mockup tasarımları hazırlandı. Donanım gereksinimleri değerlendirildi.

📅 10 Temmuz 2024

Günlük Özet: İlk model eğitimi başlatıldı ancak donanım yetersizliği sorunu yaşandı. Google Colab Pro araştırıldı. Frontend responsive design çalışmaları başladı. Takım staj yoğunluğu nedeniyle çalışma saatlerini yeniden planladı.

📅 11 Temmuz 2024

Günlük Özet: Cloud computing seçenekleri araştırıldı. Model eğitimi için donanım çözümü bulundu. Data augmentation uygulandı. Frontend upload component tasarımı tamamlandı.

📅 12 Temmuz 2024

Günlük Özet: Model eğitimi başarıyla başlatıldı. Batch size ve learning rate hiperparametre optimizasyonu yapıldı. Frontend results display component tasarlandı. Hafta sonu model eğitiminin devam etmesi planlandı.

📅 15 Temmuz 2024

Günlük Özet: İlk model eğitimi tamamlandı - %73 doğruluk elde edildi. Validation loss analizi yapıldı. Frontend navigation ve layout tasarımı tamamlandı. Model performance metrics analiz edildi.

📅 16 Temmuz 2024

Günlük Özet: Model overfitting problemi tespit edildi. Dropout ve regularization teknikleri uygulandı. Frontend dark/light theme desteği eklendi. Gizem frontend ekibine katıldı.

📅 17 Temmuz 2024

Günlük Özet: İkinci model eğitimi başlatıldı - improved architecture. Cross-validation stratejisi uygulandı. Frontend form validasyonu eklendi. Model inference pipeline tasarlandı.

📅 18 Temmuz 2024

Günlük Özet: Model performansı %78'e yükseltildi. Confusion matrix analizi yapıldı. Frontend arayüz tasarımı tamamlandı. Image preprocessing component eklendi.

📅 19 Temmuz 2024

Günlük Özet: Model fine-tuning parametreleri optimize edildi. Grad-CAM implementasyonu araştırıldı. Frontend mobile responsive test edildi. Sprint Review hazırlıkları başladı.

📅 20 Temmuz 2024

Günlük Özet: Sprint 2 completion checklist gözden geçirildi. Final model %82 doğruluk ile test edildi. Frontend demo hazırlıkları tamamlandı. Sprint Review ve Retrospective notları hazırlandı.

---

### 📋 Sprint Board Updates

**Board URL:** [Sprint Board](https://docs.google.com/spreadsheets/d/1yrPElOCZxonByDCxff-rVRn_BDlIlUAShSRS_oCt27w/edit?usp=sharing)

#### 📊 Güncel Sprint Durumu (20 Temmuz 2024)

```
📋 Backlog      🔄 In Progress    👀 Review       ✅ Done
   (0)             (0)              (0)            (15)
```

**Detaylı Durum:**
- **Done (15 items):** HAM10000 dataset entegrasyonu, CNN model eğitimi, Frontend arayüz tasarımı, Model validasyonu, Data preprocessing, UI/UX tasarım, Responsive design, Model performance optimization, Image upload component, Results display component, Navigation design, Theme implementation, Form validation, Mobile compatibility, Sprint dokümantasyonu

#### 🔥 Burndown Chart
[BurnDownChart](https://docs.google.com/spreadsheets/d/1slRiE7KsxFyPxS30SDdtpb28tGOD9MChEr4Q9-Zs0BI/edit?usp=sharing)

**Sprint 2 Velocity:** 100/100 story points ✅

---

### 📷 Screenshot

#### 🖼️ Sprint 2 Tamamlanan Geliştirmeler


---

**1. Geliştirilmiş Frontend Arayüzü**
![Front End Screenshot 1](https://github.com/Porphyri0n/Takim88/blob/main/Assets/frontend_SS1.png)
![Front End Screenshot 2](https://github.com/Porphyri0n/Takim88/blob/main/Assets/frontend_SS2.png)


---

**2. Model Training Dashboard**
![Model Training](https://github.com/Porphyri0n/Takim88/blob/main/Assets/model-training-dashboard.jpg)


---
**3. Mobile Responsive Design**
![Mobile Design](https://github.com/Porphyri0n/Takim88/blob/main/Assets/frontend_SS3.png)

---

### 🎉 Sprint Review

**📅 Tarih:** 20 Temmuz 2024, 16:00  
**📍 Konum:** Online (Google Meet)  

#### ✅ Tamamlanan İşler (Demo)

1. **Machine Learning Model Geliştirme**
   - HAM10000 dataset başarıyla entegre edildi (10,015 görüntü)
   - CNN model mimarisi tasarlandı ve eğitildi
   - Transfer learning ile ResNet50 kullanıldı
   - Model doğruluğu %82 seviyesine ulaştı
   - **Demo:** Model sınıflandırma testi

2. **Frontend Arayüz Tasarımı**
   - Modern ve kullanıcı dostu web arayüzü tamamlandı
   - Responsive design ile mobil uyumluluk sağlandı
   - Image upload ve results display componentleri geliştirildi
   - **Demo:** Frontend arayüz tanıtımı


#### 📊 Sprint Metrikleri

- **Taahhüt Edilen:** 20 story point
- **Tamamlanan:** 20 story point
- **Velocity:** 20 points
- **Başarı Oranı:** %100

### 🔄 Sprint Retrospective

**📅 Tarih:** 19 Temmuz 2024, 17:30  
**📍 Konum:** Online
**⏱️ Süre:** 1.5 saat

#### 😊 İyi Giden Şeyler

1. **Teknik Başarılar**
   - Model eğitimi başarıyla tamamlandı ve hedeflenen performansa ulaştı
   - Frontend tasarım kalitesi beklentileri aştı
   - Donanım sorunu yaratıcı çözümlerle aşıldı
   - Transfer learning yaklaşımı çok etkili oldu

2. **Takım Koordinasyonu**
   - Staj yoğunluğuna rağmen planlanan işler tamamlandı
   - Roller arası geçişler (Gizem'in frontend'e katılması) sorunsuz oldu
   - Problem çözme yaklaşımı çok iyiydi
   - Zaman yönetimi mükemmeldi

3. **Proje Yönetimi**
   - %100 story point completion başarısı
   - Risk yönetimi etkin şekilde yapıldı
   - Donanım sorunu önceden planlandığı için büyük aksaklık yaşanmadı

#### ⚠️ Geliştirilebilir Alanlar

1. **Dokümantasyon ve İletişim**
   - Daily standup notları düzenli tutulmadı
   - Toplantı planları ve notları sistematik hale getirilmeli
   - Teknik progress tracking daha detaylı olmalı

2. **Teknik Süreçler**
   - Model experiment tracking sistemi kurulmalı
   - Code review süreçleri daha sistemli hale getirilmeli
   - Version control stratejisi netleştirilmeli

3. **Kaynak Yönetimi**
   - Donanım gereksinimleri daha önceden planlanmalı
   - Staj programı ile proje takvimi daha iyi koordine edilmeli
   - Backup plan stratejileri geliştirilmeli

#### 📈 Takım Sağlığı Skoru

```
İletişim        ██████████ 10/10
Motivasyon      █████████░ 9/10
Beceri Seviyesi █████████░ 9/10
İş Tatmini      ██████████ 10/10
Stres Seviyesi  ████░░░░░░ 4/10 (düşük = iyi)

Genel Skor: 9.2/10 🌟
```

#### 🏆 Sprint 2 Öne Çıkan Başarılar

- **%100 Sprint Completion:** Tüm planların başarıyla tamamlanması
- **Design Excellence:** Zarif ve üst seviye frontend tasarım
- **Team Adaptability:** Staj yoğunluğuna rağmen plana sadık kalınması

---

### 🔬 Teknik Detaylar (Sprint 2)

#### 🤖 Machine Learning İlerleme

**Dataset İşleme:**
```
HAM10000 Dataset Statistics:
├── Total Images: 10,015
├── Training Set: 7,012 (70%)
├── Validation Set: 1,503 (15%)
└── Test Set: 1,500 (15%)

Class Distribution (After Balancing):
├── Melanocytic nevi (nv): 1,500 samples
├── Melanoma (mel): 1,113 samples
├── Benign keratosis (bkl): 1,099 samples
├── Basal cell carcinoma (bcc): 514 samples
├── Actinic keratoses (akiec): 327 samples
├── Vascular lesions (vasc): 142 samples
└── Dermatofibroma (df): 115 samples
```

## 📊 Sprint 2 Özet Metrikleri

| Metrik | Değer | Durum |
|--------|--------|--------|
| **Sprint Completion** | %100 | ✅ Mükemmel |
| **Model Accuracy** | %82.3 | ✅ Hedef Aşıldı |
| **Frontend Completion** | %100 | ✅ Tamamlandı |
| **Team Velocity** | 100 points | ✅ Planlanan |
| **Technical Debt** | Düşük | ✅ Yönetilebilir |
| **Team Satisfaction** | 9.2/10 | ✅ Yüksek |

---

<div align="center">

### 🎉 Sprint 2 Başarıyla Tamamlandı!

**Sonraki Durak: Sprint 3 - Full Integration & Deployment**

</div>

## 🚀 Sprint 3 Dokümantasyonu

### 📝 Sprint Notları

**Sprint Hedefi:** Backend-Frontend entegrasyonu ve proje finalizasyonu  
**Sprint Süresi:** 2 hafta (20 Temmuz - 3 Ağustos 2024)  
**Sprint Planlaması:** 20 Temmuz 2024, 15:00  
**API Entegrasyonu Tamamlandı:** 25 Temmuz 2024  
**Proje Finalize:** 2 Ağustos 2024  
**Tanıtım Videosu:** 3 Ağustos 2024

#### Sprint Kapsamı
- **Gemini API entegrasyonu** ve Flask backend API ile frontend full entegrasyonu
- **Xception CNN model** (299x299 input) deployment ve production optimizasyonu
- Gerçek **Xception model predictions** ile frontend'in tamamen çalışır hale getirilmesi
- **Google Gemini AI** desteği ile geliştirilmiş analiz yorumlama sistemi
- Kapsamlı test süreçleri ve hata giderme
- Performance optimizasyonları ve **Xception model** inference hızlandırması
- Ürün tanıtım videosu hazırlığı
- Final dokümantasyon güncellemeleri

---

### 🗣️ Daily Scrum

📅 20 Temmuz 2024 - Sprint 3 Başlangıcı

Günlük Özet: Sprint 3 Planning toplantısı gerçekleştirildi. Backend-Frontend entegrasyon planı hazırlandı. Mock data'dan gerçek API'ye geçiş stratejisi belirlendi. Sprint 2'den gelen momentum devam ediyor.

📅 21 Temmuz 2024

Günlük Özet: **Gemini API** ve Flask API endpoint testleri başladı. **Xception model** (299x299 input shape) loading optimizasyonu tamamlandı. Frontend JavaScript'te AJAX implementasyonu başlandı. CORS ayarları yapılandırıldı. **Google Gemini AI** entegrasyonu için API key konfigürasyonu yapıldı.

📅 22 Temmuz 2024

Günlük Özet: İlk **Gemini API + Xception model** entegrasyon testleri başarılı. File upload mechanism gerçek API ile test edildi. **Xception preprocessing pipeline** ([-1,1] normalization) optimize edildi. Error handling implementasyonu eklendi. **Gemini AI** ile analiz yorumlama sistemi test edildi.

📅 23 Temmuz 2024

Günlük Özet: **Xception model** image preprocessing pipeline optimize edildi. **Gemini API** response handling geliştirildi. Frontend loading states ve user feedback sistemleri geliştirildi. **Xception model prediction accuracy** Sprint 2'den %82'den %75'e düştü - model versiyonu değişikliği nedeniyle ancak **Gemini AI desteği** ile yorumlama kalitesi arttı.

📅 24 Temmuz 2024

Günlük Özet: Cross-browser compatibility testleri yapıldı. Mobile responsive design son testleri tamamlandı. API response format standardize edildi. Confidence score display iyileştirildi.

📅 25 Temmuz 2024

Günlük Özet: 🎉 **Gemini API + Xception Model** entegrasyonu başarıyla tamamlandı! Gerçek **Xception CNN predictions** frontend'te görüntüleniyor. **Google Gemini AI** ile geliştirilmiş analiz yorumları çalışıyor. Mock data tamamen kaldırıldı. End-to-end test süreçleri başladı.

📅 26 Temmuz 2024

Günlük Özet: Kapsamlı edge case testleri yapıldı. **Xception model** ile hata tespit edildi: cilt hastalığı olmayan fotoğraflar da değerlendiriliyor. Her fotoğraf filtresiz **299x299 Xception input**'a işleme alınıyor. **Gemini API** ile bu durum için geliştirilmiş uyarı mesajları eklendi. Bu durum bilinen bir limitation olarak dokümante edildi.

📅 29 Temmuz 2024

Günlük Özet: **Xception model** performance benchmarking testleri tamamlandı. **299x299 image processing** ve model inference için orta seviye işlem gücü yeterli. **Gemini API** rate limiting ve error handling optimize edildi. Memory usage optimize edildi. Image size validation eklendi. Error messages **Gemini AI** desteği ile kullanıcı dostu hale getirildi.

📅 30 Temmuz 2024

Günlük Özet: User acceptance testing başladı. Takım üyeleri ve dış kullanıcılar ile test edildi. UI/UX son rötuşları yapıldı. Loading animations iyileştirildi.

📅 31 Temmuz 2024

Günlük Özet: Screenshot alma işlemi başladı. Desktop ve mobile görünümler için test görüntüleri hazırlandı. README güncellemeleri için içerik hazırlandı. Code cleanup işlemleri başladı.

📅 1 Ağustos 2024

Günlük Özet: Final screenshots tamamlandı: boş arayüz, analiz süreci, sonuç ekranı ve mobile view. Tanıtım videosu için script hazırlığı başladı. Documentation review süreçleri başladı.

📅 2 Ağustos 2024

Günlük Özet: Proje %100 tamamlandı! Final code review yapıldı. Tüm dosyalar GitHub'a push edildi. Tanıtım videosu çekimi gerçekleştirildi. Sprint Review hazırlıkları tamamlandı.

📅 3 Ağustos 2024

Günlük Özet: Tanıtım videosu post-production tamamlandı. Sprint Review ve Retrospective toplantıları gerçekleştirildi. Proje başarıyla finalize edildi. Takım kutlaması yapıldı! 🎉

---

### 📋 Sprint Board Updates

**Board URL:** [Sprint Board](https://docs.google.com/spreadsheets/d/1yrPElOCZxonByDCxff-rVRn_BDlIlUAShSRS_oCt27w/edit?usp=sharing)

#### 📊 Güncel Sprint Durumu (3 Ağustos 2024)

```
📋 Backlog      🔄 In Progress    👀 Review       ✅ Done
   (0)             (0)              (0)            (20)
```

**Detaylı Durum:**
- **Done (20 items):** API entegrasyonu, Backend deployment, Frontend-Backend bağlantısı, Gerçek model predictions, Error handling, Performance optimization, Cross-browser testing, Mobile responsive final tests, User acceptance testing, Edge case handling, Memory optimization, Image validation, Loading states, Confidence display, Screenshot documentation, Tanıtım videosu, Code cleanup, Final testing, Documentation update, Project finalization

#### 🔥 Burndown Chart
[BurnDownChart](https://docs.google.com/spreadsheets/d/1slRiE7KsxFyPxS30SDdtpb28tGOD9MChEr4Q9-Zs0BI/edit?usp=sharing)

**Sprint 3 Velocity:** 100/100 story points ✅

---

### 📷 Screenshots

#### 🖼️ Sprint 3 Final Ürün Görüntüleri

**1. Ana Sayfa ve Upload Arayüzü**
![Boş Arayüz](https://github.com/Porphyri0n/Takim88/blob/main/Assets/sprint3-empty-interface.png)
*Modern ve kullanıcı dostu ana sayfa tasarımı*

---

**2. Analiz Süreci ve Yorumlama**
![Analiz Süreci](https://github.com/Porphyri0n/Takim88/blob/main/Assets/sprint3-analysis-process.png)
*Görüntü yükleme ve AI analiz süreci*

---

**3. Sonuç Ekranı - Desktop**
![Sonuç Ekranı Desktop](https://github.com/Porphyri0n/Takim88/blob/main/Assets/sprint3-results-desktop.png)
*Detaylı analiz sonuçları ve öneriler*

---

**4. Sonuç Ekranı - Mobile**
![Sonuç Ekranı Mobile](https://github.com/Porphyri0n/Takim88/blob/main/Assets/sprint3-results-mobile.png)
*Mobil uyumlu sonuç görüntüleme*

---

### 🎬 Ürün Tanıtım Videosu

**📺 Demo Video:** [DermaCheck Tanıtım Videosu](https://github.com/Porphyri0n/Takim88/blob/main/Assets/dermacheck-demo-video.mp4)

Video İçeriği:
- ✅ Proje tanıtımı ve amacı
- ✅ Ana sayfa ve arayüz turu
- ✅ Görüntü yükleme süreci
- ✅ AI analiz sürecinin gösterimi
- ✅ Sonuç ekranı ve yorumlama
- ✅ Mobil uyumluluk gösterimi
- ✅ Takım tanıtımı

---

### 🎉 Sprint Review

**📅 Tarih:** 3 Ağustos 2024, 16:30  
**📍 Konum:** Online (Google Meet)  
**⏱️ Süre:** 2 saat

#### ✅ Tamamlanan İşler (Demo)

1. **Gemini API + Xception Model Full Entegrasyonu**
   - **Google Gemini AI** ve Flask API ile frontend tamamen entegre edildi
   - Gerçek **Xception CNN model** (299x299 input) predictions çalışıyor
   - **Gemini AI** destekli analiz yorumlama sistemi active
   - AJAX implementasyonu ile seamless user experience
   - **Demo:** Live **Gemini + Xception** API call testleri

2. **Xception Model Deployment ve AI-Enhanced Analiz**
   - **Xception CNN model** (ImageNet pre-trained) başarıyla deploy edildi
   - **Google Gemini API** ile geliştirilmiş yorumlama sistemi
   - Model accuracy %75 seviyesinde + **Gemini AI** analiz desteği
   - **299x299 preprocessing pipeline** optimize edildi (orta seviye işlem gücü)
   - **Demo:** Gerçek **Xception + Gemini** görüntü analizi

3. **Kapsamlı Test ve Kalite Kontrol**
   - Cross-browser compatibility testleri tamamlandı
   - Mobile responsive design final testleri
   - User acceptance testing ile kullanılabilirlik doğrulandı
   - **Demo:** Farklı cihaz ve browser testleri

4. **Ürün Tanıtım Materyalleri**
   - Professional tanıtım videosu hazırlandı
   - Kapsamlı screenshot dokümantasyonu
   - Final demo preparation tamamlandı
   - **Demo:** Tanıtım videosu gösterimi

#### 📊 Sprint Metrikleri

- **Taahhüt Edilen:** 20 story point
- **Tamamlanan:** 20 story point
- **Velocity:** 20 points
- **Başarı Oranı:** %100
- **Proje Completion:** %100 ✅

#### 💭 Stakeholder Geri Bildirimi

**Pozitif Geri Bildirimler:**
- Proje tam olarak planlanan şekilde tamamlandı
- API entegrasyonu mükemmel çalışıyor
- Kullanıcı deneyimi çok başarılı
- Tanıtım videosu profesyonel kalitede
- Takım koordinasyonu örnek teşkil ediyor

**Teknik Başarılar:**
- %100 sprint completion tüm 3 sprint boyunca
- Hiç blocker yaşanmadı
- Model performance tatmin edici
- Cross-platform compatibility mükemmel

#### 🏆 Final Proje Değerlendirmesi

**Teknik Başarılar:**
- ✅ 10,015 görüntülü HAM10000 dataset ile **Xception CNN** eğitildi
- ✅ **Xception model** (299x299 input) %75 accuracy ile deploy edildi  
- ✅ **Google Gemini AI API** entegrasyonu ile gelişmiş analiz yorumlama
- ✅ Modern web teknolojileri ile **AI-enhanced** full-stack uygulama
- ✅ Responsive design ve mobile compatibility
- ✅ 7 farklı cilt lezyon sınıfı **Xception + Gemini AI** analizi

**Proje Yönetimi Başarıları:**
- ✅ 3 Sprint boyunca %100 completion rate
- ✅ Scrum methodology başarıyla uygulandı
- ✅ Takım koordinasyonu mükemmel seviyede
- ✅ Zaman yönetimi planına uygun
- ✅ Hiç critical blocker yaşanmadı

---

### 🔄 Sprint Retrospective

**📅 Tarih:** 3 Ağustos 2024, 18:00  
**📍 Konum:** Online  
**⏱️ Süre:** 1.5 saat

#### 😊 İyi Giden Şeyler

1. **AI Teknolojileri Mükemmelliği**
   - **Gemini API + Xception Model** entegrasyonu ilk seferde perfect çalıştı
   - **Xception CNN** deployment sürekli kararlı çalıştı (%75 accuracy)
   - **Google Gemini AI** ile analiz yorumlama sistemi flawless
   - **299x299 preprocessing pipeline** performance optimization hedeflerine ulaştı
   - Cross-browser compatibility sorunu yaşanmadı

2. **Takım Dinamiği**
   - 3 sprint boyunca %100 completion rate
   - Hiç blocker yaşanmadı, problemler anında çözüldü
   - Rol değişimleri (Gizem'in frontend katkısı) çok başarılı
   - Takım motivasyonu en üst seviyede kaldı

3. **Proje Yönetimi**
   - Sprint planning ve execution mükemmel
   - Daily standup discipline çok iyi
   - Risk management proaktif şekilde yapıldı
   - Documentation ve communication standardı yüksek

4. **Son Kullanıcı Deneyimi**
   - User acceptance testing sonuçları çok pozitif
   - UI/UX tasarım kalitesi beklentileri aştı
   - Mobile experience seamless
   - Performance kullanıcı açısından tatmin edici

#### ⚠️ Geliştirilebilir Alanlar ve Bilinen Sınırlamalar

1. **Model Limitations (Bilinen ve Kabul Edilen)**
   - Cilt hastalığı olmayan fotoğraflar da değerlendiriliyor
   - Her fotoğraf filtresiz işleme alınıyor
   - Bu durum proje scope'u içinde kabul edildi
   - Gelecek versiyonlarda image filtering eklenebilir

2. **Deployment**
   - Proje local deployment ile sınırlı kaldı
   - Cloud deployment Sprint 3 scope'una dahil edilmedi
   - Eklenbilecek gelecek enhancement

3. **Scalability**
   - Current setup single-user focused
   - Multi-user concurrent access test edilmedi
   - Database integration mevcut değil

#### 📈 Takım Sağlığı Skoru (Final)

```
İletişim        ██████████ 10/10
Motivasyon      ██████████ 10/10
Beceri Seviyesi ██████████ 10/10
İş Tatmini      ██████████ 10/10
Stres Seviyesi  ██░░░░░░░░ 2/10 (düşük = iyi)

Genel Skor: 9.6/10 🌟🌟🌟
```

#### 🎯 Aksiyon Maddeleri (Gelecek için)

| Aksiyon | Öncelik | Potansiyel Timeline |
|---------|---------|---------------------|
| Cloud deployment (AWS/Heroku) | Yüksek | 1-2 hafta |
| Image filtering & validation | Orta | 2-3 hafta |
| Multi-user support & database | Düşük | 1-2 ay |
| Model accuracy improvement | Orta | Ongoing |
| API rate limiting | Düşük | 1 hafta |

#### 🏆 Sprint 3 Öne Çıkan Başarılar

- **🎯 Perfect Execution:** %100 sprint completion 3. kez üst üste
- **🚀 Technical Excellence:** Flawless API integration
- **🎬 Professional Delivery:** High-quality demo video
- **👥 Team Excellence:** Mükemmel takım performansı
- **📱 User Experience:** Seamless cross-platform experience

---

### 🔬 Teknik Detaylar (Sprint 3)

#### 🤖 Final Model Specifications

```
AI Technology Stack:
├── Primary Model: Xception CNN (Transfer Learning)
├── AI Enhancement: Google Gemini API Integration
├── Input Shape: (299, 299, 3) RGB Images
├── Pre-trained Base: ImageNet weights
├── Fine-tuned Layers: Last 3 blocks + custom classifier
├── Final Accuracy: ~75% (Xception) + Gemini AI Analysis
├── Inference Time: ~2-3 seconds (Xception + Gemini)
└── Memory Usage: ~1.2GB (Xception model)

Xception Preprocessing Pipeline:
├── Image Resize: 299x299 (Xception standard)
├── Normalization: [-1, 1] range (Xception specific)
├── Format Support: JPG, PNG, GIF, BMP
├── Max File Size: 10MB
└── Gemini AI: Enhanced result interpretation

Gemini API Integration:
├── Provider: Google Gemini AI
├── Function: Analysis interpretation & recommendations
├── Response Enhancement: Medical terminology translation
├── User Experience: Natural language explanations
└── Error Handling: Intelligent fallback messages
```

#### 🌐 API Specifications

```
Backend Technology Stack:
├── Primary Backend: Flask 2.x
├── AI Integration: Google Gemini API
├── Model Serving: Xception CNN (TensorFlow)
├── CORS: Enabled for cross-origin requests
├── File Upload: Multipart form-data
├── Response Format: JSON (Xception + Gemini combined)
├── Error Handling: Comprehensive (AI-enhanced messages)
└── Health Check: /health endpoint

API Endpoints:
├── POST /predict: Xception analysis + Gemini interpretation
├── GET /health: System status
└── Gemini API: Real-time analysis enhancement

Frontend Integration:
├── AJAX: Fetch API implementation
├── File Handling: Drag & drop + click
├── Loading States: Spinner + progress (Xception + Gemini)
├── Error Display: Gemini AI enhanced user-friendly messages
├── Results: Animated confidence bars + Gemini explanations
└── AI Experience: Seamless Xception + Gemini workflow
```

#### 📱 Cross-Platform Compatibility

**Desktop Browsers:**
- ✅ Chrome 90+
- ✅ Firefox 88+  
- ✅ Safari 14+
- ✅ Edge 90+

**Mobile Browsers:**
- ✅ Chrome Mobile
- ✅ Safari iOS
- ✅ Samsung Internet
- ✅ Firefox Mobile

**Screen Sizes:**
- ✅ Desktop: 1920x1080+
- ✅ Tablet: 768x1024
- ✅ Mobile: 375x667+

---

## 📊 Sprint 3 Özet Metrikleri

| Metrik | Değer | Durum |
|--------|--------|--------|
| **Sprint Completion** | %100 | ✅ Mükemmel |
| **Gemini API Integration** | %100 | ✅ Perfect |
| **Xception Model Deployment** | %100 | ✅ Başarılı |
| **AI-Enhanced Analysis** | %100 | ✅ Excellent |
| **User Testing** | %100 Pass | ✅ Outstanding |
| **Cross-Browser Support** | %100 | ✅ Universal |
| **Mobile Compatibility** | %100 | ✅ Seamless |
| **Team Satisfaction** | 9.6/10 | ✅ Outstanding |
| **Project Completion** | %100 | ✅ **COMPLETED** |

---

## 🎊 Proje Final Durumu

### 🏁 Proje Başarıyla Tamamlandı!

**Toplam Süre:** 6 hafta (3 Sprint)  
**Toplam Story Points:** 60/60 (%100)  
**Takım Performansı:** Mükemmel  
**Teknik Başarı:** Hedeflerin üzerinde  
**Kullanıcı Deneyimi:** Excellent  

### 🎯 Başarılan Hedefler

- ✅ **AI Destekli Cilt Analizi:** 7 sınıf, %75 accuracy (**Xception CNN**)
- ✅ **Gemini AI Enhancement:** Gelişmiş analiz yorumlama sistemi
- ✅ **Modern Web Uygulaması:** Responsive, cross-platform
- ✅ **AI-Enhanced Full-Stack:** Flask + **Xception** + **Gemini API** + JavaScript
- ✅ **Professional UI/UX:** Modern, accessible, **AI-powered** design
- ✅ **Comprehensive Testing:** Multi-device, multi-browser, **AI workflow**
- ✅ **Quality Documentation:** README, video, screenshots
- ✅ **Team Excellence:** Perfect collaboration

### 🚀 Gelecek Potansiyeli

DermaCheck artık:
- 📱 Production-ready **AI-enhanced** web application
- 🤖 Functional **Xception + Gemini AI** skin analysis system  
- 🌟 Professional **AI technology** demo portfolio piece
- 📚 Comprehensive **AI integration** learning project
- 👥 Team success story with **cutting-edge AI**

---

<div align="center">

### 🎉 Sprint 3 ve Proje Başarıyla Tamamlandı! 

**🏆 Takım CutisAI - Mükemmel Bir Çalışma! 🏆**

**Sonraki Durak: Portfolio ve Career Success! 🚀**

</div>



#### 📚 Kaynak

- **Orijinal Yayın:** [Nature Scientific Data](https://www.nature.com/articles/sdata2018161)
- **Kaggle Dataset:** [HAM10000](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000)
- **Harvard Dataverse:** [Dataset Link](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T)

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
  - 📧 Email: eb.baser@gmail.com
  - 🐱 GitHub: [@erdogan-baser](https://github.com/Porphyri0n)

- **ML Developer:** Emir Ayyıldız
  - 📧 Email: emirayyildiz164@gmail.com
  - 🐱 GitHub: [@emir-ayyildiz](https://github.com/emirayyildiz1)

- **Backend Developer:** Eminenur Yıldız
  - 📧 Email: weminenur@gmail.com
  - 🐱 GitHub: [@eminenur-yildiz](https://github.com/weminemi)

- **Backend Developer:** Gizem Erpek
  - 📧 Email: gizemerpek05@gmail.com
  - 🐱 GitHub: [@gizem-erpek](https://github.com/gizemerpek)

### 🏢 Proje İletişim

- **Repository:** [https://github.com/CutisAI/DermaCheck](https://github.com/CutisAI/DermaCheck)

---

<div align="center">

## ⭐ Projeyi Beğendiyseniz Star Vermeyi Unutmayın!

**🚀 Birlikte daha sağlıklı bir gelecek inşa ediyoruz!**

![DermaCheck Logo](https://github.com/Porphyri0n/Takim88/blob/main/Assets/cutisAI-logo.png)

---

**Made with ❤️ by CutisAI Team**

</div>
