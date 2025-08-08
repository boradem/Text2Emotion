#!/usr/bin/env python3
"""
Text2Emotion Web API Server
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional
import uvicorn
from Text2Emotion import detect_language, analyze_emotion_with_details
from turkish_emotion_analyzer import TurkishEmotionAnalyzer

app = FastAPI(
    title="Text2Emotion API",
    description="Türkçe ve İngilizce duygu analizi API'si",
    version="1.0.0"
)

# Initialize Turkish analyzer
turkish_analyzer = TurkishEmotionAnalyzer()

class TextRequest(BaseModel):
    text: str
    language: Optional[str] = None  # 'tr', 'en', or 'auto'

class EmotionResponse(BaseModel):
    text: str
    detected_language: str
    emotions: Dict[str, float]
    dominant_emotion: str
    dominant_score: float
    processing_time: float

@app.get("/")
async def root():
    """API ana sayfası"""
    return {
        "message": "Text2Emotion API",
        "version": "1.0.0",
        "supported_languages": ["tr", "en", "auto"],
        "endpoints": {
            "/analyze": "POST - Duygu analizi yap",
            "/health": "GET - API durumu kontrol et"
        }
    }

@app.get("/health")
async def health_check():
    """API sağlık kontrolü"""
    return {"status": "healthy", "service": "Text2Emotion API"}

@app.post("/analyze", response_model=EmotionResponse)
async def analyze_emotion(request: TextRequest):
    """Metin duygu analizi"""
    import time
    
    start_time = time.time()
    
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Metin boş olamaz")
    
    # Dil tespiti
    if request.language == "auto" or request.language is None:
        is_turkish = detect_language(request.text)
        detected_lang = "tr" if is_turkish else "en"
    else:
        detected_lang = request.language
        is_turkish = detected_lang == "tr"
    
    try:
        if is_turkish:
            analysis = turkish_analyzer.analyze_with_details(request.text)
            emotions = analysis['emotions']
            dominant_emotion = analysis['dominant_emotion']
            dominant_score = analysis['dominant_score']
        else:
            analysis = analyze_emotion_with_details(request.text)
            emotions = analysis['emotions']
            dominant_emotion = analysis['dominant_emotion']
            dominant_score = analysis['dominant_score']
        
        processing_time = time.time() - start_time
        
        return EmotionResponse(
            text=request.text,
            detected_language=detected_lang,
            emotions=emotions,
            dominant_emotion=dominant_emotion,
            dominant_score=dominant_score,
            processing_time=processing_time
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analiz hatası: {str(e)}")

@app.get("/languages")
async def get_supported_languages():
    """Desteklenen diller"""
    return {
        "supported_languages": [
            {"code": "tr", "name": "Türkçe", "description": "Türkçe duygu analizi"},
            {"code": "en", "name": "İngilizce", "description": "İngilizce duygu analizi"},
            {"code": "auto", "name": "Otomatik", "description": "Otomatik dil tespiti"}
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
