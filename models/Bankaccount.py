class Bankaccount:
    def __init__(self, balance):
        self.balance = balance
        
    def __add__(self, other):
        if isinstance(other, Bankaccount):
            new_balance = Bankaccount(self.balance + other.balance)
            new_ac = new_balance
            return new_ac
        return None
    
    def __sup__(self, other):
        if isinstance(other, Bankaccount):
            new_balance = self.balance - other.balance
            new_ac = Bankaccount(new_balance)
            return new_ac
        return None
        
    def __str__(self):
        return f"Balance: {self.balance:,.2f} "
    
    