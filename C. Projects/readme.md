## My Python Projects

<h1>Rock, Paper, Scissors Simulator</h1>
The purpose of this project is to develop the actors, behavior, and conditions to run simulated outcomes for a game of Rock-Paper-Scissors. 

<h2>Modeling</h2>
I'll start by modeling our <b>Phases</b>, <b>actors</b>, <b>behaviors</b>, and <b>data</b>:<br></br>

Phase | Actor | Behavior | Data
|:---|:---|:---|:---|
Input | Participant | Chooses Symbol | Symbol saved as <i>choice</i> on Participant(choice) | 
Processing | GameRound | Compares choices against game rules. | <i>Result</i> inspected | 
Processing | GameRound | Awards points based on result value | <i>Points</i> added to weiing Participant(point) | 
Processing | Game | Check "continue?" answer | If TRUE, continue, else quit | 
Output | Game | New game round or game end credit | collect answer

This allows me to guide my code development and account for any changes to method and attribute declarations in the programming. 

The inital code - which focuses on developing the <b>ACTOR</b> classes- will look like: 

```py
class Participant:
  def __init__(self):
    self.points = 0 #We'll turn this into a protected variable using double "_" later. 

class GameRound:
  print("Replace this later")    

class Game: # We'll use placeholders for now
  def __init__(self):
    self.endGame = False
    self.particpant = Participant() #instantiating the **Participant** class for this attribute as player one.
    self.secondParticipant = Participant() #instantiating the **Participant** class for this attribute as player two.
```
<h4>Coding Logic</h4>
<ol>
<li>Create a class that holds individual participant attributes related to sign choice, points scored, and names.</li> 
<li>Create a class - GameRound - that processes the winning criteria for a round (win, loss, draw) and awards points when processed.</li>
<li>Create a class - Game - which houses the winning conditions, exit conditions, and overall continuous loop of the program till executed.</li>
</ol>

<h2>Starting a Game</h2>
The first part of any game is <u>setting up and waiting for participants to act</u>.<br>
That being said, we'll need to develop the **Game** class to establish that environment next.<br>

First, we'll adjust the **Game** class and add additional methods to account for game start, end conditions, and determining the winner:

```py
class Game: # We'll set this up to call in main and to guide the player's game journey.
  def __init__(self): # instantiation method
    self.endGame = False
    self.particpant = Participant("Player 1") #instantiating the **Participant** class for this attribute as player one.
    self.secondParticipant = Participant("Player 2") #instantiating the **Participant** class for this attribute as player two.
  def start(self):
    game_round = GameRound(self.particpant, self.secondParticipant)
  def checkEndCondition(self):
      print("Placeholder")
  def determineWinner(self):
      print("Placeholder")

##### MAIN #####

game = Game()
game.start() # Calls the GameRound method.
```
