import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vowels = ('a', 'e', 'i', 'o', 'u')
    def countVowels(text):
        count = 0
        for c in text:
            if c in vowels:
                count += 1
        return count

    p = lambda text: countVowels(text) * 1.0 / len(text)
    new_list = map(p, wordList)
    pylab.hist(new_list, numBins)
    pylab.show()

    

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList, 10)
