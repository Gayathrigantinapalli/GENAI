from flask import Flask, request, jsonify, render_template
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import numpy as np


app = Flask(__name__)


# ============================================================
# 1. LOAD MODELS
# ============================================================

print("Loading embedding model...")

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Loading local LLM...")

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

print("Models loaded successfully.")


# ============================================================
# 2. EXTRACT TEXT FROM PDF
# ============================================================

def extract_text(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# ============================================================
# 3. CREATE CHUNKS
# ============================================================

def create_chunks(pdf_file):

    print(f"Processing: {pdf_file}")

    text = extract_text(pdf_file)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)

    results = []

    for i, chunk in enumerate(chunks, start=1):

        results.append({
            "file_name": pdf_file,
            "chunk_name": f"chunk_{i}",
            "chunk_number": i,
            "text": chunk
        })

    return results


# ============================================================
# 4. LOAD PDF FILES
# ============================================================

pdf_files = [
    "xyz.pdf",
    "abc.pdf"
]


all_chunks = []


for pdf in pdf_files:

    chunks = create_chunks(pdf)

    all_chunks.extend(chunks)


print("\nTotal chunks:", len(all_chunks))


# ============================================================
# 5. CREATE EMBEDDINGS FOR ALL CHUNKS
# ============================================================

print("\nCreating embeddings...")


texts = [
    item["text"]
    for item in all_chunks
]


embeddings = embedding_model.encode(
    texts,
    convert_to_numpy=True
)


for i, item in enumerate(all_chunks):

    item["embedding"] = embeddings[i]


print("Embeddings created successfully.")


# ============================================================
# 6. COSINE SIMILARITY
# ============================================================

def cosine_similarity(a, b):

    dot_product = np.dot(a, b)

    magnitude_a = np.linalg.norm(a)

    magnitude_b = np.linalg.norm(b)

    if magnitude_a == 0 or magnitude_b == 0:
        return 0

    return dot_product / (
        magnitude_a * magnitude_b
    )


# ============================================================
# 7. SEARCH BEST CHUNK
# ============================================================

def search_documents(question):

    # Create embedding for user question

    question_embedding = embedding_model.encode(
        question,
        convert_to_numpy=True
    )


    results = []


    for item in all_chunks:

        score = cosine_similarity(
            question_embedding,
            item["embedding"]
        )


        results.append({
            "file_name": item["file_name"],
            "chunk_name": item["chunk_name"],
            "chunk_number": item["chunk_number"],
            "text": item["text"],
            "score": float(score)
        })


    # Highest similarity first

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )


    return results


# ============================================================
# 8. GENERATE ANSWER USING LOCAL LLM
# ============================================================

def generate_answer(question, context):

    prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}

Answer:
"""


    result = generator(
        prompt,
        max_new_tokens=100,
        num_return_sequences=1,
        do_sample=False
    )


    generated_text = result[0]["generated_text"]


    # Remove prompt from response

    if "Answer:" in generated_text:

        answer = generated_text.split(
            "Answer:"
        )[-1].strip()

    else:

        answer = generated_text


    return answer


# ============================================================
# 9. HOME PAGE
# ============================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ============================================================
# 10. ASK API
# ============================================================

@app.route("/ask", methods=["POST"])
def ask():

    try:

        data = request.get_json()

        question = data.get(
            "question",
            ""
        ).strip()


        if not question:

            return jsonify({
                "error": "Question is required"
            }), 400


        # Search documents

        results = search_documents(
            question
        )


        # Best result

        best_result = results[0]


        score = best_result["score"]


        # ----------------------------------------------------
        # Threshold
        # ----------------------------------------------------

        if score < 0.4:

            return jsonify({

                "question": question,

                "message":
                    "No relevant document found",

                "best_score": round(
                    score,
                    4
                )

            })


        # ----------------------------------------------------
        # Context
        # ----------------------------------------------------

        context = best_result["text"]


        # ----------------------------------------------------
        # Generate answer
        # ----------------------------------------------------

        answer = generate_answer(
            question,
            context
        )


        # ----------------------------------------------------
        # Response
        # ----------------------------------------------------

        return jsonify({

            "question": question,

            "answer": answer,

            "file_name":
                best_result["file_name"],

            "chunk_name":
                best_result["chunk_name"],

            "chunk_number":
                best_result["chunk_number"],

            "similarity_score":
                round(score, 4),

            "context":
                best_result["text"]

        })


    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ============================================================
# 11. RUN FLASK
# ============================================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )