#!/usr/bin/env python3
"""
Türkçe Duygu Analizi Modülü
"""

import re
from typing import Dict, List, Tuple

class TurkishEmotionAnalyzer:
    """Türkçe metinler için duygu analizi sınıfı"""
    
    def __init__(self):
        # Türkçe duygu kelimeleri
        self.emotion_words = {
            'Happy': [
                'mutlu', 'sevinçli', 'neşeli', 'keyifli', 'güzel', 'harika', 'mükemmel',
                'güldüm', 'gülüyorum', 'eğlenceli', 'hoş', 'tatlı', 'sevimli', 'güzel',
                'başarılı', 'kazandım', 'kazandık', 'kutlama', 'tebrik', 'ödül', 'hediye',
                'aşık', 'aşk', 'sevgi', 'dost', 'arkadaş', 'aile', 'ev', 'yuva', 'sıcak',
                'güneş', 'bahar', 'yaz', 'tatil', 'gezi', 'seyahat', 'macera', 'keşif'
            ],
            'Sad': [
                'üzgün', 'kederli', 'mutsuz', 'hüzünlü', 'yaslı', 'kırgın', 'kırık',
                'ağladım', 'ağlıyorum', 'gözyaşı', 'acı', 'keder', 'yas', 'ölüm',
                'kaybettim', 'kaybettik', 'başarısız', 'başarısızlık', 'red', 'ret',
                'yalnız', 'yalnızlık', 'terk', 'ayrılık', 'boşanma', 'kayıp', 'kayıp',
                'hasta', 'hastalık', 'acı', 'ağrı', 'sızı', 'yorgun', 'bitkin', 'tükenmiş',
                'üzgünüm', 'kederliyim', 'mutsuzum', 'hüzünlüyüm', 'yaslıyım', 'kırgınım',
                'ağlıyorum', 'ağladım', 'gözyaşı', 'acı', 'keder', 'yas', 'ölüm',
                'kaybettim', 'kaybettik', 'başarısızım', 'başarısızlık', 'red', 'ret',
                'yalnızım', 'yalnızlık', 'terk', 'ayrılık', 'boşanma', 'kayıp', 'kayıp',
                'hastayım', 'hastalık', 'acı', 'ağrı', 'sızı', 'yorgunum', 'bitkinim', 'tükenmişim'
            ],
            'Angry': [
                'kızgın', 'öfkeli', 'sinirli', 'kırgın', 'kırık', 'kırıldım', 'kırıldık',
                'küstüm', 'küstük', 'dargın', 'dargınlık', 'kavga', 'tartışma', 'çatışma',
                'savaş', 'saldırı', 'şiddet', 'vur', 'döv', 'öldür', 'katil', 'katil',
                'hırsız', 'hırsızlık', 'dolandırıcı', 'aldatma', 'ihanet', 'ihanet',
                'kötü', 'berbat', 'rezalet', 'felaket', 'kabus', 'korkunç', 'dehşet',
                'kızgınım', 'öfkeliyim', 'sinirliyim', 'kırgınım', 'kırıldım', 'kırıldık',
                'küstüm', 'küstük', 'dargınım', 'dargınlık', 'kavga', 'tartışma', 'çatışma',
                'savaş', 'saldırı', 'şiddet', 'vur', 'döv', 'öldür', 'katil', 'katil',
                'hırsız', 'hırsızlık', 'dolandırıcı', 'aldatma', 'ihanet', 'ihanet',
                'kötüyüm', 'berbatım', 'rezalet', 'felaket', 'kabus', 'korkunç', 'dehşet'
            ],
            'Fear': [
                'korku', 'korkuyorum', 'korktum', 'korkunç', 'dehşet', 'panik', 'endişe',
                'kaygı', 'stres', 'gerilim', 'tedirgin', 'huzursuz', 'rahatsız', 'sıkıntı',
                'tehlike', 'risk', 'tehdit', 'saldırı', 'şiddet', 'ölüm', 'hastalık',
                'kaza', 'felaket', 'deprem', 'sel', 'yangın', 'bomba', 'silah', 'savaş',
                'karanlık', 'gece', 'gölge', 'hayalet', 'cin', 'şeytan', 'iblis',
                'korkuyorum', 'korktum', 'korkunç', 'dehşet', 'panik', 'endişeliyim',
                'kaygılıyım', 'stresliyim', 'gerilimliyim', 'tedirginim', 'huzursuzum', 'rahatsızım', 'sıkıntılıyım',
                'tehlikeli', 'riskli', 'tehditli', 'saldırı', 'şiddet', 'ölüm', 'hastalık',
                'kaza', 'felaket', 'deprem', 'sel', 'yangın', 'bomba', 'silah', 'savaş',
                'karanlık', 'gece', 'gölge', 'hayalet', 'cin', 'şeytan', 'iblis'
            ],
            'Surprise': [
                'şaşkın', 'şaşırdım', 'şaşırıyorum', 'inanılmaz', 'inanılmaz', 'müthiş',
                'harika', 'muhteşem', 'olağanüstü', 'sıra dışı', 'beklenmedik', 'ani',
                'aniden', 'birden', 'ansızın', 'beklenmedik', 'sürpriz', 'sürpriz',
                'keşif', 'buldum', 'bulduk', 'buluş', 'icat', 'yenilik', 'yeni',
                'farklı', 'değişik', 'tuhaf', 'garip', 'acayip', 'ilginç', 'merak',
                'meraklı', 'heyecan', 'heyecanlı', 'coşku', 'coşkulu', 'enerjik',
                'şaşkınım', 'şaşırdım', 'şaşırıyorum', 'inanılmaz', 'inanılmaz', 'müthişim',
                'harikayım', 'muhteşemim', 'olağanüstüyüm', 'sıra dışıyım', 'beklenmedik', 'ani',
                'aniden', 'birden', 'ansızın', 'beklenmedik', 'sürpriz', 'sürpriz',
                'keşif', 'buldum', 'bulduk', 'buluş', 'icat', 'yenilik', 'yeni',
                'farklıyım', 'değişik', 'tuhafım', 'garibim', 'acayibim', 'ilginç', 'meraklıyım',
                'meraklı', 'heyecanlıyım', 'heyecanlı', 'coşkulu', 'coşkulu', 'enerjik'
            ]
        }
        
        # Türkçe stopwords
        self.turkish_stopwords = {
            'ben', 'sen', 'o', 'biz', 'siz', 'onlar', 'bu', 'şu', 'o', 'bunlar',
            'şunlar', 'onlar', 'bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi',
            'sekiz', 'dokuz', 'on', 've', 'ile', 'için', 'gibi', 'kadar', 'doğru',
            'yanlış', 'evet', 'hayır', 'tamam', 'tamam', 'olur', 'olmaz', 'var',
            'yok', 'için', 'içinde', 'dışında', 'üstünde', 'altında', 'yanında',
            'karşısında', 'önünde', 'arkasında', 'arasında', 'ortasında', 'başında',
            'sonunda', 'başında', 'sonunda', 'içinde', 'dışında', 'üstünde', 'altında'
        }
    
    def clean_text(self, text: str) -> str:
        """Metni temizle ve normalize et"""
        # Küçük harfe çevir
        text = text.lower()
        
        # Türkçe karakterleri normalize et
        text = text.replace('ı', 'i').replace('ğ', 'g').replace('ü', 'u')
        text = text.replace('ş', 's').replace('ö', 'o').replace('ç', 'c')
        
        # Özel karakterleri temizle (noktalama işaretleri hariç)
        text = re.sub(r'[^\w\s]', ' ', text)
        
        # Fazla boşlukları temizle
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def remove_stopwords(self, text: str) -> str:
        """Türkçe stopwords'leri kaldır"""
        words = text.split()
        filtered_words = [word for word in words if word not in self.turkish_stopwords]
        return ' '.join(filtered_words)
    
    def analyze_emotion(self, text: str) -> Dict[str, float]:
        """Türkçe metin için duygu analizi yap"""
        if not text or not text.strip():
            return {'Happy': 0.0, 'Sad': 0.0, 'Angry': 0.0, 'Fear': 0.0, 'Surprise': 0.0}
        
        # Metni temizle
        cleaned_text = self.clean_text(text)
        
        # Stopwords'leri kaldır
        processed_text = self.remove_stopwords(cleaned_text)
        
        # Kelimeleri say
        words = processed_text.split()
        total_words = len(words) if words else 1
        
        # Her duygu için skor hesapla
        emotion_scores = {}
        
        for emotion, emotion_word_list in self.emotion_words.items():
            count = 0
            for word in words:
                # Kelime eşleşmesini kontrol et
                if word in emotion_word_list:
                    count += 1
                else:
                    # Alt kelime eşleşmesi kontrol et
                    for emotion_word in emotion_word_list:
                        if word in emotion_word or emotion_word in word:
                            count += 0.5  # Kısmi eşleşme için yarım puan
                            break
            
            # Skoru normalize et (0-1 arası)
            score = count / total_words
            emotion_scores[emotion] = min(score * 3, 1.0)  # Daha belirgin skorlar için
        
        return emotion_scores
    
    def get_dominant_emotion(self, emotions: Dict[str, float]) -> Tuple[str, float]:
        """Baskın duyguyu bul"""
        if not emotions:
            return 'Happy', 0.0
        
        dominant_emotion = max(emotions, key=emotions.get)
        dominant_score = emotions[dominant_emotion]
        
        return dominant_emotion, dominant_score
    
    def analyze_with_details(self, text: str) -> Dict:
        """Detaylı duygu analizi"""
        emotions = self.analyze_emotion(text)
        dominant_emotion, dominant_score = self.get_dominant_emotion(emotions)
        
        return {
            'emotions': emotions,
            'dominant_emotion': dominant_emotion,
            'dominant_score': dominant_score,
            'original_text': text,
            'processed_text': self.remove_stopwords(self.clean_text(text))
        }

def print_turkish_analysis(analysis: Dict):
    """Türkçe analiz sonuçlarını yazdır"""
    print("\n" + "="*50)
    print("TÜRKÇE DUYGU ANALİZİ SONUÇLARI")
    print("="*50)
    print(f"Orijinal Metin: {analysis['original_text']}")
    print(f"İşlenmiş Metin: {analysis['processed_text']}")
    print("\nDuygu Skorları:")
    print("-" * 30)
    
    emotion_names = {
        'Happy': 'Mutlu',
        'Sad': 'Üzgün', 
        'Angry': 'Kızgın',
        'Fear': 'Korku',
        'Surprise': 'Sürpriz'
    }
    
    for emotion, score in analysis['emotions'].items():
        bar_length = int(score * 20)
        bar = "█" * bar_length
        turkish_name = emotion_names.get(emotion, emotion)
        print(f"{turkish_name:<12}: {bar} {score:.3f}")
    
    dominant_turkish = emotion_names.get(analysis['dominant_emotion'], analysis['dominant_emotion'])
    print(f"\nBaskın Duygu: {dominant_turkish}")
    print(f"Skor: {analysis['dominant_score']:.3f}")
    print("="*50)

if __name__ == "__main__":
    analyzer = TurkishEmotionAnalyzer()
    
    # Test örnekleri
    test_texts = [
        "Bugün çok mutluyum!",
        "Çok üzgünüm ve ağlıyorum.",
        "Bu duruma çok kızgınım!",
        "Karanlıktan korkuyorum.",
        "Bu haber beni çok şaşırttı!"
    ]
    
    for text in test_texts:
        analysis = analyzer.analyze_with_details(text)
        print_turkish_analysis(analysis)
