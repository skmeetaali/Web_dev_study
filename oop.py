class basket():
    def __init__(self, budget):
        self.budget = budget
        self.items = {}
        
    def addItem(self, item, price):
        if self.overBudget(price):
            print( f"cannot add item: {item}")
        else:
            self.items[item] = price
        
    def overBudget(self, price):
        prices = self.items.values()
        curr_sum = sum(prices) 
        new_sum = curr_sum + price
        if self.budget < new_sum:
            return True
        else:
            return False
        
    def print(self):
        print(self.items)        
        
bucket = basket(100)
bucket.addItem("cake", 45)
bucket.addItem("flower", 25)
bucket.addItem("ribbon", 35)
bucket.addItem("ribbon", 35)

bucket.print()