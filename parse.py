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

def function_words_per_post(some_text):
    some_text = normalize(some_text)
    tagged_text = nltk.pos_tag(nltk.word_tokenize(some_text))
    function_counter = 0
    #Looks for Part of Speech tags: articles, adpositions, conjunctions, aux. verbs, interjections, particples, "to", WH-determiners, WH-pronouns, WH-adverbs
    function_word_list = ["DT", "IN", "CC", "MD", "UH", "RP", "TO", "WDT", "WP", "WRB"]
    for post in tagged_text:
        if post[1] in function_word_list:
            # print post[0] <--Prints out all function words found in the post
            function_counter += 1

    return function_counter


def words_per_sentence(one_post):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(one_post) #creates a list of sentences 
    word_count_list = []
    for sentence in sentences: #for each sentence in the list
        sentence_words = sentence.split(" ") #creates a list of words in the sentence
        word_count = len(sentence_words)
        word_count_list.append(word_count)
    return word_count_list
        

def main():
    script, input_text = sys.argv

    open_file = open(input_text, 'rb')
    input_text = open_file.read()
    open_file.close()

    parser.feed(input_text)
    posts_list = parser.post_list

    post_scores = []
    
    counter = 1
    for post in posts_list:
        post = normalize(post)
        print "*******Post #%d: *********" % counter
        word_counts = words_per_sentence(post)
        function_words = function_words_per_post(post)

        word_count = 0
        for count in word_counts:
            word_count += count
        average_word_count = word_count/len(word_counts)
        print "Average # of words per sentence in a list: %r" % average_word_count
        print "# of function words per post: %d" % function_words

        post_scores.append((average_word_count, function_words))
        counter += 1

    print "AVERAGE WORD COUNT & # OF FUNCTION WORDS PER POST: ", post_scores


        
main()