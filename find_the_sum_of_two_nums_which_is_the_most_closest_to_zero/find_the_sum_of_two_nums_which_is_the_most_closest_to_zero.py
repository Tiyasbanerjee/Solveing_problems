try:
    list_ = input("Input a list of numbers separated by commas: ").split(',')
    new_list = []
    for i in list_:
        new_list.append(int(i))
    list_ = new_list
    print("cheak:-----0")

except ValueError:
    list_ = [1, 60, -10, 70, -80, 85]

print("cheak:----1")

def find_c_t_z(lst_):
    sorted_list = sorted(list_)
    print("chealk:-----2")

    if sorted_list[0] < 0:
        print("cheak:-------3.0")
        if sorted_list[-1] <=0:
            print("cheak:-----4.0")
            return sorted_list[-1] , sorted_list[-2]
        else:
            print("cheak:------4.1")
            negetive_nums = []
            positive_nums = []
            length = len(list_)
            
            for i in range(length):
                if sorted_list[i] > 0:
                    print("cheak:-----5.0")
                    positive_nums.append(sorted_list[i])
                elif sorted_list[i] < 0:
                    print("cheak:-----5.1")
                    negetive_nums.append(sorted_list[i])
                else:
                    print("cheak:------5.2")
                    if  sorted_list[i-1] + sorted_list[i+1] < 0:
                        print("cheak:-------6.0")
                        return 0 , sorted_list[i+1]
                    elif sorted_list[i-1] + sorted_list[i+1] > 0:
                        print("cheak:------6.1")
                        return 0 , sorted_list[i-1]
                    else:
                        print("cheak:--------6.2")
                        return 0 , [sorted_list[i-1],sorted_list[i+1]]
            
            min_error = [max(sorted_list),[]]
            
            print("cheak:-------7")
            print(positive_nums,negetive_nums)

            for i in negetive_nums:
                for j in positive_nums:
                    error = abs(i+j)
                    if error < min_error[0]:
                        min_error[0] , min_error[1] = error , [i,j]
            
            print("cheak:----------8")
            return min_error[1][0] , min_error[1][1]

    else:
        print("ckeak:-----3.1")
        return sorted_list[0] , sorted_list[1]
    


a,b = find_c_t_z(list_)
print(a,b)