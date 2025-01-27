
# Kakuro number sums, i.e. 24 can be written as 9+8+7, while 6 can be written as 5+1 and 4+2 (3+3 not eligible since the numbers added should be unique).


# one = 1
# two = 2
# three = 3
# four = 4
# five = 5
# six = 6
# seven = 7
# eight = 8
# nine = 9

final_numbers=[]

available_number_spots = int(input("How many available spots? "))
total_sum = int(input("What is the sum? "))
print("\n")

print("With",available_number_spots, "available spots, the number", total_sum, "can be written as the sum of:")
for one1 in range(0,2):
    for two2 in range(0,2):
        for three3 in range(0,2):
            for four4 in range(0,2):
                for five5 in range(0,2):
                    for six6 in range(0,2):
                        for seven7 in range(0,2):
                            for eight8 in range(0,2):
                                for nine9 in range(0,2):
                                    if one1*1 + two2*2 + three3*3 + four4*4 + five5*5 + six6*6 + seven7*7 + eight8*8 + nine9*9 == total_sum and one1 + two2 + three3 + four4 + five5 + six6 + seven7 + eight8 + nine9 == available_number_spots:
                                        
                                        number_list = [one1*1,two2*2,three3*3,four4*4,five5*5,six6*6,seven7*7,eight8*8,nine9*9]
                                        
                                        for i in range(0,len(number_list)):
                                            if number_list[i] != 0:
                                                final_numbers.append(number_list[i])


chunk_size = available_number_spots
list_chunked = [final_numbers[i:i + chunk_size] for i in range(0, len(final_numbers), chunk_size)]



for i in range(0,len(list_chunked)):
    print(list_chunked[i])

# from itertools import permutations 

# for i in range(0,len(list_chunked)):
#     perm = permutations(list_chunked[i])
#     for i in list(perm):
#         print(list(i))




  
  
# Get all permutations of [1, 2, 3] 
# perm = permutations([1, 2, 3]) 
  
# Print the obtained permutations 
# for i in list(perm): 
#     print (i) 





if len(list_chunked) == 1:
    print("There is",len(list_chunked),"possible solution.")
else:
    print("There are",len(list_chunked),"possible solutions.")







def reverse_string(input):
    string = "".join(reversed(input))
    return string

str_data = "Game_of_Thrones"
# print(reverse_string(str_data))



'''
final_numbers=[]

available_number_spots = 4#list(range(3,10)) # int(input("How many available spots? "))
total_sum = list(range(3,46)) # int(input("What is the sum? "))
print("\n")

for i in range(available_number_spots):
    for j in range(len(total_sum)):
        

        #print("With",available_number_spots, "available spots, the number", total_sum, "can be written as the sum of:")
        for one1 in range(0,2):
            for two2 in range(0,2):
                for three3 in range(0,2):
                    for four4 in range(0,2):
                        for five5 in range(0,2):
                            for six6 in range(0,2):
                                for seven7 in range(0,2):
                                    for eight8 in range(0,2):
                                        for nine9 in range(0,2):
                                            if one1*1 + two2*2 + three3*3 + four4*4 + five5*5 + six6*6 + seven7*7 + eight8*8 + nine9*9 == total_sum[j] and one1 + two2 + three3 + four4 + five5 + six6 + seven7 + eight8 + nine9 == available_number_spots:
                                                
                                                number_list = [one1*1,two2*2,three3*3,four4*4,five5*5,six6*6,seven7*7,eight8*8,nine9*9]
                                                
                                                for i in range(0,len(number_list)):
                                                    if number_list[i] != 0:
                                                        final_numbers.append(number_list[i])


        chunk_size = available_number_spots
        list_chunked = [final_numbers[i:i + chunk_size] for i in range(0, len(final_numbers), chunk_size)]
        print("Sum:",total_sum[j],", Spots:",available_number_spots,", Solutions:",len(list_chunked))
        # for i in range(0,len(list_chunked)):
        #     print(list_chunked[i])

        # if len(list_chunked) == 1:
        #     print("There is",len(list_chunked),"possible solution.")
        # else:
        #     print("There are",len(list_chunked),"possible solutions.")
'''