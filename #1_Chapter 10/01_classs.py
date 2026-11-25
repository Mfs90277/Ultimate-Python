class Employee:
    language = "py"  # This is a class attribute
    salary = 1200000

faiz = Employee()
faiz.name = "Faiz"  # This is an instance attribute
print(faiz.name, faiz.language, faiz.salary)

sohan = Employee()
sohan.name = "Sohan"  # This is an instance attribute
print(sohan.name, sohan.language, sohan.salary)


#  Here name is instance attribute and language and salary are class attributes as they directly belong to the class.