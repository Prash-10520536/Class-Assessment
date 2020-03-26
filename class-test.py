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
        
   #getting price with discount
    def getPrice(self):
        i=0
        priceL=[]
        for k,v in trolly.items():
            i+=prices[k]*trolly[k]*discounts[k]
            priceL.append(i)  
            
      def priceSort(self,bList):
        lowP=len(bList)
        for i in range(lowP-1):
                for j in range(lowP-1-i):
                    if bList[j] >bList[j+1]:
                        bList[j],bList[j+1]=bList[j+1],bList[j]
                    print("Prices: High to Low ", bList[::-1])
        return bList
