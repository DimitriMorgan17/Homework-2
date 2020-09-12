# author Dimitri Morgan dpm5792@psu.edu

Firstg = 0
Firstc = 0
Secondg = 0
Secondc = 0
Thirdg = 0
Thirdc = 0

grade = float(0)
def run():
  def getGradePoint(test):
    global grade
    if test == "A":
      grade = 4.0
    elif test == "A-":
      grade = 3.67
    elif test == "B+":
      grade = 3.33
    elif test == "B":
      grade = 3.0
    elif test == "B-":
      grade = 2.67
    elif test == "C+":
      grade = 2.33
    elif test == "C":
      grade = 2.0
    elif test == "D":
      grade = 1.0
    else: grade = 0.0

  def FirstGrade() :
    global Firstg
    global Firstc
    Firstg = str(input("Enter your course 1 letter grade: "))
    Firstc = input("Enter your course 1 credit: ")
    Firstc = float(Firstc)
    getGradePoint(Firstg)
    Firstg = float(grade)
    print(f"Grade point for course 1 is: ", Firstg)

  def SecondGrade() :
    global Secondg
    global Secondc
    Secondg = str(input("Enter your course 2 letter grade: "))
    Secondc = input("Enter your course 2 credit: ")
    Secondc = float(Secondc)
    getGradePoint(Secondg)
    Secondg = float(grade)
    print(f"Grade point for course 2 is: ", Secondg)

  def ThirdGrade() :
    global Thirdg
    global Thirdc
    Thirdg = str(input("Enter your course 3 letter grade: "))
    Thirdc = input("Enter your course 3 credit: ")
    Thirdc = float(Thirdc)
    getGradePoint(Thirdg)
    Thirdg = float(grade)
    print(f"Grade point for course 3 is: ", Thirdg)

  def GPA() :
      FirstGrade()
      SecondGrade()
      ThirdGrade()
      global gpaFunc 
      gpaFunc = ((Firstg*Firstc) + (Secondg*Secondc) + (Thirdg*Thirdc)) / (Firstc + Secondc + Thirdc)
  GPA()
  print(f"Your GPA is: ", gpaFunc)
if __name__ == "__main__":
  run ()