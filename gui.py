from tkinter import Tk

from gui_theme import THEME_COLOR
from gui_components import GuiButton, GuiQuestionBox, GuiScoreBoard
from quiz_brain import QuizBrain


class GUI:
    brain: QuizBrain

    window: Tk
    score_box: GuiScoreBoard
    question_box: GuiQuestionBox
    btn_true: GuiButton
    btn_false: GuiButton

    def __init__(self) -> None:
        self.brain = QuizBrain()

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(
            padx=20,
            pady=20,
            background=THEME_COLOR,
        )

        self.score_box = GuiScoreBoard(total_questions=self.brain.total_questions())
        self.score_box.grid(row=0, column=1)

        self.question_box = GuiQuestionBox(height=250, width=300)
        self.question_box.grid(row=1, column=0, columnspan=2, pady=50)

        self.btn_true = GuiButton(
            image_filename="assets/true.png",
            handler=self.btn_true_handler,
        )
        self.btn_true.grid(row=2, column=0)

        self.btn_false = GuiButton(
            image_filename="assets/false.png",
            handler=self.btn_false_handler,
        )
        self.btn_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self) -> None:
        self.question_box.update_background("white")
        if self.brain.has_more_questions():
            self.question_box.update_text(self.brain.next_question())
        else:
            self.question_box.update_text("Game Over!")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def check_answer(self, response) -> None:
        if self.brain.check_answer(response):
            self.score_box.write(self.brain.user_score)
            self.question_box.update_background("green")

        else:
            self.question_box.update_background("red")

        self.window.after(1000, self.get_next_question)

    def btn_true_handler(self) -> None:
        self.check_answer("true")

    def btn_false_handler(self) -> None:
        self.check_answer("false")
