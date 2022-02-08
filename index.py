from dataset import data

# Task 1

class Word:
    def __init__(self, line):
        self.pageID = line[0]
        self.wordID = line[1]
        self.wordIDonpage = line[2]
        self.coord = line[3:5]
        self.wordHeight = round(float(line[6]))
        self.wordWidth = line[5]
        self.text = line[7]

    def __str__(self):
        return str(self.pageID) + ',' +str(self.wordID) + ',' + str(self.wordIDonpage) + ',' + str(self.coord) + ',' + str(self.wordHeight) + ',' + str(self.wordWidth) + ',' + str(self.text)

#Task 2

dictionary = {}
for line in data[1:]:
    dictionary[line[1]] = Word(line)   

#Task 3

wordheights = []
for j in range(len(data)-1):
    wordheights.append(dictionary[str(j)].wordHeight)

unique_wordheights = set(wordheights)

lists_of_same_height = []
dict_same_height = {}
list_of_lengths_of_same_height = []

for k in unique_wordheights:
    for l in range(len(data)-1):
        if l == 0:
            pass
        else:
            if dictionary[str(l)].wordHeight == k:
                lists_of_same_height.append(dictionary[str(l)].text)
                
    dict_same_height[k] = lists_of_same_height
    list_of_lengths_of_same_height.append(len(lists_of_same_height))