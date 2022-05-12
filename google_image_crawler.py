import json
import shutil
import os
from bs4 import BeautifulSoup
from icrawler import Parser
from icrawler.builtin import GoogleImageCrawler
from datetime import datetime
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize




def clean_keywords(text:str, keywords:list) -> str:
    for w in keywords:
        text = text.replace( " "+w," ")
    return text
def clean_punc(text:str, punc:list) -> str:
    for w in punc:
        text = text.replace(w,"")
    return text


def remove_stopwords(text: str) -> str:
    stop_words = set(stopwords.words('english'))
 
    word_tokens = word_tokenize(text)
    
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    
    filtered_sentence = []
    
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence

# The text to analyze
# filename = 'data/chamounix_synopsis.txt'
filename = 'data/hmspinafore_synopsis.txt'
file = open(filename, 'r')
text = file.read()

# text cleanup
removed_words = ['Pinafore', 'Dick', 'Deadeye', 'Little Buttercup', 'Josephine', 'Porter', 'Joseph', 'Ralph']
removed_punc = ['\"',',','.','-']
text = clean_keywords(text, removed_words)
text = clean_punc(text, removed_punc)
text = remove_stopwords(text)
text = ' '.join(text)
text_list = text.split('*')
text_list = text_list[:10] # shortening output for debugging

remove_keywords = "-opera -sullivan -news -chorus -music -sheet -gilbert"

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
directory_name = 'images'+current_time
# shutil.rmtree('images')
os.mkdir(directory_name)

for s in text_list:
    print(s+"\n\n\n")
    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=1,
        downloader_threads=1,
        storage={'root_dir': directory_name})
    google_crawler.crawl(keyword=(s + remove_keywords), offset=0, max_num=4,
                        min_size=(0,0), max_size=None, file_idx_offset='auto')

