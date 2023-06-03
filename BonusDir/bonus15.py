#Learning how to work with JSON 
import json

with open('bonus15questions.json', 'r') as file:
    content = file.read()

data = json.loads(content)

# print(type(content))
# print(type(data))
# print(data)

score = 0 

for question in data:
   print(question["q_text"])
   for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, '-', alternative)
   user_choice = int(input("Enter your answer: ").strip())
   question["user_answer"] = user_choice
   if question["user_answer"] ==  question["correct_answer"]:
       score += 1
       question["user_correct"] = "Correct"
   elif question["user_answer"] !=  question["correct_answer"]:
       question["user_correct"] = "Incorrect"

print('\n')
for index, question in data:
    correct_answer_index = question['correct_answer'] - 1
    answers = question['alternatives']
    message = f"Q{index + 1}) Your answer: {question['user_answer']}, Correct answer: {question['correct_answer']} ({answers[correct_answer_index]}) | You were {question['user_correct']}"
    print(message)


print("\nYour Score: " + str(score), '/', len(data))

