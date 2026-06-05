# plagiarism_checker.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class PlagiarismChecker:

    def check_similarity(self, text1, text2):

        documents = [text1, text2]

        vectorizer = TfidfVectorizer()

        tfidf_matrix = vectorizer.fit_transform(
            documents
        )

        similarity = cosine_similarity(
            tfidf_matrix[0:1],
            tfidf_matrix[1:2]
        )[0][0]

        plagiarism_percentage = round(
            similarity * 100,
            2
        )

        originality_percentage = round(
            100 - plagiarism_percentage,
            2
        )

        return {
            "plagiarism_percentage":
            plagiarism_percentage,

            "originality_percentage":
            originality_percentage
        }