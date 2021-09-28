import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line) #class that splits each word in the line

#Open dictionary and add into dictionary list
dic = open("Dictionary.txt") #Opens dictionary.txt

dictionary = [] #Empty dictionary

for line in dic  #Loops through the dictionary
    line = line.strip()
    dictionary.append(line) #Create dicitonary of the dictionary
dic.close()

#----- Linear Search -----
print("---Linear Search---")

file = open("Alicefirstchapter.txt")
line_num=0
for line in file:
    words = split_line(line)
    line_num += 1
    for word in words:
        i = 0
        while i < len(dictionary) and dictionary[i] != word.upper():
            i += 1
        if i < len(dictionary):
            continue
        else:
            print("Line",line_num,"possible misspelled word:",word)

file.close()

#----- Binary Search -----
print("---Binary Search---")

file = open("Alicefirstchapter.txt")
line_num=0

for line in file:
    words = split_line(line)
    line_num += 1
    for word in words:
        found = False
        lower_bound=0
        upper_bound=len(dictionary)-1
        while lower_bound < upper_bound and not found:
            middle_pos = int((lower_bound + upper_bound)/2)
            if dictionary[middle_pos] < word.upper():
                lower_bound = middle_pos+1
            elif dictionary[middle_pos] > word.upper():
                upper_bound = middle_pos
            else:
                found = True
        if not found:
            print("Line",line_num,"possible misspelled word:",word)

file.close()
