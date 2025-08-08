#!/usr/bin/env python3
"""
Türkçe Duygu Analizi Test Dosyası
"""

from turkish_emotion_analyzer import TurkishEmotionAnalyzer, print_turkish_analysis

def test_turkish_emotion_detection():
    """Türkçe duygu analizi testleri"""
    
    test_cases = [
        {
            "text": "Bugün çok mutluyum! Harika bir gün geçiriyorum.",
            "expected_dominant": "Happy"
        },
        {
            "text": "Çok üzgünüm ve ağlıyorum. Hayat çok zor.",
            "expected_dominant": "Sad"
        },
        {
            "text": "Bu duruma çok kızgınım! Sinirlerim bozuldu.",
            "expected_dominant": "Angry"
        },
        {
            "text": "Karanlıktan korkuyorum. Çok endişeliyim.",
            "expected_dominant": "Fear"
        },
        {
            "text": "Bu haber beni çok şaşırttı! İnanılmaz!",
            "expected_dominant": "Surprise"
        }
    ]
    
    print("🧪 Türkçe Duygu Analizi Testleri")
    print("=" * 50)
    
    analyzer = TurkishEmotionAnalyzer()
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test_case['text']}")
        
        try:
            analysis = analyzer.analyze_with_details(test_case['text'])
            dominant = analysis['dominant_emotion']
            expected = test_case['expected_dominant']
            
            if dominant == expected:
                print(f"✅ Başarılı! Beklenen: {expected}, Bulunan: {dominant}")
            else:
                print(f"❌ Başarısız! Beklenen: {expected}, Bulunan: {dominant}")
            
            print(f"   Skorlar: {analysis['emotions']}")
            
        except Exception as e:
            print(f"❌ Hata: {e}")

def test_turkish_edge_cases():
    """Türkçe sınır durumları testleri"""
    print("\n🔍 Türkçe Sınır Durumları Testleri")
    print("=" * 50)
    
    analyzer = TurkishEmotionAnalyzer()
    
    edge_cases = [
        "",  # Boş metin
        "   ",  # Sadece boşluk
        "123456",  # Sadece sayılar
        "!@#$%^&*()",  # Sadece özel karakterler
        "a",  # Tek karakter
        "Bugün hava güzel.",  # Nötr metin
        "Çok güzel bir gün geçiriyorum.",  # Mutlu metin
        "Hayat çok zor ve acımasız.",  # Üzgün metin
        "Bu işi yapmak istemiyorum.",  # Kızgın metin
        "Gece karanlığından korkuyorum.",  # Korku metni
        "Bu sürpriz beni çok şaşırttı!"  # Şaşkın metin
    ]
    
    for i, text in enumerate(edge_cases, 1):
        print(f"\nEdge Case {i}: '{text}'")
        
        try:
            analysis = analyzer.analyze_with_details(text)
            print(f"✅ Başarılı! Baskın duygu: {analysis['dominant_emotion']}")
            print(f"   Skorlar: {analysis['emotions']}")
        except Exception as e:
            print(f"❌ Hata: {e}")

def test_language_detection():
    """Dil tespiti testleri"""
    print("\n🌍 Dil Tespiti Testleri")
    print("=" * 50)
    
    from Text2Emotion import detect_language
    
    test_texts = [
        "Bugün çok mutluyum!",  # Türkçe
        "I am very happy today!",  # İngilizce
        "Çok güzel bir gün!",  # Türkçe
        "This is amazing!",  # İngilizce
        "Korkuyorum ve endişeliyim.",  # Türkçe
        "I am scared and worried.",  # İngilizce
        "Hello world",  # İngilizce
        "Merhaba dünya",  # Türkçe
    ]
    
    for i, text in enumerate(test_texts, 1):
        is_turkish = detect_language(text)
        detected_lang = "Türkçe" if is_turkish else "İngilizce"
        print(f"Test {i}: '{text}' -> {detected_lang}")

if __name__ == "__main__":
    test_turkish_emotion_detection()
    test_turkish_edge_cases()
    test_language_detection()
    
    print("\n🎉 Tüm Türkçe testler tamamlandı!")
