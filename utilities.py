import mmh3
import csv
import os
from readability import ParserClient
from HTMLParser import HTMLParser
PC = ParserClient(os.getenv('READABILITY_API_TOKEN'))
H = HTMLParser()

STOPWORDS = ['a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am', 'among', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'being', 'because', 'been', 'but', 'by', 'can', 'cannot', 'could', 'dear', 'did', 'do', 'does', 'either', 'else', 'ever', 'every', 'for', 'from', 'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers', 'him', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'least', 'let', 'like', 'likely', 'may', 'me', 'might', 'most', 'must', 'my', 'neither', 'no', 'nor', 'not', 'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our', 'own', 'rather', 'said', 'say', 'says', 'she', 'should', 'since', 'so', 'some', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'this', 'to', 'too', 'us', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet', 'you', 'your']

def add_post_dicts_to_csv(list_of_post_dictionaries):
    #writes all important data to CSV file to be used for calculating feature vectors without hitting Readability API
    with open('post_dictionaries.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter="\n")
        writer.writerow(list_of_post_dictionaries)

def call_readability():
    post_list = []
    with open('blogscraper/links_from_wp.csv') as csvfile:
        post_links = csv.reader(csvfile)
        for link in post_links:
            post_url = link[0]
            post_dict = make_post_dict(post_url)
            if post_dict:
                post_list.append(post_dict)
    add_post_dicts_to_csv(post_list)
    return post_list

def generate_hashed_feature_vector(tokens):
    hashed_dict = {x:0 for x in range(50)} 

    filtered_tokens = [token for token in tokens if not token in STOPWORDS ]

    for token in filtered_tokens:
        hashed_token = mmh3.hash(token) % 50
        hashed_dict[hashed_token] = hashed_dict.get(hashed_token) + 1
    return hashed_dict.values()

def make_post_dict(post_url):
    parser_response = PC.get_article_content(post_url)
    post_dict = {}
    if parser_response.content.get('content') and parser_response.content.get('word_count') != 0:
        post_dict['title'] = parser_response.content.get('title')
        post_dict['content'] = parser_response.content.get('content')
        post_dict['url'] = parser_response.content.get('url')
        post_dict['excerpt'] = parser_response.content.get('excerpt')
        post_dict['word_count'] = parser_response.content.get('word_count')
        post_dict['domain'] = parser_response.content.get('domain')
    return post_dict
    
def normalize(text):
    mapping = [ (u"\u2018", "'"),
                (u"\u2019", "'"),
                (u"\u2014", " "), 
                (u"\u2026", "...")]
    new_text = text
    for src, dst in mapping:
        new_text = new_text.replace(src, dst)
    return new_text




