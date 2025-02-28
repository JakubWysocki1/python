class Grades:

    def getGrade(self, examIn, caIn):
        grade = ""

        if examIn < 0 or examIn > 100 or caIn < 0 or caIn > 100:
            grade = "Invalid input"
        elif examIn < 40 or caIn < 40:
            grade = "Component Fail"
        else:
            combined = (60 * examIn + 40 * caIn) / 100

        if combined < 60:
            grade = "Fail"
        elif combined >= 60 and combined <= 80:
            grade = "Pass"
        elif combined > 80 and combined <= 100:
            grade = "Pass with distinction"

        return grade

grade = Grades()
exam = int(input("Enter exam result: "))
ca = int(input("Enter ca result: "))
print("Student's overall grade is: " + grade.getGrade(exam, ca))