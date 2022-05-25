import shutil
import os
from blob_test import get_speech_parts
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
def image_url_crawl(filename, num_images):
    image_crawl(filename, downloader=UrlDownloader, feeder=UrlFeeder, num_images=num_images)

def clean_keywords(text:str, keywords:list) -> str:
    for w in keywords:
        text = text.replace( " "+w," ")
    return text

# Crawl images for pre-cleaned text
def image_crawl_nouns(filename, num_images):
    directory_name = 'images/'
    data_file = 'data/image_urls.json'
    
    if os.path.isdir(directory_name):
        shutil.rmtree('images')
    os.mkdir(directory_name)
    if os.path.isfile(data_file):
        os.remove(data_file)
        
    text_list = get_speech_parts(filename)
    remove_keywords = "-opera -sullivan -news -chorus -music -sheet -gilbert -newspaper -paper -notes -shirt -tshirt -clothing -libretto -act"

    i = 0
    for s in text_list:
        if s == []:
            continue
        query = ''
        for item in s:
            query += item+' '
        print('*'*30+'\n'+query+'\n'+'*'*30)
        
        save_path = directory_name+str(i)
        if not os.path.isdir(save_path):
            os.mkdir(save_path)
            
        google_crawler = GoogleImageCrawler(
            downloader_cls=UrlDownloader,
            feeder_cls=UrlFeeder,
            feeder_threads=4,
            parser_threads=4,
            downloader_threads=4,
            storage={'root_dir': save_path})
        google_crawler.crawl(keyword=(query + remove_keywords), offset=0, max_num=num_images,
                            min_size=(0,0), max_size=None, file_idx_offset='auto')
        i+=1

def image_crawl(filename, downloader=ImageDownloader, feeder=GoogleFeeder, num_images=4):
    # The text to analyze
    # filename = 'data/hmspinafore_libretto.txt'
    # filename = 'data/test.txt'
    file = open(filename, 'r')
    text = file.read()

    # text cleanup
    removed_words = ['Pinafore', 'Dick', 'Deadeye', 'Little Buttercup', 'Josephine', 'Porter', "Joseph", "Ralph"]
    text = clean_keywords(text, removed_words)
    text = text.replace('\"','') # removing quotes
    text_list = text.split('*')
    text_list = text_list[:10] # shortening output for debugging

    remove_keywords = "-opera -sullivan -news -chorus -music -sheet -gilbert -newspaper -paper -notes -shirt -tshirt -clothing -libretto -act"

    now = datetime.now()
    directory_name = 'images/'
    data_file = 'data/image_urls.json'
    if os.path.isdir(directory_name):
        shutil.rmtree('images')
    os.mkdir(directory_name)
    if os.path.isfile(data_file):
        os.remove(data_file)

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
        google_crawler.crawl(keyword=(s + remove_keywords), offset=0, max_num=num_images,
                            min_size=(0,0), max_size=None, file_idx_offset='auto')
        i+=1

if __name__ == "__main__":
    image_crawl_nouns(filename='data/chamounix_synopsis.txt', num_images=4)