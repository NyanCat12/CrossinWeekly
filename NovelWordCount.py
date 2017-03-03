import re
from collections import Counter

def NovelRe(Novel):
    content = open(Novel, 'r').readlines()
    words = []
    pattern = r'\b[a-zA-Z]+\b'
    for line in content:
        tmp = re.findall(pattern, line)
        for x in tmp:
            words.append(x)
    Count = Counter(words).most_common(100)
    return Count

def main():
    NovelList = ['a tale of two cities(双城记).txt', 'Aesop’s Fables(伊索寓言).txt', 'Jane Eyre(简·爱).txt', 'Oliver Twist(雾都孤儿(孤星血泪)).txt', 'Romeo and Juliet(罗蜜欧和朱丽叶).txt']
    for novel in NovelList:
        print ('Novel: '+novel+'\n'+'========================================')
        WordList = NovelRe(novel)
        i = 1
        for word in WordList:
            print (str(i) + '.'+'\t' + str(word[0]) + '\t' + str(word[1]))
            i += 1
        print ('\n')

if __name__ == '__main__':
    main()
