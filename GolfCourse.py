# Input the Hole class from Holy.py
from Hole import Hole

# Define the GolfCourse Class.
class GolfCourse():
    
    sName = None
    nHoleCount = None
    nCoursePar = None
    lstHoles = []
    
    # Initialize the fields.
    def __init__(self, name, holeCount, coursePar):
        self.sName = name
        self.nHoleCount = holeCount
        self.nCoursePar = coursePar
        self.lstHoles = []
        
    # The self string which outputs the golfcourse name, total holes, and total par of each hole.
    def __str__(self):
        return f"Golf Course: {self.sName}, Total Holes: {self.nHoleCount}, Total Par: {self.nCoursePar}"
    
    # Add hole to list of holes in the golfcourse.
    def AddHole(self, number, name, par):
        hole = Hole(number, name, par)
        self.lstHoles.append(hole)
        
        return hole
        
    # Asks user for name for golfer and adds golfer while printing data.
    def Advertise(self):
        print(self)
        currentGolfer = input(f"Enter a name for your golfer: ")
        
        for hole in self.lstHoles:
            
            hole.AddGolfer(currentGolfer, hole.nNumber)
            print(hole)
            