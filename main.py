from gui import GUI

# from quiz_brain import QuizBrain

from utils import clear_console


def main():
    GUI()

    # quiz_brain = QuizBrain()

    # game_running = True
    # while game_running:
    #     try:
    #         quiz_brain.next_question()
    #     except StopIteration:
    #         break

    # print("-" * 40)
    # print("You've completed the quiz.")
    # print(f"Your final score: {quiz_brain.user_score}/{quiz_brain.question_index}")


if __name__ == "__main__":
    clear_console()
    main()
