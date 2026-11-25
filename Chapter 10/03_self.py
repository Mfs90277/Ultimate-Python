class Employee:
    language = "Python"  # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

faiz = Employee()
faiz.language = "JavaScript"  # This is an instance attribute
faiz.getInfo()
faiz.greet()
#Employee.getInfo(faiz)  # This is another way to call the method
