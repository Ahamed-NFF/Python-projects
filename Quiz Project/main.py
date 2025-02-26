from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    # question = Question(item['text'], item['answer'])
    question_text = item["text"]
    question_answer = item["answer"]
    new_question = Question(question_text,question_answer)

    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)
quiz_brain.next_question()

score = 0

while quiz_brain.still_has_questions():
    score = quiz_brain.next_question()

print("You have completed the quiz")
print(f"You final score is : {score}/12")
