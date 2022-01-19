from question_model import Question
from data import question_data1, question_data2,question_data3
from quiz_brain import QuizBrain

def choose_a_category():
    category = input("Choose category: Computers, Video Games, Vehicles: ").lower()
    if category == "computers":
        return question_data1
    if category == "video games":
        return question_data2
    if category == "vehicles":
        return question_data3

question_data =  choose_a_category()

question_bank = []
for question in question_data :
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


# https://opentdb.com/