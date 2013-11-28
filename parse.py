import sys, re, utilities
from bs4 import BeautifulSoup

SENTENCE_SPLITTER = re.compile(r"([\.\?!]+)").finditer #splits text into sentences
WORD_SPLITTER = re.compile(r"(\w+)").finditer #splits sentence into words
EP_FINDER = re.compile(r"\!")
ELLIPSIS_FINDER = re.compile(r"\.{3,}")
FIRST_PERSON_SINGULAR_PRONOUNS = set(("i", "i'm", "i've", "i'll", "i'd", "me", "my", "mine"))

def calculate_feature_vector(post):
    words = make_wordcount_dict(post)
    total_words = 0
    for word in words:
        total_words += words[word]
    
    word_frequency_vector = utilities.generate_hashed_feature_vector(words)
    normalized_word_frequency_vector = normalize_word_frequency_vector(word_frequency_vector, total_words)

    I_count = int((count_i(words)/float(total_words))*100)
    exclamation_count, ellipsis_count = count_punctuation(post)
    exclamation_count = int((exclamation_count/float(total_words))*100)
    ellipsis_count = int((ellipsis_count/float(total_words))*100)
    average_sentence_length = find_average_sentence_length(post)

    style_feature_vector = [total_words, average_sentence_length, I_count, exclamation_count, ellipsis_count]
    feature_vector = style_feature_vector + normalized_word_frequency_vector 
    return feature_vector

def normalize_word_frequency_vector(frequency_vector, total_words):
    minimum_value = sorted(frequency_vector)[0]
    maximum_value = sorted(frequency_vector)[-1]
    spread = maximum_value - minimum_value

    normalized_word_frequency_vector = []
    for item in frequency_vector:
        normalized_item = int(((item-minimum_value)/float(spread+.001))*total_words)
        normalized_word_frequency_vector.append(normalized_item)
    return normalized_word_frequency_vector

def comparator(x,y):
    if x[1] < y[1]:
        return 1
    if x[1] > y[1]:
        return -1
    else:
        return cmp(x[0], y[0])

def count_i(words_dict):
    total = 0
    for word in words_dict:
        if word in FIRST_PERSON_SINGULAR_PRONOUNS:
            total += words_dict[word]
    return total 

def count_punctuation(sample):
    ep_count = len(EP_FINDER.findall(sample))
    ellipsis_count = len(ELLIPSIS_FINDER.findall(sample))
    return ep_count, ellipsis_count

def find_average_sentence_length(sample):
    #regular expressions for lexical analysis
    #maybe make more efficient with one pass through the string
    beginning = 0
    sentences = []
    for match in SENTENCE_SPLITTER(sample):
        sentence = sample[beginning:match.start()]
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

def make_wordcount_dict(post):
    token_list = normalize(post)
    wordcount = {}

    for token in token_list:
        wordcount[token] = wordcount.get(token, 0) + 1
    return wordcount

def normalize(text): 
    text = utilities.normalize(text).encode("utf8")
    word_list = text.lower().split()

    clean_list = []
    for word in word_list:
        word = word.strip("?.,_;\":!'-")
        clean_list.append(word)
    return clean_list

def open_file(input_blog):
    f = open(input_blog, 'rb')
    input_blog = f.read()
    f.close()
    return input_blog

def print_by_frequency(words):
    for k in sorted(words.iteritems(), cmp=comparator):
        print k[0], k[1]

def process_one_blog(filename):
    list_of_posts = separate_posts(filename)
    for post in list_of_posts:
        post = post.replace("urlLink", "[[LINK]]")
        feature_vector = calculate_feature_vector(post)
        index = filename.rfind("/")
        shortened_filename = filename[index+1:]
        print repr((feature_vector, shortened_filename, post))

def separate_posts(input_blog):
    post_list = []
    soup = BeautifulSoup(open_file(input_blog))
    sections = soup.find_all('post')
    for section in sections:
        post = section.contents[0].strip()
        if not post: #avoids empty posts
            continue
        post_list.append(post)
    return post_list

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
