import math
actual_cost=(float(input("enter the actual cost of product:")))
sale_cost=(float(input("Enter the sales amount of product:")))
profit=sale_cost-actual_cost

if actual_cost<sale_cost:
   
    print("the profit earned by the product is:{0}".format(profit))
else:
    

    print("Loss occured of {0}".format(abs(profit)))