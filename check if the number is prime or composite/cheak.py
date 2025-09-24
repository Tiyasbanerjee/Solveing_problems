inp = int(input("Input number:  "))       # if x is prime only devided by 1 and x, and if non-prime than devided by some number except 1 and x |
list_of_deviders = []
for i in range(2,int(inp**(1/2))+1):      # takeing squre-root(x) because x can be written as a*b = x and x = p^2 |  a or b can max to max be x  and min to min 1 | 
      if  inp % i == 0 :
            list_of_deviders.append(i)                               # if 1<a<p than b must be p<b<x |  i can try eather for-- if x % b == 0 , for which i have to cheak for elements gratten than x**(1/2) 
            list_of_deviders.append(inp//i)                             #  and smaller than x, but if i cheak for x % a == 0 , i have to cheak for elements bigger than 1 and smalller than x**(1/2) |
                                         #  cheaking set of all values of b , will see that b contains bigger values and while ittrateing in a for loop we have to do lot more 
if list_of_deviders == []:                                          # ittrations or cheaks , because in a i have to ittrate for x**(1/2)-1 values ,but in b i have to ittrate for [x**(1/2)]*{[x**(1/2)]-1} | 
        print(f"{inp} is a prime")                                  # for b insted of a , i have to cheak for nealry w^2 terms where for a , i only have to cheak for w values.  
else:
       print(f"{inp} is a non-prime number with deviders (except 1 and {inp}):--- {list_of_deviders}")

