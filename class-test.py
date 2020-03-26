discounts={'discCode1':0.5,'discCode2':0.8,'discCode3':0.10}

class Shopping :
    
    price = {"eggs": 2, "rice": 3, "flour": 5} #price
    
    def __init__(self, price):
        self.total = 0
        self.price = price
        self.items = {}
    

def doBuy():    
    for price in basket.values():
        if(price>0) :
            if(price==2):
                discount = price*discounts["discCode1"]
            elif(price==3):
                discount = price*discounts["discCode2"]
            elif(price==5):
                diccount = price*discounts["discCode3"]
            
            total = price - discount
            return total
