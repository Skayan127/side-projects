# f = open("myfile.txt", "x")

# final_textfile = ""

# original_string = "tbbt ("

# txt=".srt"

# number = list(range(1,280))

# # f = open("tbbt1.txt", "r")


# for i in range(len(number)):
#     file_name = original_string + str(number[i]) + ")" + txt
#     print(file_name)
#     f2 = open(file_name, "r")
#     string = f2.read()
#     string.encode('utf-8').strip()
#     # str = str(str, errors='replace')
#     # string = string.decode('unicode_escape').encode('utf-8')
#     # string = unicode(str, errors='replace')
    
#     f.write(string)

# f.close()
# f2.close()
f = open("you_complete.txt", "x")
end_file = ""
numberOfEpisodes = 261
number = list(range(numberOfEpisodes+1))
original_string = "tahm ("
txt=".srt"

import pysrt

for i in range(1,len(number)):
    file_name = original_string + str(number[i]) + ")" + txt
    # print("working 1")
    subs = pysrt.open(file_name,encoding='latin-1')
    # print("working 2")
    for sub in subs:
        temp1 = sub.text.replace("<i>","")
        temp1 = temp1.replace("</i>","")
        end_file += temp1 + "\n\n"
    end_file += ".......... ********** .........." + "\n\n"
    # print("working 3")
    f.write(end_file)
    # print("working 4")
    end_file = ""
    #print(file_name)

# f.close()

# f = open("you_complete.txt",'r')
# filedata = f.read()
# f.close()

# newdata = filedata.replace("</i>","rersadasdas")

# f = open("you_complete.txt", "w")
# f.write(newdata)
# f.close()
