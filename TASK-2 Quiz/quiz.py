import random

class QuizGame:
    def __init__(self, quiz_questions):
        self.quiz_questions = quiz_questions
        self.score = 0

    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("You will be asked multiple-choice or fill-in-the-blank questions.")
        print("For each question, select the correct answer.")
        print("Let's get started!\n")

    def present_question(self, question):
        print(question["question"])

        if question["type"] == "multiple_choice":
            random.shuffle(question["choices"])
            for i, choice in enumerate(question["choices"], start=1):
                print(f"{i}. {choice}")

            try:
                user_choice = int(input("Enter the number of your choice: "))
                user_answer = question["choices"][user_choice - 1]
            except (ValueError, IndexError):
                user_answer = input("Invalid input. Please enter your answer: ")

        else:  # Fill-in-the-blank type
            user_answer = input("Enter your answer: ")

        return user_answer

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is: {correct_answer}\n")

    def display_final_results(self):
        total_questions = len(self.quiz_questions)
        percentage_score = (self.score / total_questions) * 100
        print(f"Your Final Score: {self.score}/{total_questions}")
        print(f"You scored {percentage_score:.2f}%")

    def play(self):
        self.display_welcome_message()

        random.shuffle(self.quiz_questions)

        for question in self.quiz_questions:
            user_answer = self.present_question(question)
            self.evaluate_answer(user_answer, question["answer"])

        self.display_final_results()

if __name__ == "__main__":
    # Sample quiz questions
    quiz_questions = [
        {
            "question": "What is the capital of France?",
            "type": "multiple_choice",
            "choices": ["Paris", "London", "Berlin", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "type": "multiple_choice",
            "choices": ["Venus", "Mars", "Mercury", "Jupiter"],
            "answer": "Mercury"
        },
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "type": "fill_in_the_blank",
            "answer": "Shakespeare"
        }
    ]

    while True:
        quiz_game = QuizGame(quiz_questions)
        quiz_game.play()

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break