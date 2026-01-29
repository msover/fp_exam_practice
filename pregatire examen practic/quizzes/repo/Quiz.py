from data.Question import Question


class Quiz:
    def __init__(self, questionList: list[Question] = None):
        if questionList is None:
            self.questionList: list[Question] = []
        else:
            self.questionList = questionList

    def add(self, question: Question):
        if question in self.questionList:
            raise ValueError("Cannot have duplicate ID")
        self.questionList.append(question)

    def remove(self, question: Question):
        if question in self.questionList:
            self.questionList.remove(question)

    def wipe(self):
        self.questionList = []

    def __iter__(self):
        return iter(self.questionList)

    def __str__(self):
        printString = ''
        for question in self.questionList:
            printString += f"{question}\n"
        return printString
