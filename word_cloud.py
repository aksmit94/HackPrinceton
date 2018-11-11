import os
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def get_word_cloud(text_file):
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    # Read the whole text.
    text = open(path.join(d, text_file)).read()
    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    
    
if __name__ == '__main__':
    text_file = 'abs.txt'
    get_word_cloud(text_file)