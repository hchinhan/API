# Japanese-to-English Translation API

This project is a Web API built with **FastAPI** that deploys a machine translation model from Hugging Face to translate Japanese text (such as anime dialogue) into English.

---

## 1. Student Information

- **Full Name:** Huỳnh Chí Nhân
- **Student ID:** 25127440

---

## 2. Selected Model

- **Model Name:** `Helsinki-NLP/opus-mt-ja-en`
- **Task:** Machine Translation (Japanese $\rightarrow$ English)
- **Hugging Face Link:** [https://huggingface.co/Helsinki-NLP/opus-mt-ja-en](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en)

---

## 3. System Description

This system is designed to translate Japanese sentences and conversations into English automatically. It uses the `Helsinki-NLP/opus-mt-ja-en` neural machine translation model, making it very useful for practical situations such as translating anime subtitles, reading raw manga or light novels, understanding Japanese games, or supporting Japanese language learners in looking up daily expressions.

On the technical side, the system provides a RESTful API using **FastAPI** and **Hugging Face Transformers** (`AutoTokenizer` and `AutoModelForSeq2SeqLM`). The model path is configured in `config.yaml` and loaded with `OmegaConf`.

Main features of the API:
- **`GET /`**: Returns basic information about the API and the translation model being used.
- **`GET /health`**: Checks whether the server is running and the model is loaded properly.
- **`POST /predict`**: Receives a Japanese text string in JSON format, translates it into English using the Hugging Face model, and returns the result in JSON format.
- **Input Validation & Error Handling**: Validates incoming JSON data with Pydantic, returns HTTP `400` if the input text is empty or contains only whitespace, and handles runtime inference errors with HTTP `500`.

---

## 4. Installation Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hchinhan/API.git
   cd API
   ```

2. **Create and activate a virtual environment:**
   - On Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - On macOS / Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 5. Running the Application

Start the FastAPI server using Python or Uvicorn:

```bash
python main.py
```

Or:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Once the server starts, it will be available at:
- **API Base URL:** `http://127.0.0.1:8000`
- **Interactive Swagger UI Docs:** `http://127.0.0.1:8000/docs`

*(Note: On the first run, the system will automatically download the `Helsinki-NLP/opus-mt-ja-en` model weights from Hugging Face).*

---

## 6. Calling the API (Examples)

You can test all endpoints automatically by opening a second terminal and running the test script:

```bash
python test_api.py
```

### Endpoint 1: `GET /` (API Introduction)

- **Request:**
  ```http
  GET http://127.0.0.1:8000/
  ```
- **Example Response (`200 OK`):**
  ```json
  {
    "message": "Welcome to the Japanese-to-English Anime Translation API!",
    "model_used": "Helsinki-NLP/opus-mt-ja-en",
    "source_lang": "Japanese (ja)",
    "target_lang": "English (en)",
    "docs_url": "/docs"
  }
  ```

### Endpoint 2: `GET /health` (Health Check)

- **Request:**
  ```http
  GET http://127.0.0.1:8000/health
  ```
- **Example Response (`200 OK`):**
  ```json
  {
    "status": "healthy",
    "model_loaded": true
  }
  ```

### Endpoint 3: `POST /predict` (Translate Text)

- **Request:**
  ```http
  POST http://127.0.0.1:8000/predict
  Content-Type: application/json

  {
    "text": "海賊王に俺はなる！"
  }
  ```
- **Example Response (`200 OK`):**
  ```json
  {
    "status": "success",
    "japanese_input": "海賊王に俺はなる！",
    "english_translation": "I'm going to be the Pirate King!"
  }
  ```

- **Example Error Response (Empty Input - `400 Bad Request`):**
  - Request Body:
    ```json
    {
      "text": "   "
    }
    ```
  - Response:
    ```json
    {
      "detail": "Error: Input Japanese text cannot be empty!"
    }
    ```

---

## 7. Demonstration Video

- **Video Link:** 

Youtube: https://youtu.be/DULtzvY0ft8

GG Drive: https://drive.google.com/drive/folders/1R74UhoUQu31pUKKLMZGZdJsLkQ7JRqOA?usp=drive_link

