"""
Takes in XML blog document
Splits into posts 
Adds each post to a list

Cleans each post (removes escapes)
Assigns (x,y) to each post (word length, sentence length)
Run k-means algorithm on all blog scores to give average? (Or just average)
"""

import sys, nltk
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

    counter = 1
    

    for post in post_list:
        post = normalize(post)
        # print "Post #%d: "%counter, nltk.pos_tag(nltk.word_tokenize(post))
        tagged_text = nltk.pos_tag(nltk.word_tokenize(post))
        function_counter = 0
        for post in tagged_text:
            if post[1] == "IN":
                function_counter += 1

        print "Number of function words in Post #%r: " %counter, function_counter
        if counter == 10:
            break
        counter += 1

        
main()