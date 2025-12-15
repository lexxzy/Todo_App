import json

score = 0

with open('question.json', 'r') as file:
    questions = json.load(file)
for q in questions:
    print(q['question_text'])
    for i, option in enumerate(q['answer_options'], 1):
        print(f"{i}. {option}")
    answer = int(input("Your answer (number): "))
    q["user_answer"] = answer
    if answer == q['correct_answer']:
        result = "Correct Answer"
        score += 1
        print("Correct!\n")
    else:
        result = "Wrong Answer"
        print("Wrong answer.\n")
    message = f"{i + 1}. {q['question_text']} - Your answer: {q['answer_options'][answer - 1]} - {result}"

    
Final_result = {"Total Questions": len(questions), "Correct Answers": score, "Score Percentage": f"{(score/len(questions))*100:.2f}%"}
print(Final_result)
print(message)
