"""
Take in a blog
Split blog into posts (=samples)

For each post/sample
Create a list of feature scores based on: 1)words 2)first person singular pronouns 3)exclamation points

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
    exclamation_count = 0
    for token in tokens:
        words[token] = words.get(token, 0) + 1
        for character in token:
            if character == "!":
                exclamation_count += 1
    return words, exclamation_count

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
    #script, input_blog = sys.argv

    for input_blog in sys.argv[1:]:
        posts = separate_posts(input_blog)

        for post in posts:
            words, exclamation_count = make_wordcount_dict(post)

            I_count = count_i(words)

            total_words = 0

            for word in words:
                total_words += words[word]
            #may be more efficient to shorten key names, but clearer now
            # scores = {"word_count": total_words, "I_count": I_count, "exclamation_count": exclamation_count}
            # print repr(scores)

            scores = [total_words, I_count, exclamation_count]
            print repr(scores)

      

for pathname in sys.argv[1:]:
    try:
        sys.stderr.write("Now trying %s\n" % pathname)
        main()
    except Exception, e:
        sys.stderr.write(pathname)
        sys.stderr.write(": ")
        sys.stderr.write(str(e))
        sys.stderr.write("\n")

