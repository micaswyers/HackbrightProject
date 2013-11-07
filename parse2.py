"""
Take in a blog
Split blog into posts (=samples)

For each posts
Create a list of feature scores based on: 1)I 2) ! 3) # of words per post

Assemble list of feature scores for each sample (posts for all blogs)
Run K-means clustering
Recommend based on k-means clustering results
"""

import sys
# from HTMLParser import HTMLParser
from bs4 import beautifulsoup


# class MyHTMLParser(HTMLParser):
#     def __init__(self):
#         HTMLParser.__init__(self)
#         self.post = False
#         self.post_list = []
#     def handle_starttag(self, tag, attrs):
#         print "Encountered a start tag:", tag
#         if tag == "post":
#             self.post = True
#     def handle_endtag(self, tag):
#         print "Encountered an end tag: ", tag
#         self.post = False
#     def handle_data(self, data):
#         print "Encountered data: ", data
#         if self.post == True:
#             self.post_list.append(data)


# parser = MyHTMLParser()

def normalize(input_text):
    #strips out leading and trailing white space
    return input_text.strip()

def open_file(input_blog):
    f = open(input_blog, 'rb')
    input_blog = f.read()
    f.close()
    return input_blog

def separate_posts(input_blog):
    parser.feed(input_blog)
    list_of_posts = parser.post_list
    return list_of_posts

def count_i(sample):
    i_counter = 0
    list_of_words = sample.split()
    list_of_i_forms = ["I","I'M", "I'LL", "I'VE", "I'D"]
    for word in list_of_words:
        if word.upper() in list_of_i_forms:
            i_counter += 1
    return i_counter

def count_exclamation(sample):
    ep_counter = 0
    for letter in sample: 
        if letter == "!":
            ep_counter += 1
    return ep_counter

def count_words(sample):
    return len(sample.split())


def main():
    script, input_blog = sys.argv
    
    one_blog = open_file(input_blog)
    list_of_posts = separate_posts(one_blog)

    for each_post in list_of_posts:
        post = normalize(each_post)
        I_count = count_i(post)
        EP_count = count_exclamation(post)
        word_count = count_words(post)
        print "Post #%d has %d instances of 'I', %d !'s, & %d words." % (list_of_posts.index(each_post), I_count, EP_count, word_count)
        print post, "\n"
              

main() 


