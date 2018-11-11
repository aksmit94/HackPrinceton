import urllib.request
import matplotlib.pyplot as plt
from word_cloud import get_word_cloud
from nltk.corpus import wordnet as wn
from wordcloud import WordCloud


def gen_syn(word):
    synonyms = []
    x = (wn.synsets(word))
    for syn in x:
        for l in syn.lemmas():
            synonyms.append(l.name())

    x = set(synonyms)
    return (x)

def count_words(words):       
    counts = {word: 0 for word in words}
    
    for word in counts:
        counts[word] = words.count(word)
    
    return counts

def internal_generate_tech(query, num_results):
    url_link = ('http://export.arxiv.org/api/query?search_query=all:' 
                + query + '&start=0&max_results=' + str(num_results))
    with urllib.request.urlopen(url_link) as url:
        data = url.read()

    data = data.decode("utf-8") 
    data = data.lower()
    data = data.replace('\n',' ')
    data = data.replace('$','')
    syn_list = gen_syn(query)

    for syn in syn_list:
	    data = data.replace(syn,'')

    data = data.split('summary>')

    s = ''

    for i in range(len(data) - 1):
        data[i] = data[i].replace('<', '')
        data[i] = data[i].replace('>', '')
        data[i] = data[i].replace('/', '')
        if (i % 2 == 1):
            s += data[i] + '\n'
    
    # # write to file
    # file = open('papers.txt','w')
    # file.write(s)

    # Scientific terms frequencies
    words = open('clean_list2.txt').readlines()

    for i in range(len(words)):
        words[i] = words[i].replace('\n','')
        words[i] = ' ' + words[i] + ' '

    counts = count_words(s)

    for word in list(counts):
        if(word == '' or counts[word] == 0):
            counts.pop(word)

    print(counts)

    wordcloud = WordCloud().generate_from_frequencies(counts)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")


def generate_text_tech(query):
    num_results = 1000
    internal_generate_tech(query, num_results)
    # get_word_cloud('papers.txt')
    
if __name__ == '__main__':
    query = 'homeless'
    generate_text_tech(query)