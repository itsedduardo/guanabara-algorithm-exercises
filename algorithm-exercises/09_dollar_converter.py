# Write an algorithm that reads how much money a person has in their wallet (in Brazilian Reais) and shows how many dollars they can buy. Consider US$1.00 = R$3.45.

class Dollar_converter:

    def __init__(self): 
        self.BRL_wallet = 0
        self.US_wallet = 0
        self.max_withdraw = 0        
        self.dollar_price = 3.45
        pass
    #//
    def show_balance(self): 
        print(f"="*35)
        print("Account balance")
        print(f"BRL: R${self.BRL_wallet:.2f}")
        print(f"US: ${self.US_wallet:.2f}")
        print(f"Maximum withdraw US: ${self.max_withdraw:.2f}")
        print(f"="*35)        
        pass
    #//
    def navigation_bar(self):
        print(" ")
        print("Greeting User! What's in your mind today?")
        print("1.[Deposit] | 2.[Convert BRL -> US] | 3.[Withdraw]")
        pass
    #//
    #//
    def user_choice(self):
        #temp input
        action_call = ""

        action_call = str(input(" "))
        if action_call == "1":
            self.bank_deposit()
            self.show_balance()
        elif action_call == "2":
            self.bank_converter()
            self.show_balance()
        elif action_call == "3":
            self.bank_withdraw()
            self.show_balance()
        else:
            exit = str(input("Do you want to exit? [Y/N]: "))
            if exit == "Y":
                return False
            else: pass
    #//
    def maximum_withdraw(self):
        self.max_withdraw = self.BRL_wallet / self.dollar_price
        pass
    #//
    def bank_deposit(self): 
        BRL_deposit = float(input("How much BRL do you want to deposit? R$"))       
        self.BRL_wallet += BRL_deposit
        self.maximum_withdraw()
        pass
    #//
    def bank_converter(self):
        self.US_converter = float(input("How much BRL do you want to convert? R$"))
        if not self.validate_converter():
            return False
        else:
            self.BRL_wallet -= self.US_converter
            self.US_wallet = self.US_converter / self.dollar_price
            self.maximum_withdraw()
        pass
    #//
    def bank_withdraw(self):
        self.US_withdraw = 0
        self.BRL_withdraw = 0
        #/
        currency_choice = str(input("What currency do you wish to withdraw? [BRL/US]: "))
        if currency_choice == "BRL":
            self.BRL_withdraw = float(input("Amount to withdraw: R$"))
            if not self.validate_withdraw():
                return False
            else:
                self.BRL_wallet -= self.BRL_withdraw
        else:
            self.US_withdraw = float(input("Amount to withdraw: $"))
            if not self.validate_withdraw():
                return False
            else:
                self.US_wallet -= self.US_withdraw
        self.maximum_withdraw()
        pass
    #//
    def validate_converter(self):
        #1st test: converter
        if self.US_converter > self.BRL_wallet:
            print(" ")
            print("Invalid amount. Try again.", end=" ")
            print(" ")
            return False
        else: return True
    #//
    def validate_withdraw(self):
        #2nd test: US and BRL Withdraws
        if self.US_withdraw > self.US_wallet:
            print(" ")
            print("Invalid amount. Try again.", end=" ")
            print(" ")
            return False
        #/
        if self.BRL_withdraw > self.BRL_wallet:
            print(" ")
            print("Invalid amount. Try again.", end=" ")
            print(" ")
            return False
        return True
#//
if __name__ == "__main__":
    conv = Dollar_converter()
#//
conv.show_balance()
while True:
    conv.navigation_bar()
    if conv.user_choice() == False:
        break
#//