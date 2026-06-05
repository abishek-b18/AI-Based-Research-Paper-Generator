# paper_generator.py

from datetime import datetime

class ResearchPaperGenerator:

    def generate_paper(self, topic):

        paper = {
            "title": topic,

            "abstract":
            f"""
            This research explores {topic} using modern Artificial
            Intelligence and Machine Learning techniques.
            The study focuses on improving efficiency,
            accuracy, and scalability.
            """,

            "introduction":
            f"""
            The field of {topic} has experienced rapid growth in recent years.
            Researchers are continuously developing innovative methods
            to solve real-world challenges.
            """,

            "literature_review":
            f"""
            Previous studies indicate significant improvements
            in performance when AI-based solutions are applied
            to {topic}. Various algorithms and frameworks
            have been proposed.
            """,

            "methodology":
            """
            Data Collection
            Data Preprocessing
            Feature Engineering
            Model Development
            Evaluation Metrics
            Result Analysis
            """,

            "results":
            """
            Experimental results demonstrate improved performance
            compared with traditional approaches.
            Accuracy, precision, recall, and F1 score
            were used for evaluation.
            """,

            "conclusion":
            f"""
            The proposed research confirms that {topic}
            can benefit significantly from AI-driven solutions.
            Future work can explore deeper optimization methods.
            """,

            "generated_date":
            str(datetime.now())
        }

        return paper