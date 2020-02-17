#Variable Declaration & Initialization
text        = "I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn’t really happy."
wordHash    = {}

#Splitting text into Array of Words
words       = text.split(' ')

#If word exist in Word Hash THEN Increment its Count, ELSE Start its Sount at 1
def checkForWord(search, words):
    if search in wordHash:
        wordHash[search] += 1
    else:
        wordHash[search] = 1

#Iterate through Word Array to determine its Sount
for word in words:
    checkForWord(word, words)

#Display Words and their Counts
print(wordHash)
    