import sys, re, csv
from bs4 import BeautifulSoup
from string import punctuation
SENTENCE_SPLITTER = re.compile(r"([\.\?!]+)").finditer #splits text into sentences
WORD_SPLITTER = re.compile(r"(\w+)").finditer #splits sentence into words
FIRST_PERSON_SINGULAR_PRONOUNS = set(("i", "i'm", "i've", "i'll", "i'd", "me", "my", "mine"))

def calculate_feature_vector(post):
    exclamation_count = count_exclamation_points(post)
    words = make_wordcount_dict(post)
    I_count = count_i2(words)
    average_sentence_length = find_average_sentence_length(post)

    total_words = 0
    for word in words:
        total_words += words[word]
    feature_vector = [total_words, I_count, exclamation_count, average_sentence_length] 
    feature_vector = [feature+0.001 for feature in feature_vector] #prevents divide-by-0 errors
    return feature_vector
    
def count_exclamation_points(sample):
    #replace for-loop with RE
    exclamation_count = 0
    for character in sample:
        if character == "!":
            exclamation_count += 1
    return exclamation_count

def count_i2(words):
    total = 0
    for word in words:
        stripped_word = word.strip(punctuation)
        if stripped_word.lower() in FIRST_PERSON_SINGULAR_PRONOUNS:
            total += words[word]
    return total 

def find_average_sentence_length(sample):
    #regular expressions for lexical analysis
    #maybe make more efficient with one pass through the string
    beginning = 0
    sentences = []
    for match in SENTENCE_SPLITTER(sample):
        sentence = sample[beginning:match.start()]
        # punctuation = sample[match.start():match.end()]
        sentences.append(sentence)
        beginning = match.end()
    total_words = 0
    for sentence in sentences:
        total_words += len([word for word in WORD_SPLITTER(sentence)])
    if len(sentences) == 0:
        average_sentence_length = len(sample.split())
    else:
        average_sentence_length = total_words/len(sentences)
    return average_sentence_length

def make_wordcount_dict(sample):
    words = {}
    word_list = sample.split()
    for word in word_list:
        words[word] = words.get(word, 0) + 1
    return words

def open_file(input_blog):
    f = open(input_blog, 'rb')
    input_blog = f.read()
    f.close()
    return input_blog

def separate_posts(input_blog):
    #separates into posts & returns posts in a list
    post_list = []
    soup = BeautifulSoup(open_file(input_blog))
    sections = soup.find_all('post')

    for section in sections:
        post = section.contents[0].strip()
        post_list.append(post)
    return post_list

def process_one_blog(filename):
    list_of_posts = separate_posts(filename)

    for post in list_of_posts:
        feature_vector = calculate_feature_vector(post)
        index = filename.rfind("/")
        shortened_filename = filename[index+1:]
        print repr((feature_vector, shortened_filename, post))

if __name__ == "__main__":
    for pathname in sys.argv[1:]:
        try:
            # sys.stderr.write("Now trying %s\n" % pathname)
            process_one_blog(pathname)
        except Exception, e:
            sys.stderr.write(pathname)
            sys.stderr.write(": ")
            sys.stderr.write(str(e))
            sys.stderr.write("\n")
