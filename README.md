# 🖼️🔍 AI-Powered OCR: Smart Text Extraction 🚀

A Flask web application that extracts text from images/videos using OCR, enables text refinement through Gemini AI, and maintains contextual chat conversations. 🤖💬

## ✨ Features

- **📸 Image Processing**  
  Upload PNG/JPG/WEBP images (<1MB) for OCR text extraction with direct editing capabilities. ✂️
- **🎥 Video Processing**  
  Upload MP4 videos (<20MB) for frame-by-frame OCR analysis (1 frame/10 processed). 🎞️
- **🧠 AI Interaction**  
  - Context-aware text refinement using Gemini-1.5-flash LLM ✨
  - Persistent chat memory with conversation history 📜
  - Session-based management (30-minute timeout) ⏳
- **⚠️ Error Handling**  
  Detailed error reports with tracebacks and styled error pages 🎨

## ⚙️ Installation

1. Clone repository:
```bash
git clone https://github.com/3liodeh/Smart-OCR.git && cd Smart-OCR
```

2. Create virtual environment:
```bash
python -m venv venv && source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Environment setup:
```bash
touch .env
echo "AI_API_TOKEN=your_gemini_api_key" >> .env
echo "OCR_SPACE_API=your_ocr.space_key" >> .env
```

## 🚀 Usage

1. Start application:
```bash
python app.py
```

2. Access via `http://localhost:10000` 🌍

### 🔄 **Workflow**
- **🖼️ Images**: Upload → Edit OCR text → AI refinement → Chat contextually 💬
- **🎞️ Videos**: Upload → Select frame → Edit text → Continue to chat 📝
- `/chat` maintains conversation history until session expiration ⏳

### ⚠️ **Limitations**
- Max image size: **1MB** (auto-resized) 📏
- Max video size: **20MB** 🎬
- Session timeout: **30 minutes inactivity** ⏰

## 📡 API Requirements

| Service | Key Environment Variable | Documentation |
|---------|--------------------------|---------------|
| Google Gemini 🤖 | `AI_API_TOKEN` | [Gemini API Docs](https://ai.google.dev/) |
| OCR.space 🔍 | `OCR_SPACE_API` | [OCR.space API Docs](https://ocr.space/ocrapi) |

## 📂 Project Structure

```
.
├── app.py               # Flask application core 🏗️
├── LLM.py               # Gemini LLM integration 🤖
├── OCR.py               # Image/Video OCR processing 🖼️
├── run.py               # OCR-LLM bridge 🔗
├── requirements.txt     # Dependency list 📜
└── templates/           # Flask HTML templates 🎨
    ├── index.html
    ├── image.html
    ├── video.html
    └── result.html
```

## 🛠️ Error Handling

Custom error page features:
- 📝 Formatted error tracebacks
- 🧹 Session auto-clear on critical errors
- 🔄 Homepage redirect button
- 🎨 Style-consistent error display

## 📜 License

Open-source under MIT License. Third-party API services may have independent usage policies. 📖

