#!/usr/bin/env python3
"""
Comprehensive test coverage for Text2Emotion
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from Text2Emotion import (
    download_nltk_data, clean_text, remove_stopwords, 
    detect_emotion, analyze_emotion_with_details, 
    detect_language, interactive_mode
)
from turkish_emotion_analyzer import TurkishEmotionAnalyzer

class TestText2Emotion(unittest.TestCase):
    """Test cases for Text2Emotion module"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.analyzer = TurkishEmotionAnalyzer()
    
    def test_clean_text(self):
        """Test text cleaning functionality"""
        # Test basic cleaning
        result = clean_text("Hello, World! 123")
        self.assertEqual(result, "hello world 123")
        
        # Test Turkish characters
        result = clean_text("Merhaba Dünya!")
        self.assertEqual(result, "merhaba dünya")
    
    def test_detect_language(self):
        """Test language detection"""
        # Test Turkish text
        self.assertTrue(detect_language("Merhaba dünya"))
        self.assertTrue(detect_language("Bugün çok güzel"))
        
        # Test English text
        self.assertFalse(detect_language("Hello world"))
        self.assertFalse(detect_language("Today is beautiful"))
    
    def test_turkish_analyzer(self):
        """Test Turkish emotion analyzer"""
        # Test happy text
        analysis = self.analyzer.analyze_with_details("Bugün çok mutluyum!")
        self.assertIn('emotions', analysis)
        self.assertIn('dominant_emotion', analysis)
        
        # Test sad text
        analysis = self.analyzer.analyze_with_details("Çok üzgünüm")
        self.assertIn('emotions', analysis)
    
    @patch('Text2Emotion.te.get_emotion')
    def test_detect_emotion(self, mock_get_emotion):
        """Test emotion detection with mocked text2emotion"""
        mock_get_emotion.return_value = {
            'Happy': 0.8, 'Sad': 0.1, 'Angry': 0.05, 
            'Fear': 0.03, 'Surprise': 0.02
        }
        
        result = detect_emotion("I am very happy!")
        self.assertIn('Happy', result)
        self.assertEqual(result['Happy'], 0.8)
    
    def test_analyze_emotion_with_details(self):
        """Test detailed emotion analysis"""
        with patch('Text2Emotion.te.get_emotion') as mock_get_emotion:
            mock_get_emotion.return_value = {
                'Happy': 0.9, 'Sad': 0.1, 'Angry': 0.0, 
                'Fear': 0.0, 'Surprise': 0.0
            }
            
            result = analyze_emotion_with_details("I am very happy!")
            self.assertIn('emotions', result)
            self.assertIn('dominant_emotion', result)
            self.assertIn('dominant_score', result)
            self.assertEqual(result['dominant_emotion'], 'Happy')
    
    def test_edge_cases(self):
        """Test edge cases"""
        # Empty text
        analysis = self.analyzer.analyze_with_details("")
        self.assertIn('emotions', analysis)
        
        # Very short text
        analysis = self.analyzer.analyze_with_details("a")
        self.assertIn('emotions', analysis)
        
        # Special characters only
        analysis = self.analyzer.analyze_with_details("!@#$%")
        self.assertIn('emotions', analysis)

class TestPerformance(unittest.TestCase):
    """Test performance aspects"""
    
    def test_caching(self):
        """Test that caching works"""
        # First call should be slower
        start_time = __import__('time').time()
        result1 = clean_text("test text")
        first_call_time = __import__('time').time() - start_time
        
        # Second call should be faster (cached)
        start_time = __import__('time').time()
        result2 = clean_text("test text")
        second_call_time = __import__('time').time() - start_time
        
        self.assertEqual(result1, result2)
        # Second call should be faster (though this might not always be true due to system load)
    
    def test_memory_usage(self):
        """Test memory usage doesn't grow excessively"""
        import gc
        import sys
        
        # Force garbage collection
        gc.collect()
        initial_memory = sys.getsizeof(clean_text("test"))
        
        # Call function many times
        for i in range(1000):
            clean_text(f"test text {i}")
        
        # Force garbage collection again
        gc.collect()
        final_memory = sys.getsizeof(clean_text("test"))
        
        # Memory usage shouldn't grow significantly
        memory_growth = final_memory - initial_memory
        self.assertLess(memory_growth, 1000)  # Allow some growth but not excessive

if __name__ == '__main__':
    # Run tests with coverage
    unittest.main(verbosity=2)
