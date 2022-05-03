import shutil
import os
from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler
from datetime import datetime



def clean_keywords(text:str, keywords:list) -> str:
    for w in keywords:
        text = text.replace( " "+w," ")
    return text

# The text to analyze
# filename = 'data/chamounix_synopsis.txt'
filename = 'data/hmspinafore_synopsis.txt'
file = open(filename, 'r')
text = file.read()

# text cleanup
removed_words = ['Pinafore', 'Dick', 'Deadeye', 'Little Buttercup', 'Josephine', 'Porter', "Joseph", "Ralph"]
text = clean_keywords(text, removed_words)
text = text.replace('\"','') # removing quotes
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

