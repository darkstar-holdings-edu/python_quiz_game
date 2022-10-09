import html

from api import OpenTriviaDBApi
from question_model import Question


class QuizBrain:
    question_bank: list[Question]
    question_index: int
    user_score: int

    def __init__(self, num_questions: int = 10, category_id: int = 9) -> None:
        self.question_bank = []
        self.question_index = -1
        self.user_score = 0
        self.current_question: Question

        api = OpenTriviaDBApi(question_count=num_questions)
        for record in api.get_questions():
            question = Question(
                text=html.unescape(record["question"]),
                correct_answer=html.unescape(record["correct_answer"].lower()),
                incorrect_answers=[
                    html.unescape(a.lower()) for a in record["incorrect_answers"]
                ],
            )

            self.question_bank.append(question)

    def total_questions(self) -> int:
        return len(self.question_bank)

    def has_more_questions(self) -> bool:
        return self.question_index < len(self.question_bank) - 1

    def next_question(self) -> str:
        self.question_index += 1
        if self.question_index >= len(self.question_bank):
            raise StopIteration("There are no more questions in the question bank")

        return (
            f"Q{self.question_index + 1}. "
            f"{self.question_bank[self.question_index].text}"
        )

    def check_answer(self, response: str) -> bool:
        if response == self.question_bank[self.question_index].correct_answer.lower():
            self.user_score += 1
            return True

        return False
