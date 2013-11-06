"""
Takes in XML blog document
Splits into posts 
Adds each post to a list

Cleans each post (removes escapes)
Assigns (x,y) to each post (word length, sentence length)
Run k-means algorithm on all blog scores to give average? (Or just average)
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
        if tag == "post":
            self.post = True
    def handle_endtag(self, tag):
        self.post = False
    def handle_data(self, data):
        if self.post == True:
            self.post_list.append(data)


parser = MyHTMLParser()


#Not actually using this right now
def convert(input_text):
    text = BeautifulSoup(input_text)

def normalize(input_text):
    input_text = input_text.strip()
    return input_text


def main():
    script, input_text = sys.argv

    open_file = open(input_text, 'rb')
    input_text = open_file.read()
    open_file.close()

    parser.feed(input_text)
    
    post_list = parser.post_list
    one_post = normalize(post_list[0])
    print "%r" % one_post


    counter = 0
    for post in post_list:
        post = normalize(post)
        print "Post #%d: " %counter, post
        counter += 1
main()