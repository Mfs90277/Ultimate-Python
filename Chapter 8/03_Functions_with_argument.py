def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)

goodDay("Faiz", "Thankyou!")
goodDay("Rohan", "Thankyou!")
goodDay("Suhani", "Thanks!")

def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "Ok"

a = goodDay("Harry", "Thank You")
print(a)