import os
from os import path
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree


def get_org_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    current_chunk = []
    for i in chunked:
         if type(i) == Tree:
                 current_chunk.append([i])
    
    
    main_list = []
    for tree in current_chunk:
        obj = []
        if tree[0].label() == 'ORGANIZATION':
            for i in tree[0]:
                obj += [i[0]]
            main_list += [obj]

    tmp = []
    for i in main_list:
        st = ""
        for j in i:
            st += j
            st += " "
        st = st[0:len(st)-1]
        tmp.append(st)
    tmp_dict ={i:tmp.count(i) for i in set(tmp)}
    return tmp_dict

def get_dict(text_file_name):
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    text = open(path.join(d, text_file_name)).read()
    continuous_chunk = get_org_chunks(text)
    return continuous_chunk



if __name__ == '__main__':
    text_file_name = 'abs.txt'
    continuous_chunk = get_dict(text_file_name)


