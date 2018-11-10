#This function takes a blob of text data and returns processed phrases.

def blobintophrases(textchunk):

    wordlist = []
    wordlst = []
    phraselist = []
    textchunk = textchunk.lower()
    wordlist = textchunk.split()
    texttemp = ""

    for elem in wordlist:
        elem2 = ""
        for i in elem:
            if i.isalpha():
                elem2 += i
        wordlst.append(elem2)


    if len(wordlst) < 5:
        for elem in range(len(wordlst)):
            texttemp += wordlst[elem] + " "
        texttemp = texttemp.rstrip()
        phraselist.append(texttemp)
        return phraselist

    if len(wordlst) >= 5:
        for numb in range(int(len(wordlst)/4)):
            num1 = numb * 4
            texttemp = ""
            texttemp += (wordlst[num1 - 5] + " " + wordlst[num1 - 4] + " " + wordlst[num1 - 3] + " " + wordlst[num1 - 2] + " " + wordlst[num1 - 1])
            phraselist.append(texttemp)

    return phraselist

## THE GHOST OF THE SHADOW ##