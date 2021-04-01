#create the class
class ATM(object):
    def __init__(self,card_number,pin_number):
        self.card_number=card_number
        self.pin_number   

    def cashwithdrawal(self):
        print("cashwithdrawal")

    def balanceenquiry(self) :
        print("balanceenquiry")

#create the object
ICICI=ATM("100000","1000000")
print(ICICI.card_number())
print(ICICI.pin_number)

