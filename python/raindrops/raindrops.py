def convert(number):
    raindrop = ''
    if number == 0: 
        return 0
    elif  abs(number) > 0:     
        if number % 3 == 0:
            raindrop += "Pling"
        if number % 5 == 0: 
            raindrop += "Plang"
        if number % 7 == 0:
            raindrop += "Plong" 
        if raindrop == "":    
            return str(number)
        else:
            return raindrop    
    else:
        return str(number)       

print(convert(28))
