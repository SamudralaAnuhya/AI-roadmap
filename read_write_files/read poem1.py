# poem.txt contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your python program and
# find out words with maximum occurance.

repeat_words= {}

with open("/Users/anuhyasamudrala/Documents/python_exercise/poem.txt" , "r") as f:
    for line in f:
        words = line.split()
        for word in words:
            if word in repeat_words:
                repeat_words[word]+=1
            else:
                repeat_words[word]=1

print(repeat_words)

max_count = max(repeat_words.values())
print("max occurance of word is " , max_count)

for word,count in repeat_words.items():
    if count == max_count:
        print("maximum occurance of the word in the poem is ", word, "with the count", count)

