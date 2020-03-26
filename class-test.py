discounts={'rice':0.5,'eggs':0.8,'flour':0.10}
prices = {"flour": 2, "eggs": 3, "rice": 5} #price
trolly={}

class Shopping :
    
    def __init__(self, basket={}):
        self.__basket = basket
        
    #to add items and quants
    def addItems(self, items, quant):        
        trolly[items] = quant
        print(trolly)
