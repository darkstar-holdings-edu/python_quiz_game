import cooked_input as ci


class Question:
    def __init__(self, **kwargs) -> None:
        """
        text: Question Text
        correct_answer: Answer
        incorrect_answers: Invalid Answers
        """
        # self.__dict__.update(kwargs)
        self.text = kwargs["text"]
        self.correct_answer = kwargs["correct_answer"]
        self.incorrect_answers = kwargs["incorrect_answers"]

    def responses(self) -> list[str]:
        values = self.incorrect_answers
        values.append(self.correct_answer)

        return sorted(values)

    def ask(self, question_number) -> str:
        valid_responses = self.responses()
        answer_cleaner = ci.ChoiceCleaner(valid_responses)
        answer_validator = ci.ChoiceValidator(valid_responses)

        options = ", ".join(opt.capitalize() for opt in valid_responses)
        prompt = f"Q.{question_number} {self.text} [{options}]"
        response = ci.get_input(
            prompt=prompt,
            cleaners=[
                ci.StripCleaner(),
                ci.CapitalizationCleaner("lower"),
                answer_cleaner,
            ],
            validators=answer_validator,
        )

        return response

    def check_answer(self, response: str) -> bool:
        return response == self.correct_answer.lower()
