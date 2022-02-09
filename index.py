from dataset import data
from statistics import *

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

#Task 4

largest_length = max(list_of_lengths_of_same_height)

list_of_unique_wordheights = list(unique_wordheights)

for i in range(len(list_of_lengths_of_same_height)):
    if largest_length == list_of_lengths_of_same_height[i]:
        height_of_mainbody = list_of_unique_wordheights[i]

mainbody = list_of_unique_wordheights[7]

#Task 5

#PART 1
dict_y_coords = {}

for word in dict_same_height[18]:
    for line in data:
        if line[7] == word:
            if line[4] not in dict_y_coords.keys():
                a = []
                dict_y_coords[line[4]] = a

for key in dict_y_coords.keys():
    b = []
    for line in data:
        if line[4] == key:
            b.append(line[7])
    dict_y_coords[key] = b

#PART 2

y_coords = []
for j in dict_y_coords.keys():
    y_coords.append(j)

list_of_distances_between_y_coords = []
for i in range(len(y_coords)-2):
    z = float(y_coords[i+1])-float(y_coords[i])
    list_of_distances_between_y_coords.append(z)

mean_distance = -1* sum(list_of_distances_between_y_coords)/len(list_of_distances_between_y_coords)
median_distance = median(list_of_distances_between_y_coords)
mode_distance = mode(list_of_distances_between_y_coords)

#Part 3

lines = []
for key in dict_y_coords.keys():
    a = dict_y_coords[key]
    #this is a list of all the words on the same line. Now need to find each word's line in the dataset, find its x coord and then order it.
    list_of_unordered_words_on_same_line = []
    for k in a:
        for line in data:
            if line[7] == k:
                list_of_unordered_words_on_same_line.append(line[3])
        lines.append(list_of_unordered_words_on_same_line)

list_of_sorted_words_xcoords_on_same_line = []
for line in lines:
    list_of_sorted_words_xcoords_on_same_line.append(sorted(line))

#Part 4

list_of_distances_between_x_coords = []
for line in list_of_sorted_words_xcoords_on_same_line:
    for j in range(len(line)-2):
        v = float(line[j+1]) - float(line[j])
        list_of_distances_between_x_coords.append(v)

mean_x_distance = mean(list_of_distances_between_x_coords)
median_x_distance = median(list_of_distances_between_x_coords)
mode_x_distance = mode(list_of_distances_between_x_coords)
