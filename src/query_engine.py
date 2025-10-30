import os
from dotenv import load_dotenv
import google.generativeai as genai
from database_manager import search_documents, get_all_text

# ----------------------------------------------------------
# 🔑 Load Gemini API key
# ----------------------------------------------------------
load_dotenv()  # Load from .env file if available
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# ----------------------------------------------------------
# ⚙️ Configure Gemini (use a supported model)
# ----------------------------------------------------------
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")  # You can switch to gemini-pro if preferred


# ----------------------------------------------------------
# 🧠 Build context from your local database
# ----------------------------------------------------------
def build_context_from_query(query: str, max_chars: int = 3000) -> str:
    """
    Retrieves relevant text snippets from the local knowledge base (SQLite DB)
    matching the user's query.
    """
    results = search_documents(query, limit=5)
    if results:
        context_parts = []
        print("\n🧠 Matched documents:")
        for name, content in results:
            snippet = content[:300].replace("\n", " ")
            print(f"   📄 {name}: {snippet}...")
            context_parts.append(f"From {name}:\n{content}\n")
        return "\n".join(context_parts)[:max_chars]
    else:
        print("\n⚠️ No exact FTS match found. Using all available data as fallback.")
        return get_all_text()[:max_chars]


# ----------------------------------------------------------
# 💬 Generate answer using Gemini
# ----------------------------------------------------------
def answer_query_with_gemini(query: str) -> str:
    """
    Generates a natural language response from Gemini
    based on extracted knowledge base context.
    """
    context = build_context_from_query(query)

    if not context.strip():
        return "No relevant information found in the knowledge base."

    print("\n📚 Sending context to Gemini...")
    print(context[:500], "...\n")

    prompt = f"""
You are a smart AI assistant. Answer the user's query using only the context below.
If context doesn’t contain relevant information, say so clearly.

Context:
{context}

User Query:
{query}

Answer:
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Gemini API Error: {str(e)}"


# ----------------------------------------------------------
# 🧪 Test block (only runs if executed directly)
# ----------------------------------------------------------
if __name__ == "__main__":
    test_query = "Summarize the key points about forests."
    print("Question:", test_query)
    answer = answer_query_with_gemini(test_query)
    print("\n💬 Gemini's Answer:\n", answer)
