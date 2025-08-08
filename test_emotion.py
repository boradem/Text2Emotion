#!/usr/bin/env python3
"""
Test script for Text2Emotion
"""

from Text2Emotion import detect_emotion, analyze_emotion_with_details

def test_emotion_detection():
    """Test emotion detection with various texts"""
    
    test_cases = [
        {
            "text": "I am very happy today! The weather is great!",
            "expected_dominant": "Happy"
        },
        {
            "text": "I'm so angry about what happened yesterday.",
            "expected_dominant": "Angry"
        },
        {
            "text": "I'm feeling sad and depressed.",
            "expected_dominant": "Sad"
        },
        {
            "text": "Wow! That's amazing! I can't believe it!",
            "expected_dominant": "Surprise"
        },
        {
            "text": "I'm scared and afraid of what might happen.",
            "expected_dominant": "Fear"
        }
    ]
    
    print("🧪 Duygu Analizi Testleri")
    print("=" * 50)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test_case['text']}")
        
        try:
            analysis = analyze_emotion_with_details(test_case['text'])
            dominant = analysis['dominant_emotion']
            expected = test_case['expected_dominant']
            
            if dominant == expected:
                print(f"✅ Başarılı! Beklenen: {expected}, Bulunan: {dominant}")
            else:
                print(f"❌ Başarısız! Beklenen: {expected}, Bulunan: {dominant}")
            
            print(f"   Skorlar: {analysis['emotions']}")
            
        except Exception as e:
            print(f"❌ Hata: {e}")

def test_edge_cases():
    """Test edge cases"""
    print("\n🔍 Sınır Durumları Testleri")
    print("=" * 50)
    
    edge_cases = [
        "",  # Boş metin
        "   ",  # Sadece boşluk
        "123456",  # Sadece sayılar
        "!@#$%^&*()",  # Sadece özel karakterler
        "a",  # Tek karakter
        "I am feeling neutral about this situation."  # Nötr metin
    ]
    
    for i, text in enumerate(edge_cases, 1):
        print(f"\nEdge Case {i}: '{text}'")
        
        try:
            analysis = analyze_emotion_with_details(text)
            print(f"✅ Başarılı! Baskın duygu: {analysis['dominant_emotion']}")
            print(f"   Skorlar: {analysis['emotions']}")
        except Exception as e:
            print(f"❌ Hata: {e}")

if __name__ == "__main__":
    test_emotion_detection()
    test_edge_cases()
    
    print("\n🎉 Tüm testler tamamlandı!")
