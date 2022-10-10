class DataCenter:
    def __int__(self, question: object, answer: object) -> object:
        self.question = question
        self.answer = answer


ques = ""
ans = ""


def ask_data():
    import data
    global ques, ans
    import random
    data_range = random.randint(0, len(data.question_data) - 1)
    ques = str(data.question_data[data_range]["text"])
    ans = str(data.question_data[data_range]["answer"])

# import question_model
# stop = False
# while stop == False:
#     question_model.ask_data()
#     data = question_model.DataCenter
#     data.question = question_model.ques
#     data.answer = question_model.ans
#     print(data.question)
#     print(data.answer)
