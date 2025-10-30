# app.py
import os
import tempfile
import streamlit as st
from dotenv import load_dotenv

# Import your local modules
from extract_data import extract_text
from database_manager import init_db, add_document
from query_engine import answer_query_with_gemini

# Load environment
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

# Initialize database
init_db()

# Streamlit page setup
st.set_page_config(
    page_title="Multimodal Data Processing using Gemini",
    page_icon="🧠",
    layout="wide",
)

st.title("🧠 Multimodal Data Processing using Gemini (Grow with Guntur – Batch 3)")
st.markdown(
    """
    This app extracts information from **PDF, DOCX, PPTX, TXT, images, audio, video, and YouTube links**,  
    stores it in a **SQLite knowledge base**, and answers your natural-language queries using **Google Gemini**.
    ---
    """
)

# --- Tabs for better UX ---
tab1, tab2 = st.tabs(["📥 Upload & Process Files", "💬 Ask Questions"])

# =====================================================
# 📥 TAB 1: Upload & Process Files
# =====================================================
with tab1:
    st.header("Upload or link your data files")

    uploaded_files = st.file_uploader(
        "Upload files (PDF, DOCX, PPTX, TXT, MD, PNG, JPG, MP3, MP4, etc.)",
        type=[
            "pdf", "docx", "pptx", "txt", "md",
            "png", "jpg", "jpeg",
            "mp3", "wav", "mp4", "mov", "avi", "mkv"
        ],
        accept_multiple_files=True,
    )

    youtube_url = st.text_input("Or enter a YouTube URL:")

    if st.button("📄 Process and Add to Knowledge Base"):
        if not uploaded_files and not youtube_url:
            st.warning("Please upload at least one file or provide a YouTube link.")
        else:
            with st.spinner("Processing files..."):
                init_db()
                added_files = []
                failed_files = []

                # Handle uploaded files
                for file in uploaded_files:
                    try:
                        suffix = os.path.splitext(file.name)[1].lower()
                        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                            tmp.write(file.read())
                            tmp_path = tmp.name

                        text = extract_text(tmp_path)
                        add_document(file.name, text)
                        added_files.append(file.name)
                    except Exception as e:
                        failed_files.append((file.name, str(e)))

                # Handle YouTube link
                if youtube_url.strip():
                    try:
                        text = extract_text(youtube_url.strip())
                        add_document(youtube_url.strip(), text)
                        added_files.append(youtube_url)
                    except Exception as e:
                        failed_files.append((youtube_url, str(e)))

            # Display results
            if added_files:
                st.success(f"✅ Successfully added {len(added_files)} file(s):")
                for f in added_files:
                    st.write(f"- {f}")

            if failed_files:
                st.error(f"⚠️ Some files failed to process:")
                for name, err in failed_files:
                    st.write(f"- {name}: {err}")

# =====================================================
# 💬 TAB 2: Ask Questions
# =====================================================
with tab2:
    st.header("Ask a Question about Your Uploaded Data")

    query = st.text_area("Enter your question:", placeholder="e.g. Summarize the key points about forests.")
    if st.button("🔍 Get Answer"):
        if not query.strip():
            st.warning("Please enter a question first.")
        else:
            with st.spinner("Thinking..."):
                answer = answer_query_with_gemini(query)

            st.subheader("🤖 Gemini’s Answer")
            st.write(answer)

    st.markdown("---")
    st.caption("Powered by Google Gemini • Developed by Sukanya Das • Grow with Guntur – Batch 3")
