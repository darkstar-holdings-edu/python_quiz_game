class Question:
    text: str
    correct_answer: str
    incorrect_answers: list[str]

    def __init__(
        self,
        text: str,
        correct_answer: str,
        incorrect_answers: list[str],
    ) -> None:
        self.text = text
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
