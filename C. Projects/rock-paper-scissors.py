class Participant: # sets the actor blueprint
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""

    def choose(self):
        self.choice = input("{name}, select rock, paper, or scissor: ".format(name= self.name))
        print("{name} selects {choice}".format(name=self.name,  choice = self.choice))

    def toNumericalChoice(self):
        switcher = { "rock": 0, "paper": 1, "scissor": 2}
        return switcher[self.choice]

    def incrementPoint(self):
        self.__points__ +=1 #Error on 02.04.2024 @ 15:19

class GameRound:
    def __init__(self, p1, p2):
        self.rules = [ 
            [0,-1,1], #Rock v [Rock, Paper, Scissors]
            [1,0,-1], #Paper v [Rock, Paper, Scissors]
            [-1,1,0] #Scissors v [Rock, Paper, Scissors]
         ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1,p2)
        if result > 0: 
            p1.incrementPoint() #Error on 02.04.2024 @ 15:19
        elif result <0: 
            p2.incrementPoint()
        print("Round resulted in a {result}".format(result=self.getResultAsString(result) ))

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

    def getResultAsString(self,result):
        res = {0: "draw", 1: "win", -1: "loss"}
        return res[result]
        
    def awardPoints(self):
        print("implement")

class Game: # Sets the game parameter blueprint
    def __init__(self):
        self.endGame = False #sets the ending
        self.participant = Participant("Spock") #sets the actor varible
        self.secondParticipant = Participant("Kirk") #sets another actor variable

    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant) #Error on 02.04.2024 @ 15:19
            self.checkEndCondition()
        
    
    def checkEndCondition(self):
        answer = input("Continue game y/n: ")
        if answer == 'y':
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition
        else: 
            print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name = self.participant.name, p1points = self.participant.points, p2name = self.secondParticipant.name, p2points = self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True
        

    def determineWinner(Self):
        resultString = "It's a Draw"
        if self.participant.points > self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.secondParticipant.name)
        print(resultString)

game = Game()
game.start() #Error on 02.04.2024 @ 15:19
