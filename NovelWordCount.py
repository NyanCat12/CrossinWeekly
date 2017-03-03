import re
from collections import Counter

def NovelRe(Novel):
    content = open(Novel, 'r').read().lower()
    words = []
    pattern = r"(?<!')\b[a-zA-Z]{2}[a-zA-Z]+\b"
    tmp = re.findall(pattern, content)
    DropList = ['you','don','mer','for','jul','its','his','with','elecbook','classics','charlotte','bront','aesop','fables','dickens','tale','and','the','that','was']
    for word in DropList:
        tmp = [x for x in tmp if x!=word]
    for x in tmp:
        words.append(x)
    Count = Counter(words).most_common(100)
    return Count

def WordListToWordDict(WordList):
    Dict = {}
    for word in WordList:
        Dict[word[0]] = word[1]
    return Dict

def FullWordList(OldList, AddDict):
    for key in AddDict:
        OldList.append(key)
    NewList = list(set(OldList))
    return NewList

def Output():
    NovelList = ['a tale of two cities(双城记).txt', 'Aesop’s Fables(伊索寓言).txt', 'Jane Eyre(简·爱).txt', 'Oliver Twist(雾都孤儿(孤星血泪)).txt', 'Romeo and Juliet(罗蜜欧和朱丽叶).txt']
    for novel in NovelList:
        print ('Novel: '+novel+'\n'+'========================================')
        WordList = NovelRe(novel)
        i = 1
        for word in WordList:
            print (str(i) + '.'+'\t' + str(word[0]) + '\t' + str(word[1]))
            i += 1
        print ('\n')

def Freq(Dict):
    WordSum = 0
    for key in Dict:
        WordSum += Dict[key]
    for key in Dict:
        Dict[key] = Dict[key]/WordSum
    return Dict

def Style():
    NovelList = ['a tale of two cities(双城记).txt', 'Aesop’s Fables(伊索寓言).txt', 'Jane Eyre(简·爱).txt', 'Oliver Twist(雾都孤儿(孤星血泪)).txt', 'Romeo and Juliet(罗蜜欧和朱丽叶).txt']
    Dict = {}
    for novel in NovelList:
        Dict[novel[:-4]] = Freq(WordListToWordDict(NovelRe(novel)))
    WordList = []
    for key in Dict:
        WordList = FullWordList(WordList, Dict[key])
    return WordList, Dict
        
def WordVector(WordList, Dict):
    vector = [x*0 for x in range(len(WordList))]
    for index in range(len(WordList)):
        try:
            vector[index] = Dict[WordList[index]]
        except:
            vector[index] = 0
    return vector

def NovelVector():
    WordList, Dict = Style()
    NovelVectorDict = {}
    for key in Dict:
        NovelVectorDict[key] = WordVector(WordList, Dict[key])
    return NovelVectorDict

if __name__ == '__main__':
    Output()
    print (NovelVector())
