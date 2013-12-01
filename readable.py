from readability.readability import Document
import urllib
import csv
from bs4 import BeautifulSoup
import os
from readability import ParserClient
from HTMLParser import HTMLParser
PC = ParserClient(os.getenv('READABILITY_API_TOKEN'))
H = HTMLParser()

def call_readability():
    post_list = []
    with open('blog/unique_links.csv') as csvfile:
        post_links = csv.reader(csvfile)
        for link in post_links:
            post_url = link[0]
            post_dict = make_post_dict(post_url)
            if post_dict:
                post_list.append(post_dict)
    return post_list

def make_post_dict(post_url):
    parser_response = PC.get_article_content(post_url)
    post_dict = {}
    if parser_response.content.get('content'):
        post_dict['title'] = parser_response.content.get('title')
        post_dict['content'] = parser_response.content.get('content')
        post_dict['url'] = parser_response.content.get('url')
        post_dict['excerpt'] = parser_response.content.get('excerpt')
        post_dict['word_count'] = parser_response.content.get('word_count')
        post_dict['domain'] = parser_response.content.get('domain')
    return post_dict
        
            

#probably don't need these: 
# def parse_page():
#     with open('blog/links.csv') as csvfile:
#         post_links = csv.reader(csvfile)
#         counter = 1
#         for row in post_links:
#             post_url = row[0]
#             html_doc = urllib.urlopen(post_url).read()
#             readable_html = Document(html_doc).summary().encode("utf8")
#             content = BeautifulSoup(readable_html).get_text().encode("utf8")
#             readable_title = Document(html_doc).title().encode("utf8")
#             if "Page not found" not in readable_title:
#                 write_to_xml(counter, post_url, readable_title, readable_html)
#             counter += 1

# def write_to_xml(counter, post_url, readable_title, content):
#     f = open(r'wpblogs/blog%s.xml' % counter, 'w')
#     f.write("<url>%s</url> <title>%s</title> <post>%s</post>" % (post_url, readable_title, content))
#     # f.write("<post>%s</post>" % content)
