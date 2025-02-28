class Grade():
    EXAM_WEIGHTING = 60
    CA_WEIGHTING = 40

    #Constructor - expects 2 parameters
    def __init__(self, exam_result_in, ca_result_in):
        self.exam_result = exam_result_in
        self.ca_result = ca_result_in


    #Method that will return your Grade based on your Exam and CA result
    def calculate_grade_category(self):
        try:
            self.exam_result = float(self.exam_result)
            self.ca_result = float(self.ca_result)

            if self.exam_result < 0 or self.exam_result > 100 or self.ca_result < 0 or self.ca_result > 100:
                grade = "Invalid input"
            elif self.exam_result < 40 or self.ca_result < 40:
                grade = "Component Fail"
            else:
                combined = (self.EXAM_WEIGHTING * self.exam_result + self.CA_WEIGHTING * self.ca_result) / 100
                if combined < 60:
                    grade = "Fail"
                elif combined >= 60 and combined <= 80:
                    grade = "Pass"
                elif combined > 80 and combined <= 100:
                    grade = "Pass with distinction"
        except ValueError:
            grade = "Invalid input"

        return grade


if __name__ == '__main__':
    print("******                  *******    ")
    print("****** Running Grades   *******    ")
    exam = input("Please enter your exam percentage: ")
    ca = input("Please enter your CA percentage:  ")
    grades = Grade(exam,ca)
    print("->", grades.calculate_grade_category())
