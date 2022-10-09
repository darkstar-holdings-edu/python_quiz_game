from tkinter import Label

from gui_theme import THEME_COLOR, THEME_FONT_FACE


class GuiScoreBoard(Label):
    total_questions: int

    def __init__(self, total_questions: int) -> None:
        super().__init__()

        self.total_questions = total_questions
        self.config(
            foreground="white",
            background=THEME_COLOR,
            font=(THEME_FONT_FACE, 16, "normal"),
        )

        self.write()

    def write(self, score: int = 0) -> None:
        self.config(text=f"Score: {score}/{self.total_questions}")
