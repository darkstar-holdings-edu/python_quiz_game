from typing import TypedDict
import requests

API_URL = "https://opentdb.com/api.php"
API_QUESTION_TYPE = "boolean"
API_QUESTION_COUNT = 10


class ApiResults(TypedDict):
    category: str
    type: str
    difficulty: str
    question: str
    correct_answer: str
    incorrect_answers: list[str]


class ApiResponse(TypedDict):
    response_code: int
    results: list[ApiResults]
    ...


class OpenTriviaDBApi:
    question_type: str
    question_count: int

    def __init__(self, question_count: int = API_QUESTION_COUNT) -> None:
        self.url = API_URL
        self.question_type = API_QUESTION_TYPE
        self.question_count = question_count
        self.questions: list[dict] = []

    def get_questions(self) -> list[ApiResults]:
        payload: dict[str, str | int] = {
            "amount": self.question_count,
            "type": self.question_type,
        }

        response = requests.get(self.url, params=payload)
        response.raise_for_status()

        json: ApiResponse = response.json()
        return json["results"]
