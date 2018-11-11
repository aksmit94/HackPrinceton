import urllib.request
from word_cloud import get_word_cloud

def internal_generate(query, num_results):
    url_link = ('http://export.arxiv.org/api/query?search_query=all:' 
                + query + '&start=0&max_results=' + str(num_results))
    with urllib.request.urlopen(url_link) as url:
        data = url.read()
    data = data.decode("utf-8") 
    data = data.lower()
    data = data.replace('\n',' ')
    data = data.replace('$','')
    data = data.split('summary>')
    s = ''
    for i in range(len(data) - 1):
        data[i] = data[i].replace('<', '')
        data[i] = data[i].replace('>', '')
        data[i] = data[i].replace('/', '')
        if (i % 2 == 1):
            s += data[i] + '\n'
    
    # write to file
    file = open('papers.txt','w')
    file.write(s)


def generate_text(query):
    num_results = 100
    internal_generate(query, num_results)
    get_word_cloud('papers.txt')
    
if __name__ == '__main__':
    query = 'homeless'
    generate_text(query)