import time


class Account(object):
    
    count = 0
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = Account.count
        Account.count += 1
        self.transaction_history = []

    def withdraw(self, price):
        if self.balance <= price:
            print(f"残高：{self.balance}円。不足です")
        else:
            self.balance -= price
            self.add_transaction_history(price)

    def deposit(self, price):
        self.balance += price
        self.add_transaction_history(price)


    @staticmethod
    def get_time_str():
        current_time = time.localtime()
        return "{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分".format(current_time)
        
    def add_transaction_history(self, price):
        transaction = {
            "名義":self.name,
            "口座番号":self.account_number,
            "取引時間":Account.get_time_str(),
            "取引金額":price,
            "残高":self.balance,
		}
        self.transaction_history.append(transaction)
        print(self.transaction_history)
        
    def show_transaction_history(self):
        for transaction in self.transaction_history:
            for k, v in transaction.items():
                print(k, v)
            
    


kazu = Account("KAZU", 1000000)
kazu.deposit(100000)
kazu.deposit(30000)

print("\n")
print("################################################")
kazu.show_transaction_history()


