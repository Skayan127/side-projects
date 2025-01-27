f = open("words_alpha.txt", "r")
# f = open("svenska_ord.txt", "r")
real_data = f.readlines()

for i in range(len(real_data)):
    real_data[i] = real_data[i][:-1]

searched_word = "po00y"
# searched_word = ["c","o","0","e","r"]

inWord = "poy"  # Letters in the word
inWord = list(inWord)  # Convert the string to a list of letter elements

notInWord = "cranemistfudgblh"  # Letters NOT in the word
notInWord = list(notInWord)  # Convert the string to a list of letter elements

specificLettersNotInWord = "00000"   # Specific letters not in certain position in word
specificLettersNotInWord = list(specificLettersNotInWord)

CertainLetter = "0"
countOfCertainLetter = 1

word_length = 5

# If length of the word is 5
l1 = "".join(searched_word[0])  # "W _ _ _ _ _"
l2 = "".join(searched_word[1])  # "_ O _ _ _ _"
l3 = "".join(searched_word[2])  # "_ _ R _ _ _"

l12 = "".join(searched_word[0:2])  # "W O _ _ _ _"
l123 = "".join(searched_word[0:3])  # "W O R _ _ _"

lastL = "".join(searched_word[-1])  # "_ _ _ _ _ E"
second2last = "".join(searched_word[-2])  # "_ _ _ _ L _"
third2last = "".join(searched_word[-3])  # "_ _ _ D _ _"

last2L = "".join(searched_word[-2:])  # "_ _ _ _ L E"
last3L = "".join(searched_word[-3:])  # "_ _ _ D L E"

### Filters the words by specifying positions of the included letters
##l1 = 0                     # "W _ _ _ _ _"
##l2 = 0                       # "_ O _ _ _ _"
##l3 =  0                      # "_ _ R _ _ _"
##
##l12 = 0                      # "W O _ _ _ _"
##l123 = 0                     # "W O R _ _ _"
##
##
##
##lastL = 0                   # "_ _ _ _ _ E"
##second2last = 0              # "_ _ _ _ L _"
##third2last = 0                    # "_ _ _ D _ _"
##
##last2L = 0                # "_ _ _ _ L E"
##last3L = 0                   # "_ _ _ D L E"

counterIN = 0
counterNOT = 0
lista = []
counter = 0
for i in range(len(real_data)):
    if len(real_data[i]) == word_length:
        # if 3 <= len(real_data[i]) <= word_length:
        for j in range(len(inWord)):
            if inWord[j] in real_data[i]:
                counterIN += 1
        for k in range(len(notInWord)):
            if notInWord[k] not in real_data[i]:
                counterNOT += 1
            # if notInWord[j] in real_data[i]:
            #     counterNOT += 1
        if counterNOT == len(notInWord) and counterIN == len(inWord):

            if "0" in l1 or real_data[i][0] == l1:
                if "0" in l2 or real_data[i][1] == l2:
                    if "0" in l3 or real_data[i][2] == l3:

                        if "0" in l12 or real_data[i][0:2] == l12:
                            if "0" in l123 or real_data[i][0:3] == l123:

                                if "0" in lastL or real_data[i][-1] == lastL:
                                    if "0" in second2last or real_data[i][
                                            -2] == second2last:
                                        if "0" in third2last or real_data[i][
                                                -3] == third2last:

                                            if "0" in last2L or real_data[i][
                                                    -2:] == last2L:

                                                if "0" in last3L or real_data[
                                                        i][-3:] == last3L:
                                                    
                                                    if specificLettersNotInWord[0] != real_data[i][0]:
                                                        if specificLettersNotInWord[1] != real_data[i][1]:
                                                            if specificLettersNotInWord[2] != real_data[i][2]:
                                                                if specificLettersNotInWord[3] != real_data[i][3]:
                                                                    if specificLettersNotInWord[4] != real_data[i][4]:

                                                                        if list(real_data[i]).count(CertainLetter) == countOfCertainLetter or CertainLetter == "0":


                                                                            lista.append(real_data[i])
                                                                            counter += 1

        counterIN = 0
        counterNOT = 0

# print(lista)
for i in lista:
    # if "r" in i:
    print(i)
print("Number of words: ", counter)
