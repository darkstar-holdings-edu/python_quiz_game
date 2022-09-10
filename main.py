from utils import clear_console
from quiz_brain import QuizBrain


def main():
    quiz_brain = QuizBrain()

    game_running = True
    while game_running:
        try:
            question = quiz_brain.next_question()
        except StopIteration:
            break

    print("-" * 40)
    print("You've completed the quiz.")
    print(f"Your final score: {quiz_brain.user_score}/{quiz_brain.question_index}")


if __name__ == "__main__":
    clear_console()
    main()
