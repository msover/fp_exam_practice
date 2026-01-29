import random

from data.Enums import Difficulty
from data.Question import Question
from data.RandomQuestion import RandomQuestion
from repo.Quiz import Quiz
from repo.Repo import Repo


class Service:
    def __init__(self):
        self.quizScore = 0
        self.repo = Repo()

    def generateLargeQuiz(self):
        self.repo.openFile("master.txt")
        self.repo.quiz.wipe()
        self.repo.write()
        for index in range(100):
            self.repo.add(RandomQuestion(index).makeQuestion())

    def newQuiz(self, difficulty: Difficulty, numberOfQuestions: int, filename: str):
        self.repo.openFile('master.txt')
        quiz = Quiz(self.repo.quiz.questionList[:])
        ofDifficulty: list[Question] = []
        difficultyCounter = 0
        for question in quiz:
            if question.difficulty == difficulty:
                difficultyCounter += 1
                ofDifficulty.append(question)

        questionsChoice: list[Question] = []
        if difficultyCounter < numberOfQuestions:
            raise ValueError(f"Not enough {difficulty.value} questions")

        for index in range(numberOfQuestions):
            question = random.choice(ofDifficulty)
            questionsChoice.append(question)

        self.repo.openFile(filename)
        self.repo.setQuiz(questionsChoice)

    def addQuestion(self, question: Question):
        self.repo.openFile("master.txt")
        self.repo.add(question)

    def openFile(self, filename: str):
        self.repo.openFile(filename)

    def loadQuestion(self) -> Question | None:
        if len(self.repo.quiz.questionList):
            question = self.repo.quiz.questionList[random.randint(0, len(self.repo.quiz.questionList) - 1)]
            self.repo.remove(question)
            return question
        return None

    def isCorrectAnswer(self, question: Question, answer: str):
        if question.answer == answer:
            self.quizScore += 1
        else:
            self.quizScore -= 1
        return question.answer == answer

    def getQuizScore(self) -> int:
        quizScore = self.quizScore
        self.quizScore = 0
        return quizScore