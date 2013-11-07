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
from bs4 import BeautifulSoup


def normalize(input_text):
    #strips out leading and trailing white space
    return input_text.strip()

def open_file(input_blog):
    f = open(input_blog, 'rb')
    input_blog = f.read()
    f.close()
    return input_blog

def separate_posts(input_blog):
    post_list = []
    blog = BeautifulSoup(open_file(input_blog))
    sections = blog.find_all('post')

    for section in sections:
        post = normalize(section.contents[0])
        post_list.append(post)
    return post_list


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

    posts = separate_posts(input_blog)

    for post in posts:
        I_count = count_i(post)
        EP_count = count_exclamation(post)
        word_count = count_words(post)
        print "Post #%d has %d instances of 'I', %d !'s, & %d words." % (posts.index(post), I_count, EP_count, word_count)
        print post, "\n"
              

main() 


