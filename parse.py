"""
Takes in XML blog document
Splits into posts 
Adds each post to a list
Returns list
"""

import sys
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup

class MyHTMLParser(HTMLParser):
    def handle_start(self, tag, attrs):
        print "Encountered start tag: ", tag
    def handle_endtag(self, tag):
        print "Encountered end tag: ", tag
    def handle_data(self, data):
        print "Encountered some data: ", data

parser = MyHTMLParser()



def convert(input_text):
    text = BeautifulSoup(input_text)


def main():
    script, input_text = sys.argv

    open_file = open(input_text, 'rb')
    input_text = open_file.read()
    open_file.close()

    parser.feed(input_text)

main()