# reviewer.py

import random

class PaperReviewer:

    def review_paper(self, paper_text):

        grammar_score = random.randint(80, 95)
        technical_score = random.randint(75, 95)
        readability_score = random.randint(80, 95)
        novelty_score = random.randint(70, 95)

        overall_score = round(
            (
                grammar_score +
                technical_score +
                readability_score +
                novelty_score
            ) / 4,
            2
        )

        feedback = []

        if grammar_score < 85:
            feedback.append(
                "Improve grammar and sentence structure."
            )

        if technical_score < 85:
            feedback.append(
                "Add more technical explanations."
            )

        if readability_score < 85:
            feedback.append(
                "Improve readability and formatting."
            )

        if novelty_score < 85:
            feedback.append(
                "Increase research novelty and contribution."
            )

        return {
            "grammar_score": grammar_score,
            "technical_score": technical_score,
            "readability_score": readability_score,
            "novelty_score": novelty_score,
            "overall_score": overall_score,
            "feedback": feedback
        }