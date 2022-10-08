import requests

API_URL = "https://opentdb.com/api.php"
API_CATEGORY = 9
API_QUESTION_TYPE = "boolean"
API_QUESTION_COUNT = 10


class OpenTriviaDBApi:
    """Handles API Calls to the Open Trivial Database."""

    def __init__(
        self,
        category_id: int = API_CATEGORY,
        question_count: int = API_QUESTION_COUNT,
    ) -> None:
        self.url = API_URL
        self.category_id = category_id
        self.question_type = API_QUESTION_TYPE
        self.question_count = question_count
        self.questions: list[dict] = []

    def get_questions(self) -> list[dict]:
        """Retrieves a list of questions"""
        payload: dict[str, str | int] = {
            "category": self.category_id,
            "amount": self.question_count,
            "type": self.question_type,
        }

        response = requests.get(self.url, params=payload)
        response.raise_for_status()

        json = response.json()
        return json["results"]
