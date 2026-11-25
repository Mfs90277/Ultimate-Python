class Employee:
    language = "Python"  # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language):  # Dunder Method Which is automatically called when you create an new object of the class.
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

faiz = Employee("Faiz", 1300000, "JavaScript")
#faiz.name = "Faiz"
print(faiz.name, faiz.salary, faiz.language)

#rohan = Employee()
