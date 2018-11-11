from nltk.corpus import wordnet as wn
synonyms = []
x = (wn.synsets(input()))
for syn in x:
    for l in syn.lemmas():
        synonyms.append(l.name())

x = set(synonyms)
print (x)
