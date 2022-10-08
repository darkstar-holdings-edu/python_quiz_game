from tkinter import Button, Canvas, Label, PhotoImage, Tk
from typing import Callable

THEME_COLOR = "#375362"
THEME_FONT_FACE = "Arial"


class GuiQuestionBox:
    canvas: Canvas
    text_id: int

    def __init__(
        self,
        height: int,
        width: int,
    ) -> None:

        canvas = Canvas(
            height=height,
            width=width,
            background="white",
            borderwidth=0,
            highlightthickness=0,
        )

        self.text_id = canvas.create_text(
            150,
            125,
            text="Default text.",
            fill=THEME_COLOR,
            font=(THEME_FONT_FACE, 20, "italic"),
            width=width,
        )

        self.canvas = canvas

    def grid(self, row: int, column: int, columnspan: int, pady: int) -> None:
        self.canvas.grid(row=row, column=column, columnspan=columnspan, pady=pady)

    def update(self, text: str) -> None:
        self.canvas.itemconfig(self.text_id, text=text)


class GuiScoreBox(Label):
    score: int = 0

    def __init__(self) -> None:
        super().__init__()

        self.config(
            foreground="white",
            background=THEME_COLOR,
            font=(THEME_FONT_FACE, 16, "normal"),
        )

        self.write()

    def write(self) -> None:
        self.config(text=f"Score: {self.score}")

    def increment(self) -> None:
        self.score += 1
        self.write()


class GuiButton(Button):
    image: PhotoImage

    def __init__(
        self,
        image_filename: str,
        handler: Callable[[], None],
    ) -> None:
        super().__init__()

        self.image = PhotoImage(file=image_filename)
        self.config(
            image=self.image,
            command=handler,
            borderwidth=0,
            highlightthickness=0,
        )


class GUI:
    window: Tk
    score_box: GuiScoreBox
    question_box: GuiQuestionBox
    btn_true: GuiButton
    btn_false: GuiButton

    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(
            padx=20,
            pady=20,
            background=THEME_COLOR,
        )

        self.score_box = GuiScoreBox()
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

        self.window.mainloop()

    def btn_true_handler(self):
        print("True")
        self.score_box.increment()

    def btn_false_handler(self):
        print("False")
