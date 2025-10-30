
# 🌟 Multimodal Data Processing using GenAI

### 🚀 Grow with Guntur – Batch 3 | Internship Assessment Project  
**Organization:** Coastal Seven Consulting  
**Project Title:** *Multimodal Data Processing System*  
**Objective:** Build a system capable of processing multimodal input files and responding to natural language queries using Gemini LLM.

---

## 🧠 Overview

This project is an intelligent **Multimodal Data Processing System** that:
- Extracts and processes data from **multiple file types** (text, documents, images, audio, video, and YouTube URLs)
- Stores processed text in a **SQLite database**
- Lets users ask **natural lang
uage queries**
- Responds intelligently using **Google Gemini (Free Version)**

The system integrates OCR, NLP, speech recognition, and AI-based query answering — all inside a clean Streamlit web app.

---

## ⚙️ Features

✅ **Multimodal Data Extraction**
- 📄 PDF, DOCX, TXT, MD  
- 🖼️ PNG, JPG, JPEG (OCR via Tesseract)  
- 🎧 MP3 / 🎥 MP4 / YouTube videos (Audio transcription)

✅ **AI-Powered Query Response**
- Queries answered using **Gemini 2.5 Flash** model  
- Context retrieved from processed knowledge base  

✅ **Database Storage**
- Uses **SQLite** to store and search extracted data efficiently  

✅ **Streamlit Web Interface**
- Upload files  
- Extract and store automatically  
- Ask natural questions and get AI answers  

---

## 🗂️ Repository Structure

```

Multimodal-Data-Processing-using-GenAI/
│
├── src/
│   ├── app.py                 # Streamlit app interface
│   ├── extract_data.py        # Handles file reading & data extraction
│   ├── database_manager.py    # SQLite database operations
│   ├── query_engine.py        # AI-powered search and Gemini interaction
│   ├── **init**.py
│
├── data/                      # Sample data files (PDFs, images, etc.)
│
├── .env                       # Stores Google API Key (not shared)
├── .gitignore                 # Ignores temp, env, and cache files
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── Assignment.ipynb           # Jupyter notebook (for testing)

````

---

## 🧩 Technologies Used

| Category | Tools / Libraries |
|-----------|------------------|
| **Language** | Python 3.x |
| **Frontend** | Streamlit |
| **Database** | SQLite3 |
| **AI/LLM** | Google Gemini 2.5 Flash |
| **Document Processing** | PyPDF2, python-docx, python-pptx |
| **Image Processing** | Pillow, pytesseract |
| **Audio/Video** | pydub, ffmpeg, SpeechRecognition, yt-dlp |
| **Environment Management** | python-dotenv |

---

## 🧱 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Multimodal-Data-Processing-using-GenAI.git
cd Multimodal-Data-Processing-using-GenAI
````

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate       # On Windows
# OR
source venv/bin/activate    # On Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup `.env` File

Create a `.env` file in your root folder and add:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

> 🔑 You can get a free Gemini API key from [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

### 5️⃣ Run the Streamlit App

```bash
streamlit run src/app.py
```

---

## 🧮 Supported File Formats

| Type        | Supported Formats                       |
| ----------- | --------------------------------------- |
| Text        | `.pdf`, `.docx`, `.pptx`, `.md`, `.txt` |
| Image       | `.png`, `.jpg`, `.jpeg`                 |
| Audio/Video | `.mp3`, `.mp4`, `.avi`, `.mov`, `.mkv`  |
| YouTube     | `https://youtu.be/...`                  |

---

## 💬 Example Usage

1. Upload your files (PDF, image, MP3, etc.)
2. Wait while the app extracts and stores the data
3. Ask a question like:

   ```
   Summarize the key points about forests.
   ```
4. Get an instant AI-generated response from Gemini.

---

## 🗄️ Database Schema

| Column Name    | Type      | Description                |
| -------------- | --------- | -------------------------- |
| id             | INTEGER   | Auto-increment primary key |
| file_name      | TEXT      | Original file name or URL  |
| extracted_text | TEXT      | Cleaned extracted text     |
| created_at     | TIMESTAMP | Date of insertion          |

---

## 🧪 Sample Data Files

Make sure to place your example files in:

```
data/
 ├── GenAI.pdf
 ├── Forest.docx
 ├── Music.txt
 ├── quote.png
 ├── VandeMataram.mp3
 ├── SnowGeese.mp4
```

---

## 💡 Future Improvements

* Integrate **Vector Search / Embeddings** for semantic retrieval
* Add **audio output (text-to-speech)** for responses
* Deploy the app on **Streamlit Cloud** or **Hugging Face Spaces**

---

## 🧑‍💻 Author

**👩‍💻 Sukanya Das**
* 💼 Internship Candidate — Coastal Seven Consulting
* 📧 sukanyadas1211@gmail.com
* 🔗 https://www.linkedin.com/in/sukanya-das-a05935244/

---

## 🏁 Acknowledgments

* **Google DeepMind** – for the Gemini API
* **Streamlit** – for simple web app deployment
* **Coastal Seven Consulting** – for the opportunity and guidance

---

### 🌈 *“Integrating knowledge across formats — making AI truly multimodal.”*

```
