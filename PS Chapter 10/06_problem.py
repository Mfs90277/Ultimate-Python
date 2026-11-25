from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on the time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {fro} to {to} is {randint (222,555)}")


t = Train(13009)
t.book("Rampur", "Ayodhya")
t.getstatus()
t.getFare("Rampur", "Ayodhya")
