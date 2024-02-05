#Class
class Participant:
    def __init__(self, name): #Method
        self.name = name #Attribute
        self.points = 0
        self.choice = ""
    def choose(self):
        self.choice = input("\n{name}, select rock, paper or scissor: ".format(name=self.name))
        print("\n{name} selects {choice}".format(name=self.name, choice=self.choice))
    def toNumericalChoice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2
        }
        return switcher[self.choice]
    def incrementPoint(self):
        self.points += 1

class GameRound:
    def __init__(self, p1, p2):
        self.rules = [      # __Matrix array attribute of beatable combinations__
            [0, -1, 1],     # Rock v [Rock, Paper, Scissors)
            [1, 0, -1],     # Paper v [Rock, Paper, Scissors)
            [-1, 1, 0]      # Scissors v [Rock, Paper, Scissors)
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print("Round resulted in a {result}".format(result=self.getResultAsString(result)))
        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()
        else:
            print("No points for anybody.")
    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
    def awardPoints(self):
        print("implement")
    def getResultAsString(self, result):
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }
        return res[result]

class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant(input("Player 1: enter your name: "))
        self.secondParticipant = Participant(input("Player 2: enter your name:"))
    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
    def checkEndCondition(self):
        answer = input("Continue game y/n: ")
        if answer == 'y':
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print("Game ended, {p1name} has {p1points} point(s), and {p2name} had {p2points} point(s)".format(p1name=self.participant.name, p1points=self.participant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True
    def determineWinner(self):
        resultString = "It's a Draw"
        if self.participant.points > self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.secondParticipant.name)
        print(resultString)

game = Game()
game.start()
