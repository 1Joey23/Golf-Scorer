# Import Golfer class from Golfer.py
from Golfer import Golfer

# Create hole class.
class Hole():
    
    nNumber = None
    nPar = None
    sName = None
    lstGolfers = []
    
    # Initialize fields.
    def __init__(self, number, name, par):
        self.nNumber = number
        self.sName = name
        self.nPar = par
        self.lstGolfers = []
        
    # The Hole self string which outputs the hole number, name, par, and the user's name by joining the golfer self string.
    def __str__(self):
        golferJoinString = self.PrintGolfers()
        return f"Hole {self.nNumber}: {self.sName} - Par {self.nPar}, User: {golferJoinString}"

    # Add golfer using the inputed name from golfcourse and add it to the list of golfers on each hole number.
    def AddGolfer(self, name, holeNumber):
        golfer = Golfer(name)
        self.lstGolfers.append(golfer)
        
        currentScore = input(f"What is the score for {golfer.sName} on hole {self.nNumber}? ")
        golfer.AddScore(holeNumber, currentScore, self.nPar)
        
        return golfer

    # Joing string to display all golfers in the list of golfers.
    def PrintGolfers(self):
        return ", ".join(str(golfer) for golfer in self.lstGolfers)
        