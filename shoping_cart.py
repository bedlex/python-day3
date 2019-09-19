def shoping_cart(shop_cart):
    cart = shop_cart
    print ("wlecome to your shoping cart")
    while True:
        answer = input("What you wanna to do? \n For see all item print: items. \n For add some items print: add. \n For remove some item print: remove \n For quit print: quit \n")
        if answer.lower() == "quit":
            break
        elif answer.lower() == "items":
            for key, value in cart.items():
                print("{} ${}".format(key,value))   
        elif answer.lower() == "add":            
            cart[input("enter an item: ")] = input("enter item description: ")           
        elif answer.lower() == "remove":
            for key, value in cart.items():
                print("{} ${}".format(key,value)) 
            answer = input("what item you wanna remove?: ")          
            del cart[answer.lower()]
##        answer = input("do you wann se your shopping cart? ")
#        if answer.lower() == "quit":
#            break
#        elif answer.lower() == "yes":
#            print("\n")
#            for key, value in cart.items():
#                print("{} ${}".format(key,value))
#        answer = input ("do you want to remove some items from cart?") 
#        if answer.lower() == "quit":
#            break
#        elif answer.lower() == "yes":
#            answer = input("what do you want to remove? ")
#            if answer.lower() == "quit":
#                break
#            print(answer.lower())
#            del cart[answer.lower()]        
#        elif answer.lower == "no":
#            answer = input("")
#        
                   
            return cart           
 
            
            
#cart = {"laptop" : "2000","tv":"300"}  
#shoping_cart(cart)         