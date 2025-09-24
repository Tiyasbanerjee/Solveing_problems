list_ = input("Enter the list of numbers separated by coma: ").split(',')
length_of_list = len(list_)-1
print(length_of_list)
for i in range(length_of_list):
       list_[i+1], list_[i] = list_[i] , list_[i+1]            # evens will be 0 , 2 , 4, 6, 7,8 ....
                                                               # odds will be 1 , 3, 5 , 7 , 9 ,11  ...
         
print(list_)