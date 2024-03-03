# Import the Score Class from Score.py
from Score import Score

# Define Golfer Class.
class Golfer():
    
    sName = None
    lstScores = []
    
    # Initialize the fields.
    def __init__(self, name):
        self.sName = name
        self.lstScores = []
        
    # The Golfer Self String which displays the user's name and joins to the Score class self string.
    def __str__(self):
        scoreJoinString = self.PrintScore()
        return f"{self.sName}, {scoreJoinString}"
    
    # Add and calculate the score from the golfer.
    def AddScore(self, score, scoreHoleNumber, par):
        self.lstScores.append(Score(score, scoreHoleNumber, par))
    
    # Join the self string from golfer to the Score self string.
    def PrintScore(self):
        return ", ".join(str(score) for score in self.lstScores)