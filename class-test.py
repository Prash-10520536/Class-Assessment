#global dictionary
discounts={'rice':0.5,'eggs':0.8,'flour':0.6} #discount
prices = {"flour": 2, "eggs": 3, "rice": 5} #price


class Shopping :
    
    def __init__(self, basket={}):
        self.__basket = basket
        
    #to add items and quants
    trolly={}
    def addItems(self, items, quant):        
        trolly[items] = quant
        print(trolly)
        
    #getting price with discount
    def getPrice(self):
        i=0
        priceL=[] #for price list
        for k,v in trolly.items():
            i+=prices[k]*trolly[k]*discounts[k] #applying dicsount
            priceL.append(i)        
        
        print(priceL) #to print after appending 
        self.priceSort(priceL)
        return i

    #sorting using bubble sort
    def priceSort(self,bList):
        lowP=len(bList)
        for i in range(lowP-1):
                for j in range(lowP-1-i):
                    if bList[j] >bList[j+1]:
                        bList[j],bList[j+1]=bList[j+1],bList[j]
                            
        print("Price highest to lowest ", bList[::-1])
        return bList

