class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode


p = Programmer("Faiz", 120000, 244713)
print(p.name, p.salary, p.pincode, p.company)
r = Programmer("Rohan", 1200090, 244713)
print(r.name, r.salary, r.pincode, r.company)