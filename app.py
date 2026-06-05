from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# ==========================
# Home Route
# ==========================
@app.route('/')
def home():
    return jsonify({
        "message": "AI Research Paper Generator API Running Successfully"
    })


# ==========================
# Generate Research Paper
# ==========================
@app.route('/generate-paper', methods=['POST'])
def generate_paper():

    data = request.json

    topic = data.get('topic')

    if not topic:
        return jsonify({
            "error": "Topic is required"
        }), 400

    paper = {
        "title": topic,

        "abstract":
        f"This research paper investigates {topic} using advanced methodologies and analytical techniques.",

        "introduction":
        f"The field of {topic} has gained significant attention due to rapid technological developments.",

        "literature_review":
        f"Several researchers have contributed towards understanding {topic} and its applications.",

        "methodology":
        "Data collection, preprocessing, machine learning analysis, and evaluation techniques are used.",

        "results":
        "The proposed system demonstrated improved performance and efficiency.",

        "conclusion":
        f"The study confirms the effectiveness of {topic} and highlights future research opportunities."
    }

    return jsonify({
        "status": "success",
        "paper": paper
    })


# ==========================
# Review Research Paper
# ==========================
@app.route('/review-paper', methods=['POST'])
def review_paper():

    data = request.json

    paper_text = data.get('paper')

    if not paper_text:
        return jsonify({
            "error": "Paper content required"
        }), 400

    review_report = {
        "grammar_score": 90,
        "technical_score": 88,
        "readability_score": 85,
        "novelty_score": 82,
        "overall_score": 86,
        "suggestions": [
            "Improve literature review section.",
            "Add more recent references.",
            "Expand methodology explanation."
        ]
    }

    return jsonify({
        "status": "success",
        "review": review_report
    })


# ==========================
# Plagiarism Checker
# ==========================
@app.route('/check-plagiarism', methods=['POST'])
def plagiarism_checker():

    data = request.json

    content = data.get('content')

    if not content:
        return jsonify({
            "error": "Content required"
        }), 400

    plagiarism_score = 12

    return jsonify({
        "status": "success",
        "plagiarism_percentage": plagiarism_score,
        "originality_percentage": 100 - plagiarism_score
    })


# ==========================
# Citation Generator
# ==========================
@app.route('/generate-citation', methods=['POST'])
def citation_generator():

    data = request.json

    title = data.get('title')
    author = data.get('author')
    year = data.get('year')

    citation = f"{author}. \"{title}\" ({year})"

    return jsonify({
        "status": "success",
        "citation": citation
    })


# ==========================
# Dashboard Statistics
# ==========================
@app.route('/dashboard', methods=['GET'])
def dashboard():

    stats = {
        "total_users": 150,
        "papers_generated": 1200,
        "papers_reviewed": 850,
        "average_score": 87,
        "generated_at": datetime.now()
    }

    return jsonify(stats)


# ==========================
# User Registration
# ==========================
@app.route('/register', methods=['POST'])
def register():

    data = request.json

    username = data.get('username')
    email = data.get('email')

    return jsonify({
        "message": "User Registered Successfully",
        "username": username,
        "email": email
    })


# ==========================
# User Login
# ==========================
@app.route('/login', methods=['POST'])
def login():

    data = request.json

    email = data.get('email')
    password = data.get('password')

    return jsonify({
        "message": "Login Successful",
        "email": email
    })


# ==========================
# Run Application
# ==========================
if __name__ == '__main__':
    app.run(debug=True)