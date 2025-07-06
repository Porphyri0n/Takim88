<!-- README.md for DermaCheck - Sprint 1 Detayları -->

<style>
  /* Genel Stil */
  body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; line-height: 1.6; color: #333; }
  h1, h2, h3 { text-align: center; }
  h1 { 
    background: linear-gradient(90deg, #00C9FF, #92FE9D); 
    -webkit-background-clip: text; 
    -webkit-text-fill-color: transparent;
    font-size: 3em; margin-bottom: 0.2em;
  }
  .badge { display: inline-block; margin: 0 0.3em; vertical-align: middle; }
  .table-container { overflow-x: auto; margin: 1em 0; }
  table { width: 100%; border-collapse: collapse; }
  th, td { padding: 0.75em 1em; border: 1px solid #ddd; }
  th { background: #f5f5f5; }
  tr:nth-child(even) { background: #fafafa; }
  .task-owner { font-weight: bold; color: #0366d6; }
  .points { font-family: monospace; background: #eef; padding: 0.1em 0.4em; border-radius: 3px; }
  .note { font-style: italic; color: #555; }
</style>

<h1>🚀 DermaCheck — Sprint 1 Detayları</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Sprint-1-blue" alt="Sprint 1" class="badge"/>
  <img src="https://img.shields.io/badge/Date-20%20Haziran%20%E2%80%93%206%20Temmuz-red" alt="Dates" class="badge"/>
  <img src="https://img.shields.io/badge/Status-In%20Progress-orange" alt="In Progress" class="badge"/>
</p>

---

## 🎯 Sprint 1 Hedefi

**Veri Hazırlığı & Keşif**  
HAM10000 veri setini hazırlayıp inceleyerek, model eğitimi için sağlam bir temel oluşturmak.

---

## 📋 Görev Listesi

<div class="table-container">
<table>
  <thead>
    <tr>
      <th>#</th>
      <th>Task</th>
      <th>Owner</th>
      <th>Points</th>
      <th>Detaylar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>HAM10000 dataset indirme & klasör yapısı oluşturma</td>
      <td class="task-owner">Gizem Erpek</td>
      <td><span class="points">5</span></td>
      <td>
        <ul>
          <li>Kaggle’dan `skin-cancer-mnist-ham10000` verisinin çekilmesi</li>
          <li>Proje kökünde `data/raw/HAM10000/` klasör hiyerarşisi</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>2</td>
      <td>Görüntü ön işleme pipeline’ı geliştirme</td>
      <td class="task-owner">Erdoğan Başer</td>
      <td><span class="points">8</span></td>
      <td>
        <ul>
          <li>Resize (224×224), normalize etme</li>
          <li>Basit augmentasyon (flip, rotate)</li>
          <li>Reusable Python modülü: `preprocessing.py`</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>3</td>
      <td>Eksik etiket ve class dengesine bakma</td>
      <td class="task-owner">Emir Ayyıldız</td>
      <td><span class="points">5</span></td>
      <td>
        <ul>
          <li>Her sınıf için örnek sayısı raporu</li>
          <li>Gerekirse oversampling stratejisi belirleme</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>4</td>
      <td>Keşifsel Veri Analizi (EDA)</td>
      <td class="task-owner">Eminenur Yıldız</td>
      <td><span class="points">8</span></td>
      <td>
        <ul>
          <li>Notebook: sınıf dağılım grafikleri</li>
          <li>Örnek görsellerin görselleştirilmesi</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>5</td>
      <td>Veri kalitesi dashboard’u</td>
      <td class="task-owner">Gizem Erpek</td>
      <td><span class="points">5</span></td>
      <td>
        <ul>
          <li>Pandas Profiling ya da custom Streamlit tablosu</li>
          <li>Eksik değer & aykırı değer raporu</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>6</td>
      <td>Scrum setup & Daily Scrum</td>
      <td class="task-owner">Erdoğan Başer</td>
      <td><span class="points">3</span></td>
      <td>
        <ul>
          <li>Slack kanalı oluşturma</li>
          <li>Jira/Miro board template’i paylaşma</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
</div>

---

## 📅 Zaman Çizelgesi

| Hafta                  | Aktivite                                    |
|------------------------|----------------------------------------------|
| **20–22 Haziran**      | Data indirme & klasör hiyerarşisi oluşturma  |
| **23–26 Haziran**      | Ön işleme pipeline geliştirme                |
| **27–29 Haziran**      | Eksik etiket kontrol & denge analizi         |
| **30 Haziran–3 Temmuz**| EDA notebook tamamlama                       |
| **4–6 Temmuz**         | Dashboard ve Scrum ayarları                  |

---

## 📦 Çıktılar

- **Sprint Notları:**  
  - `notebooks/data_exploration.ipynb` üzerinden bulgular
- **Sprint Board Güncellemesi:**  
  - `screenshots/board_sprint1_*.png`
- **Demo Screenshots:**  
  - Örnek EDA grafikleri ve preprocess öncesi/sonrası görseller
- **Review & Retrospective:**  
  - `docs/sprint1_review.md` ve `docs/sprint1_retro.md`

> <span class="note">Not: İlk commit ve placeholder dosyalar 20 Haziran’da eklenecek!</span>

---

<p align="center">
  <strong>CutisAI / DermaCheck</strong> • Sprint 1 • 20 Haziran – 6 Temmuz  
</p>
