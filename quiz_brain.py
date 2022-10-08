import html

from open_trivia_db_api import OpenTriviaDBApi
from question_model import Question


class QuizBrain:
    """Handles the Quiz Game logic"""

    def __init__(self, num_questions: int = 10, category_id: int = 9) -> None:
        self.total_questions = num_questions
        self.question_category_id = category_id
        self.question_bank = []
        self.question_index = -1
        self.user_score = 0

        api = OpenTriviaDBApi(category_id=category_id, question_count=num_questions)
        for record in api.get_questions():
            question = Question(
                text=html.unescape(record["question"]),
                correct_answer=html.unescape(record["correct_answer"].lower()),
                incorrect_answers=[
                    html.unescape(a.lower()) for a in record["incorrect_answers"]
                ],
            )

            self.question_bank.append(question)

    def next_question(self) -> None:
        self.question_index += 1
        if self.question_index >= len(self.question_bank):
            raise StopIteration("There are no more questions in the question bank")

        question: Question = self.question_bank[self.question_index]
        response = question.ask(self.question_index + 1)
        if question.check_answer(response):
            self.user_score += 1
            print("That's right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {question.correct_answer}")
        print(f"Your current score is: {self.user_score}/{self.question_index + 1}")
