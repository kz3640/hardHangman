def genPos(word, letter):
    #number of combinations the letter can be placed in
    numPos = 2**(word.count("_"))
    #return values
    retval = []
    for i in range(numPos):
        binnum = bin(i).replace("0b","").zfill(word.count("_"))
        newstr = word
        for j in range(len(binnum)):
            if binnum[j:j+1] == "1":
                n = find_nth(word, "_", j+1)
                newstr2 = newstr[:n] + letter + newstr[n+1:]
                newstr=newstr2
        retval.append(newstr)
    return retval

def find_nth(haystack, needle, n):
    cnt = 0
    for i in range(len(haystack)):
        if haystack[i:i+1] == needle:
            cnt += 1
            if cnt == n:
                return i
    return "help"

def similar(word1, word2):
    #word1 is similar to word2 if the letters in word1 and word2
    #are the same, given that _ is a wildcard
    for i in range(len(word1)):
        if word1[i:i+1] != "_" and word1[i:i+1] != word2[i:i+1]:
            return False
    return True

def main():
    bigtext = open('6letterwords.txt', 'r')
    bigtextline = bigtext.readline()
    currentWord = "______"
    wordList = bigtextline.split()
    while currentWord.count("_") > 0:
        print("The current word is: " + currentWord)
        ui = raw_input("Guess a letter: ")
        print(ui)
        possibilities = genPos(currentWord, ui)
        possibilities.sort(key=lambda x: x.count(ui), reverse = True)
        buckets=[[] for _ in range(len(possibilities))]
        for i in range(len(possibilities)):
            stop = len(wordList)
            j = 0
            while j < stop:
                if similar(possibilities[i],wordList[j]):
                    buckets[i].append(wordList[j])
                    wordList = wordList[:j]+wordList[j+1:]
                    stop -= 1
                    j -= 1
                j += 1

        bigBucketInfo = max(enumerate(buckets), key = lambda tup: len(tup[1]))

        wordList = bigBucketInfo[1]
        currentWord = possibilities[bigBucketInfo[0]]

if __name__ == "__main__":
    main()
