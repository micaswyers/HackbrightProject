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
        print "*******Post #%d: *********" % counter
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        sentences = tokenizer.tokenize(post)
        for sentence in sentences:
            print "This is a whole sentence: ", sentence
            sentence_words = sentence.split(" ")
            print "This is how many words are in the sentence: ", len(sentence_words)

        if counter == 10:
            break
        counter += 1
"""
    
#looking for function words in a post
    for post in post_list:
        post = normalize(post)
        tagged_text = nltk.pos_tag(nltk.word_tokenize(post))
        function_counter = 0
        #Looks for POS tags: articles, adpositions, conjunctions, aux. verbs, interjections, particples, "to", WH-determiners, WH-pronouns, WH-adverbs
        function_word_list = ["DT", "IN", "CC", "MD", "UH", "RP", "TO", "WDT", "WP", "WRB"]
        for post in tagged_text:
            if post[1] in function_word_list:
                function_counter += 1

        print "Number of function words in Post #%r: " %counter, function_counter
        counter += 1
"""


        
main()