# 1. make a list with all multiples of 3 up to 1k
# 2. make a list with all multiples of 5 up to 1k
# 3. make a list by concatenating those lists
# 4. delete all entries that appear more than once
# 5. sum the entries

import math

bignumber = math.factorial(9)
iteration_limit = 1000
iter3 = 0
iter5 = 0
three_list = []
five_list = []
sum_list = []
bigsum = 0

def bigsum_function():

    global iteration_limit
    global iter3
    global three_list
    global iter5
    global five_list
    global bigsum

    #grab every number divisible by 3 up to 1000
    for i in range(bignumber):

        if iter3 + 3 < iteration_limit:
            iter3 = iter3 + 3
            three_list.append(iter3)     

        else:
            #print(str(three_list))
            break

    # remove elements divisible by 5
    for i in three_list:
        if i % 5 == 0:
                three_list.remove(i)

    #make five_list
    for i in range(bignumber):
    
            if iter5 + 5 < iteration_limit:
                iter5 = iter5 + 5
                five_list.append(iter5)     
    
            else:
                #print(str())
                break

    #concatenate five_list and three_list
    sum_list = three_list + five_list
    #print(str(sum_list))

    #sum items in sum_list
    for i in sum_list:
        bigsum = bigsum + i

    print("bigsum: "+str(bigsum))


bigsum_function()


