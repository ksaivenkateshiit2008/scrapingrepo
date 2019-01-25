from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString
import requests
from config import EXCLUDE_WORDS_LIST,HTML_TAG_NAMES_TO_IGNORE
from datastructure import MyDataStructure
import sys

class Scraper(object):
    def __init__(self):
        self.words_list = []

    def process_url(self, url):
        response = requests.get(url)

        soup = BeautifulSoup(
            response.text.encode('ascii','replace').decode('ascii'),
            "html.parser",
            from_encoding='utf-8'
            )

        self.extract_words(soup.find("body"))

    def extract_words(self, soupobj,
                      ignore_names=HTML_TAG_NAMES_TO_IGNORE,
                      exclude_words=EXCLUDE_WORDS_LIST
                      ):
        if not isinstance(soupobj, NavigableString):
            for child in soupobj.children:
                if isinstance(child, Tag):
                    if child.name.strip() not in ignore_names:
                        try:
                            words_list = child.getText().strip().lower().split()
                            for word in words_list:
                                if word and word not in exclude_words:
                                    self.words_list.append(str(word))
                        except:
                            pass
                        for child_tag in child.children:
                            self.extract_words(child_tag)



if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "python myparse.py <url_path> <number_of_max_occurences>"
        sys.exit(1)

    sobj = Scraper()
#    sobj.process_url("https://hiverhq.com/")
    sobj.process_url(sys.argv[1])
    sobj.words_list
    obj = MyDataStructure()
    for word in sobj.words_list:
        obj.insert(word)
    #obj.print_ds()
    print obj.get_max_n_elements(int(sys.argv[2]))