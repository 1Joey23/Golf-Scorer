# The class, Score.
class Score():
    
    nScoreHoleNumber = None
    nHoleScore = None
    nHolePar = None
    
    # Initialize the class, Score.
    def __init__(self, scoreHoleNumber, holeScore, par):
        self.nScoreHoleNumber = scoreHoleNumber
        self.nHoleScore = holeScore
        self.nHolePar = par
        
    # Output string returns the Score and the Score Name.
    def __str__(self):
        scoreType = self.PrintScoreType(self.nHoleScore, self.nHolePar)
        return f"Score: {self.nHoleScore}, {scoreType}"
    
    # Assign the Score type to the users score. (i.e. 1 below par is a birdie.)
    def PrintScoreType(self, holeScore, par):
        holeScore = int(holeScore)
        par = int(par)
        difference = holeScore - par

        if holeScore == 0 or holeScore < 0 or difference == par:
            return "Invalid Score!"
        
        elif difference == -4:
            if holeScore == 1:
                return "Hole in One, Condor!"
            else:
                return "Condor!"
        
        elif difference == -3:
            if holeScore == 1:
                return "Hole in One, Albatros!"
            else:
                return "Albatros"
        
        elif difference == -2:
            if holeScore == 1:
                return "Hole in One, Eagle!"
            else:
                return "Eagle"
        
        elif difference == -1:
            return "Birdie"
        
        elif difference == 0:
            return "Par"
        
        elif difference == 1:
            return "Bogey"
        
        elif difference == 2:
            return "Double Bogey"
        
        elif difference == 3:
            return "Triple Bogey"
        
        else:
            return f"{difference} above par"
        