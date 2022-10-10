import question_model
import quiz_brain

stop = False
while stop == False:
    score = 0
    quesno = 0
    quesno += 1
    question_model.ask_data()
    data = question_model.DataCenter
    data.question = question_model.ques
    data.answer = question_model.ans
    attri = quiz_brain.Attributes
    attri.score = score
    attri.question_number = quesno
    print(data.question)
    print("your score - " + str(attri.score) + "/" + str(attri.question_number))
    user_answer = input("What do you think it is true or false\n->").lower()
    if user_answer == data.answer.lower():
        score += 1
        print("gg's")
    else:
        stop = True
        print("lost!!\nyour final score was")
        print("your score - " + str(attri.score) + "/" + str(attri.question_number))
