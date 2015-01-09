__author__ = 'Mateusz'

from collections import Counter

firstDoc = 'The game of life is a game of everlasting learning.'
secondDoc = 'The unexamined life is not worth living.'
thirdDoc = 'Never stop learning.'

allDoc = firstDoc, secondDoc, thirdDoc

# TF

def termFrequency(doc):

    docSplit = doc.lower().split()
    docDict = Counter(docSplit)
    docLength = len(docSplit)

    for key, value in docDict.iteritems():
        value = float(value) / docLength
        docDict[key] = value

    return docDict

for i in (firstDoc, secondDoc, thirdDoc):
    print(termFrequency(i))

# IDF