# Text2Emotion - Duygu Analizi Aracı

Bu proje, metinlerdeki duyguları analiz eden bir Python uygulamasıdır. `text2emotion` kütüphanesi kullanılarak geliştirilmiştir.

## Özellikler

- 📝 Metin temizleme ve ön işleme
- 🎭 5 farklı duygu kategorisi analizi (Happy, Angry, Surprise, Sad, Fear)
- 📊 Görsel duygu skorları
- 🎯 Baskın duygu tespiti
- 💬 İnteraktif kullanıcı arayüzü

## Kurulum

1. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

2. Programı çalıştırın:
```bash
python Text2Emotion.py
```

## Kullanım

### İnteraktif Mod
Program çalıştırıldığında otomatik olarak interaktif moda geçer:
- Analiz edilecek metni girin
- Sonuçları görüntüleyin
- Çıkmak için 'quit' yazın

### Programatik Kullanım
```python
from Text2Emotion import detect_emotion, analyze_emotion_with_details

# Basit kullanım
emotions = detect_emotion("I am very happy today!")
print(emotions)

# Detaylı analiz
analysis = analyze_emotion_with_details("I am very happy today!")
print(analysis)
```

## Çıktı Formatı

Program şu duygu kategorilerini analiz eder:
- **Happy** (Mutlu)
- **Angry** (Kızgın)
- **Surprise** (Şaşkın)
- **Sad** (Üzgün)
- **Fear** (Korku)

Her duygu için 0-1 arasında bir skor döndürülür.

## Örnek Çıktı

```
==================================================
DUYGU ANALİZİ SONUÇLARI
==================================================
Orijinal Metin: I am very happy today!

Duygu Skorları:
------------------------------
Happy        : ████████████████████ 0.850
Angry        : █ 0.050
Surprise     : ██ 0.100
Sad          : █ 0.050
Fear         : █ 0.050

Baskın Duygu: Happy
Skor: 0.850
==================================================
```

## Gereksinimler

- Python 3.6+
- text2emotion
- nltk

## Lisans

Bu proje açık kaynak kodludur.
