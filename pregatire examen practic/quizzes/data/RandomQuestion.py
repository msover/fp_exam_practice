import random

from data.Enums import Difficulty
from data.Question import Question


class RandomQuestion:
    def __init__(self, qid):
        self.operands = [random.randint(1, 50) for _ in range(2)]
        self.operator = random.choice(['+', '-', '*'])
        self.qid = qid
        self.problemText = f'What is {self.operands[0]} {self.operator} {self.operands[1]}?'
        self.a = '0'
        self.b = '0'
        self.c = '0'
        self.answer = '0'
        self.difficulty = Difficulty.EASY
        match self.operator:
            case '+':
                self.difficulty = Difficulty.EASY
                self.answer = self.operands[0] + self.operands[1]
            case '-':
                self.difficulty = Difficulty.MEDIUM
                self.answer = self.operands[0] - self.operands[1]
            case '*':
                self.difficulty = Difficulty.HARD
                self.answer = self.operands[0] * self.operands[1]

        correctChoice = random.randint(1, 3)
        match correctChoice:
            case 1:
                self.a = self.answer
                self.b = self.a + 1
                self.c = self.b + 1
            case 2:
                self.b = self.answer
                self.a = self.b + 1
                self.c = self.a + 1
            case 3:
                self.c = self.answer
                self.a = self.c + 1
                self.b = self.a + 1
        self.a = str(self.a)
        self.b = str(self.b)
        self.c = str(self.c)
        self.answer = str(self.answer)



    def makeQuestion(self) -> Question:
        return Question(self.qid, self.problemText, self.a, self.b, self.c, self.answer, self.difficulty)