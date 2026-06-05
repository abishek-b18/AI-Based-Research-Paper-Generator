from database import db
from datetime import datetime

# ==========================
# User Table
# ==========================
class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }


# ==========================
# Research Paper Table
# ==========================
class ResearchPaper(db.Model):

    __tablename__ = "research_papers"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id')
    )

    title = db.Column(
        db.String(300),
        nullable=False
    )

    abstract = db.Column(db.Text)

    introduction = db.Column(db.Text)

    literature_review = db.Column(db.Text)

    methodology = db.Column(db.Text)

    results = db.Column(db.Text)

    conclusion = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "abstract": self.abstract,
            "introduction": self.introduction,
            "literature_review": self.literature_review,
            "methodology": self.methodology,
            "results": self.results,
            "conclusion": self.conclusion
        }


# ==========================
# Review Table
# ==========================
class Review(db.Model):

    __tablename__ = "reviews"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    paper_id = db.Column(
        db.Integer,
        db.ForeignKey('research_papers.id')
    )

    grammar_score = db.Column(db.Float)

    technical_score = db.Column(db.Float)

    readability_score = db.Column(db.Float)

    novelty_score = db.Column(db.Float)

    overall_score = db.Column(db.Float)

    feedback = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "grammar_score": self.grammar_score,
            "technical_score": self.technical_score,
            "readability_score": self.readability_score,
            "novelty_score": self.novelty_score,
            "overall_score": self.overall_score,
            "feedback": self.feedback
        }


# ==========================
# Citation Table
# ==========================
class Citation(db.Model):

    __tablename__ = "citations"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    paper_id = db.Column(
        db.Integer,
        db.ForeignKey('research_papers.id')
    )

    citation_style = db.Column(
        db.String(50)
    )

    citation_text = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# ==========================
# Plagiarism Table
# ==========================
class PlagiarismReport(db.Model):

    __tablename__ = "plagiarism_reports"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    paper_id = db.Column(
        db.Integer,
        db.ForeignKey('research_papers.id')
    )

    plagiarism_percentage = db.Column(
        db.Float
    )

    originality_percentage = db.Column(
        db.Float
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )