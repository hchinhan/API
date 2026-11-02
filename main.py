import re
import torch
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from omegaconf import OmegaConf
from pydantic import BaseModel, Field
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


class MachineTranslation:
    def __init__(self, config_path):
        self.config = OmegaConf.load(config_path)
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.model_path)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path)

    def __call__(self, text: str) -> str:
        inputs = self.tokenizer(text, return_tensors="pt", padding=True)
        with torch.no_grad():
            translated_tokens = self.model.generate(**inputs)

        return self.tokenizer.decode(translated_tokens[0], skip_special_tokens=True)


translator = MachineTranslation("./config.yaml")


app = FastAPI(
    title="Anime Engsub Translation API",
    description="API for translating Anime dialogue from Japanese to English",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TranslationRequest(BaseModel):
    text: str = Field(..., description="Japanese dialogue text to translate", example="海賊王に俺はなる！")


@app.get("/")
def root():
    return {
        "message": "Welcome to the Japanese-to-English Anime Translation API!",
        "model_used": translator.config.model_path,
        "source_lang": "Japanese (ja)",
        "target_lang": "English (en)",
        "docs_url": "/docs",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": True,
    }


@app.post("/predict")
def translate_text(payload: TranslationRequest):
    cleaned_text = payload.text.strip()

    if not cleaned_text:
        raise HTTPException(
            status_code=400,
            detail="Error: Input Japanese text cannot be empty!",
        )

    if not re.search(r"[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]", cleaned_text):
        raise HTTPException(
            status_code=400,
            detail="Error: Input must contain valid Japanese characters (Hiragana, Katakana, or Kanji)!",
        )

    try:
        translated_result = translator(cleaned_text)

        return {
            "status": "success",
            "japanese_input": payload.text,
            "english_translation": translated_result,
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Translation error: {str(e)}",
        )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
