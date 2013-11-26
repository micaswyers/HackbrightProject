from urllib2 import urlopen
from bs4 import BeautifulSoup
import json

def make_url_list():
    url_list = []
    while len(url_list) < 2:
        wordpress_soup = BeautifulSoup(urlopen("http://en.blog.wordpress.com/next/").read())
        url = wordpress_soup.find("a").contents[0]
        url = url[7:] #string-slicing to remove "http://"
        url_list.append(url)
    return url_list

def make_api_list(url_list):
    api_url_list = []
    for url in url_list:
        api_url = "https://public-api.wordpress.com/rest/v1/sites/%sposts" % url
        api_url_list.append(api_url)
    return api_url_list

def make_blog_list(api_list):
    dictionary_of_blogs = {} #key = url, value = dictionary of posts

    for api_url in api_list: #for every blog in the list of apis
        data = json.load(urlopen(api_url)) 

        blogs_post_dict = {} #key = post title, value = post content
        for post_dictionary in data["posts"]: #for every post-dictionary in the list "posts"
            if len(post_dictionary) != 0:
                post_title = post_dictionary["title"]
                post_content = post_dictionary["content"]
                blogs_post_dict[post_title] = post_content
        dictionary_of_blogs[api_url] = blogs_post_dict
    return dictionary_of_blogs

def main():
    url_list = make_url_list()
    api_list = make_api_list(url_list)
    blog_dict = make_blog_list(api_list)

    for value in blog_dict.values():
        print value

main()
#feed into api url 
#http://developer.wordpress.com/docs/api/1/get/sites/%24site/#apidoc-example
#example: https://public-api.wordpress.com/rest/v1/sites/savvyfreelancewriter.wordpress.com/posts
#base = "https://public-api.wordpress.com/rest/v1/sites/%s/posts"" % url in url_list <--array of bases
#posts_list = []
#for every item in base_list:
    #data = json.load(urlopen(item))
    #for item in data["posts"]:
        #posts_list.append(item["content"])

