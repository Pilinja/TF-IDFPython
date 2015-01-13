__author__ = 'Mateusz'

from collections import Counter
from math import log

firstDoc = 'The game of life is a game of everlasting learning.'
secondDoc = 'The unexamined life is not worth living.'
thirdDoc = 'Never stop learning.'
ignoredChar = "."

# split documents

def splitDoc(doc):

    allDoc = ''

    for i in doc:
        i = i.lower()
        for j in i:
            allDoc = allDoc + j

    allDoc = allDoc.replace(ignoredChar, " ")
    # print(allDoc)
    return allDoc

docs = (firstDoc, secondDoc, thirdDoc)
splitDoc(docs)

# TF

def termFrequency(doc):

    docSplit = doc.lower().split()
    docDict = Counter(docSplit)
    docLength = len(docSplit)

    for key, value in docDict.iteritems():
        value = float(value) / docLength
        docDict[key] = value

    return docDict


# IDF

def inverseDocumentFrequency(word, docs):

    numOfDocs = len(docs)
    numDocWithWord = 0

    for doc in docs:
        if word.lower() in doc.lower().split():
            numDocWithWord = numDocWithWord + 1

    if numDocWithWord > 0:
        return 1.0 + log(float(numOfDocs) / numDocWithWord)
    else:
        return 1.0

def idfForDoc(docs):

    arrayOfResults = []
    for doc in docs:

        docSplit = doc.lower().split()
        docDict = Counter(docSplit)

        for key, value in docDict.iteritems():
            value = inverseDocumentFrequency(key, docs)
            docDict[key] = value

        arrayOfResults.append(docDict)
    return arrayOfResults

# TF-IDF

def tfidf(doc, docs):

    tf = termFrequency(doc)
    idf = idfForDoc(docs)

    docSplit = doc.lower().split()
    docDict = Counter(docSplit)

    arrayOfResults = []
    for i in range(0, 3):
        idfTemporary = idf[i]
        for key, value in docDict.iteritems():
            value = float(tf[key]) * idfTemporary[key]
            docDict[key] = value

        arrayOfResults.append(docDict)

    return arrayOfResults



for i in (firstDoc, secondDoc, thirdDoc):
    tfidf(i, docs)
    print(tfidf(i, docs))


