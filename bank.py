#Encapulation
class Bank:
    def __init__(self,name,age,amount):
        self.name=name #Public Attribute
        self._age=age  #protected Attribute
        self.__amount=amount   #private Attribute
    def get_balance(self):
        return f"Current balance is {self.__amount}"
    def withdraw(self,withdraw_amount):
        if self.__amount>=withdraw_amount:
            self.__amount -=withdraw_amount
            return f"withdraw is successful and current balance is {self.__amount}"
        else:
            return "Insufficient amount"
    def _totalUser(self):   #Protrcted Method
        return "Total users in bank"
    def __total_amount(self):   #private Method
        return "Total amount in bank"
