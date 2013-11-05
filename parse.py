"""
Takes in XML blog document
Splits into posts 
Adds each post to a list



"""

import sys
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.post = False
        self.post_list = []
    def handle_starttag(self, tag, attrs):
        print tag
        if tag == "post":
            self.post = True
    def handle_endtag(self, tag):
        self.post = False
    def handle_data(self, data):
        if self.post == True:
            print data
            self.post_list.append(data)


parser = MyHTMLParser()


#Not actually using this right now
def convert(input_text):
    text = BeautifulSoup(input_text)


def main():
    script, input_text = sys.argv

    open_file = open(input_text, 'rb')
    input_text = open_file.read()
    open_file.close()

    parser.feed(input_text)
    print parser.post_list

main()