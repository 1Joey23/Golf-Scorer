# Input the Golfcourse class from GolfCourse.py
from GolfCourse import GolfCourse

# Import the csv to get commands.
import csv

# Open and interpret the data from the golf input csv file and the user, and assign data accordingly.
def ReadGolfFile():
    golfFileInput = open(r"C:\Users\Joey\Documents\GitHub\Golf-Scorer\GolfCourseInput.csv", "r")
    
    currentGolfCourse = None
    lstGolfCourses = []
    
    for record in golfFileInput:
        record = record.replace("\n", "")
        line = record.split(",")
        
        if line[0] == "C":
            currentGolfCourse = ProcessGolfFile(line)
            lstGolfCourses.append(currentGolfCourse)
        elif line[0] == "H":
            currentHole = currentGolfCourse.AddHole(line[1], line[2], line[3])
        
    golfFileInput.close()
    OutputGolfCourse(lstGolfCourses)
    TotalData(lstGolfCourses)
    WriteFileOutput(lstGolfCourses)
    
    return lstGolfCourses
    
# Print each course in the lst of golfcourses and call print method in GolfCourse.py
def OutputGolfCourse(lstGolfCourses):
    for course in lstGolfCourses:
        course.Advertise()
    
# Add data from table to the golfcourse.
def ProcessGolfFile(line):
    currentGolfCourse = GolfCourse((line[1]), int(line[3]), int(line[2]))
    
    return currentGolfCourse

# Total up all data and return it
def TotalData(lstGolfCourses):
    totalPar = 0
    totalScore = 0

    for course in lstGolfCourses:
        totalPar += course.nCoursePar

        for hole in course.lstHoles:
            for golfer in hole.lstGolfers:
                for score in golfer.lstScores:
                    totalScore += int(score.nHoleScore)

    print(f"User: {golfer.sName}, Total Par: {totalPar}, Total Score: {totalScore}")
    
# Write the output to the GolfCourseOutput.csv
def WriteFileOutput(lstGolfCourses):
    outputFile = open("GolfCourseOutput.csv", 'w', newline='')
    csv_writer = csv.writer(outputFile)

    # Write header row with attributes of class, student, assignment, grage, average assignment percentage, and average assignment grade.
    csv_writer.writerow(["Course Name", "Total Holes", "Total Par", "Golfer", "Hole Number", "Hole Name", "Hole Par", "Score", "ScoreType"])

    # Write all of the information to the csv output file.
    for course in lstGolfCourses:
        for hole in course.lstHoles:
            for golfer in hole.lstGolfers:
                for score in golfer.lstScores:
                    csv_writer.writerow([course.sName, course.nHoleCount, course.nCoursePar, golfer.sName, hole.nNumber,
                                        hole.sName, hole.nPar, score.nHoleScore, score.PrintScoreType(score.nHoleScore, score.nHolePar)])
                    
    # Calculate and write the total score information
    totalPar = sum(course.nCoursePar for course in lstGolfCourses)
    totalScore = sum(int(score.nHoleScore) for course in lstGolfCourses for hole in course.lstHoles for golfer in hole.lstGolfers for score in golfer.lstScores)
    csv_writer.writerow([f"Golfer: {golfer.sName}, Total Par: {totalPar}, Total Score: {totalScore}"])


    outputFile.close()
    
# Run the application.
ReadGolfFile()

    


