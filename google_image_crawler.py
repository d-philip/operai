import shutil
import os
from collections import defaultdict
from six.moves.urllib.parse import urlencode
from icrawler import ImageDownloader
from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler, GoogleFeeder
from datetime import datetime
import json

# Overwrite feeder to set global variable with search term (keyword)
class UrlFeeder(GoogleFeeder):
    def feed(self, keyword, offset, max_num, language=None, filters=None):
        base_url = 'https://www.google.com/search?'
        self.filter = self.get_filter()
        filter_str = self.filter.apply(filters, sep=',')
        for i in range(offset, offset + max_num, 100):
            self.signal.set(current_keyword=keyword)
            params = dict(
                q=keyword,
                ijn=int(i / 100),
                start=i,
                tbs=filter_str,
                tbm='isch')
            if language:
                params['lr'] = 'lang_' + language
            url = base_url + urlencode(params)
            self.out_queue.put(url)
            self.logger.debug('put url to url_queue: {}'.format(url))

# Overwrite downloader to save image URLs and keywords to JSON file
class UrlDownloader(ImageDownloader):
    images = []
    
    def process_meta(self, task):
        if task['file_url']:
            self.images.append({'image_url': task['file_url'], 'text': self.signal.get('current_keyword')})
            self.signal.set(image_url_list=self.images)
            # if self.reach_max_num:
            with open('data/image_urls.json', 'w') as file:
                json.dump({'images': self.signal.get('image_url_list')}, fp=file, indent=1)

# Version of image crawl that saves image URLS and keywords to JSON file
def image_url_crawl():
    image_crawl(downloader=UrlDownloader, feeder=UrlFeeder)

def clean_keywords(text:str, keywords:list) -> str:
    for w in keywords:
        text = text.replace( " "+w," ")
    return text

def image_crawl(downloader=ImageDownloader, feeder=GoogleFeeder):
    # The text to analyze
    filename = 'data/chamounix_synopsis.txt'
    # filename = 'data/test.txt'
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
    directory_name = 'images/'
    if os.path.isdir(directory_name):
        shutil.rmtree('images')
    os.mkdir(directory_name)

    i = 0
    for s in text_list:
        print(s+"\n\n\n")
        save_path = directory_name+str(i)
        if not os.path.isdir(save_path):
            os.mkdir(save_path)
            
        google_crawler = GoogleImageCrawler(
            downloader_cls=downloader,
            feeder_cls=feeder,
            feeder_threads=1,
            parser_threads=1,
            downloader_threads=1,
            storage={'root_dir': save_path})
        google_crawler.crawl(keyword=(s + remove_keywords), offset=0, max_num=4,
                            min_size=(0,0), max_size=None, file_idx_offset='auto')
        i+=1

if __name__ == "__main__":
    image_url_crawl()