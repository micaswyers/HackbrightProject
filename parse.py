"""
Take in a blog
Split blog into posts (=samples)

For each post
Create a list of feature scores based on: 1)words/post 2)first person singular pronouns/post 3)exclamation points/post

Assemble list of feature scores for each sample (posts for all blogs)
Run K-means clustering
Recommend based on k-means clustering results
"""

import sys
from bs4 import BeautifulSoup

def count_i(words):
    first_person_singular_pronouns = ["I", "I'm", "I've", "I'll", "I'd", "Me", "i", "i'm", "i've", "i'll", "i'd", "me"]
    total = 0
    for pronoun in first_person_singular_pronouns:
        total += words.get(pronoun, 0)
    return total

def make_wordcount_dict(sample):
    words = {}
    tokens = sample.split()
    ep_count = 0
    for token in tokens:
        words[token] = words.get(token, 0) + 1
        for character in token:
            if character == "!":
                ep_count += 1
    return words, ep_count

def open_file(input_blog):
    f = open(input_blog, 'rb')
    input_blog = f.read()
    f.close()
    return input_blog

def separate_posts(input_blog):
    #separates into posts & returns posts in a list
    post_list = []
    blog = BeautifulSoup(open_file(input_blog))
    sections = blog.find_all('post')

    for section in sections:
        post = section.contents[0].strip()
        post_list.append(post)
    return post_list


def main():
    script, input_blog = sys.argv
    posts = separate_posts(input_blog)

    feature_scores = []
    for post in posts:
        words, ep_count = make_wordcount_dict(post)

        I_count = count_i(words)

        total_words = 0
        for word in words:
            total_words += words[word]
        scores = (total_words, I_count, ep_count)
        # print "Post #%d has: %d words, %d I's, & %d exclamation points" % (posts.index(post), scores[0], scores[1], scores[2])
        feature_scores.append(scores)

    #feature_scores is a list of tuples for the word-, I-, and !- counts for each post in the blog.


      

main() 


