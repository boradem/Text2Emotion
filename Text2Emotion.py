import text2emotion as te
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
from turkish_emotion_analyzer import TurkishEmotionAnalyzer, print_turkish_analysis

def download_nltk_data():
    """Download required NLTK data"""
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')

def clean_text(text):
    """Clean and preprocess text"""
    # Convert to lowercase
    text = text.lower()
    # Remove special characters but keep spaces
    text = re.sub(r'[^\w\s]', '', text)
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text

def remove_stopwords(text):
    """Remove stopwords from text"""
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

def detect_emotion(text):
    """Detect emotions in the given text"""
    # Download required NLTK data
    download_nltk_data()
    
    # Clean the text
    cleaned_text = clean_text(text)
    
    # Remove stopwords
    processed_text = remove_stopwords(cleaned_text)
    
    # Get emotion predictions
    emotions = te.get_emotion(processed_text)
    
    return emotions

def analyze_emotion_with_details(text):
    """Analyze emotion with detailed information"""
    emotions = detect_emotion(text)
    
    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    dominant_score = emotions[dominant_emotion]
    
    return {
        'emotions': emotions,
        'dominant_emotion': dominant_emotion,
        'dominant_score': dominant_score,
        'original_text': text
    }

def print_emotion_analysis(analysis):
    """Print emotion analysis results in a formatted way"""
    print("\n" + "="*50)
    print("DUYGU ANALİZİ SONUÇLARI")
    print("="*50)
    print(f"Orijinal Metin: {analysis['original_text']}")
    print("\nDuygu Skorları:")
    print("-" * 30)
    
    for emotion, score in analysis['emotions'].items():
        bar_length = int(score * 20)  # Scale for visualization
        bar = "█" * bar_length
        print(f"{emotion.capitalize():<12}: {bar} {score:.3f}")
    
    print(f"\nBaskın Duygu: {analysis['dominant_emotion'].capitalize()}")
    print(f"Skor: {analysis['dominant_score']:.3f}")
    print("="*50)

def detect_language(text):
    """Basit dil tespiti - Türkçe karakterler varsa Türkçe kabul et"""
    turkish_chars = set('çğıöşü')
    text_lower = text.lower()
    turkish_char_count = sum(1 for char in text_lower if char in turkish_chars)
    
    # Türkçe kelimeler
    turkish_words = ['ben', 'sen', 'o', 'biz', 'siz', 'onlar', 'bu', 'şu', 'bir', 'iki', 'üç']
    turkish_word_count = sum(1 for word in text_lower.split() if word in turkish_words)
    
    return turkish_char_count > 0 or turkish_word_count > 0

def interactive_mode():
    """Run the program in interactive mode"""
    print("🎭 Text2Emotion - Duygu Analizi Aracı")
    print("Türkçe ve İngilizce destekli!")
    print("Çıkmak için 'quit' yazın\n")
    
    # Türkçe analizörü başlat
    turkish_analyzer = TurkishEmotionAnalyzer()
    
    while True:
        text = input("Analiz edilecek metni girin: ")
        
        if text.lower() in ['quit', 'exit', 'çık']:
            print("Program sonlandırılıyor...")
            break
        
        if not text.strip():
            print("Lütfen geçerli bir metin girin!")
            continue
        
        try:
            # Dil tespiti yap
            is_turkish = detect_language(text)
            
            if is_turkish:
                print("🌍 Türkçe metin tespit edildi - Türkçe analizör kullanılıyor...")
                analysis = turkish_analyzer.analyze_with_details(text)
                print_turkish_analysis(analysis)
            else:
                print("🌍 İngilizce metin tespit edildi - İngilizce analizör kullanılıyor...")
                analysis = analyze_emotion_with_details(text)
                print_emotion_analysis(analysis)
                
        except Exception as e:
            print(f"Hata oluştu: {e}")

# Example usage
if __name__ == "__main__":
    # Interactive mode
    interactive_mode()
    
    # Or use with sample text
    # sample_text = "I am very happy today! The weather is great and I'm enjoying my time."
    # analysis = analyze_emotion_with_details(sample_text)
    # print_emotion_analysis(analysis)
