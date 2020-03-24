discCode1 = float[0.5]
discCode2 = float[0.8]
discCode3 = float[0.010]

class Shopping :
    
    basket = {"eggs": 10, "rice": 15, "flour": 20} #qantity
    price = {"eggs": 8, "rice": 12, "flour": 10} #price

def bill(food):
    total = 0
    for items in basket:
        if(price>0) :
            if(price==8):
                discount = price*discCode1
            elif(price==12):
                discount = price*discCode2
            elif(price==10):
                diccount = price*discCode3
            
            total = price - discount
            return total
                
            
        
    
    
    

    
