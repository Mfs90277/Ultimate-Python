class Employee:
    language = "Python"  # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

faiz = Employee()
faiz.language = "JavaScript"  # This is an instance attribute
faiz.getInfo()


