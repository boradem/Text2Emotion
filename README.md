# Text2Emotion - Gelişmiş Duygu Analizi Aracı

Bu proje, metinlerdeki duyguları analiz eden gelişmiş bir Python uygulamasıdır. Hem Türkçe hem İngilizce destekli, performans odaklı bir duygu analizi aracıdır.

## 🚀 Özellikler

- 📝 **Çok Dilli Destek**: Türkçe ve İngilizce metin analizi
- 🎭 **5 Duygu Kategorisi**: Happy, Angry, Surprise, Sad, Fear
- 📊 **Görsel Sonuçlar**: Çubuk grafiklerle duygu skorları
- 🎯 **Baskın Duygu Tespiti**: En yüksek skorlu duygu
- 💬 **İnteraktif Arayüz**: Kolay kullanım
- ⚡ **Yüksek Performans**: Caching ve lazy loading
- 🌐 **Web API**: FastAPI ile REST API
- 🐳 **Docker Desteği**: Kolay deployment
- 📈 **Logging**: Detaylı log sistemi
- 🧪 **Kapsamlı Testler**: Unit testler ve coverage

## 📦 Kurulum

### 1. Temel Kurulum
```bash
# Repository'yi klonlayın
git clone https://github.com/boradem/Text2Emotion.git
cd Text2Emotion

# Sanal ortam oluşturun
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Bağımlılıkları yükleyin
pip install -r requirements.txt
```

### 2. Docker ile Kurulum
```bash
# Docker image'ı build edin
docker build -t text2emotion .

# Container'ı çalıştırın
docker run -p 8000:8000 text2emotion
```

### 3. Docker Compose ile Kurulum
```bash
# Tüm servisleri başlatın
docker-compose up -d
```

## 🎯 Kullanım

### Komut Satırı Arayüzü
```bash
python Text2Emotion.py
```

### Web API
```bash
# API server'ı başlatın
python api_server.py

# API'yi test edin
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"text": "Bugün çok mutluyum!", "language": "auto"}'
```

### Programatik Kullanım
```python
from Text2Emotion import detect_emotion, analyze_emotion_with_details
from turkish_emotion_analyzer import TurkishEmotionAnalyzer

# İngilizce analiz
emotions = detect_emotion("I am very happy today!")
print(emotions)

# Türkçe analiz
analyzer = TurkishEmotionAnalyzer()
analysis = analyzer.analyze_with_details("Bugün çok mutluyum!")
print(analysis)
```

## 🌐 API Endpoints

### POST /analyze
Metin duygu analizi yapar.

**Request:**
```json
{
  "text": "Bugün çok mutluyum!",
  "language": "auto"
}
```

**Response:**
```json
{
  "text": "Bugün çok mutluyum!",
  "detected_language": "tr",
  "emotions": {
    "Happy": 0.75,
    "Sad": 0.0,
    "Angry": 0.0,
    "Fear": 0.0,
    "Surprise": 0.25
  },
  "dominant_emotion": "Happy",
  "dominant_score": 0.75,
  "processing_time": 0.123
}
```

### GET /health
API sağlık kontrolü.

### GET /languages
Desteklenen dilleri listeler.

## 🧪 Testler

### Temel Testler
```bash
python test_emotion.py
python test_turkish_emotion.py
```

### Kapsamlı Test Coverage
```bash
python test_coverage.py
```

## 📊 Performans

- **Caching**: LRU cache ile tekrarlanan işlemler hızlandırılır
- **Lazy Loading**: Türkçe analizör sadece gerektiğinde yüklenir
- **Memory Optimization**: Bellek kullanımı optimize edilmiştir
- **Processing Time**: İşlem süreleri loglanır

## 🐳 Docker

### Build
```bash
docker build -t text2emotion .
```

### Run
```bash
docker run -p 8000:8000 text2emotion
```

### Docker Compose
```bash
docker-compose up -d
```

## 📈 Monitoring

### Logs
Loglar `logs/` dizininde günlük dosyalar halinde saklanır:
```
logs/text2emotion_20241201.log
```

### Health Check
```bash
curl http://localhost:8000/health
```

## 🔧 Geliştirme

### Yeni Duygu Kelimesi Ekleme
`turkish_emotion_analyzer.py` dosyasındaki `emotion_words` sözlüğüne yeni kelimeler ekleyebilirsiniz.

### Yeni Dil Desteği
1. Yeni dil için analizör sınıfı oluşturun
2. `detect_language` fonksiyonunu güncelleyin
3. API'ye yeni dil desteği ekleyin

## 📋 Gereksinimler

- Python 3.8+
- text2emotion==0.0.5
- nltk==3.8.1
- emoji==1.7.0
- fastapi==0.104.1
- uvicorn==0.24.0
- pydantic==2.5.0

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit edin (`git commit -m 'Add amazing feature'`)
4. Push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında açık kaynak kodludur.

## 🆘 Destek

Sorunlarınız için GitHub Issues kullanın veya email gönderin.
