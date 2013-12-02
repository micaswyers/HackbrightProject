import re, utilities
from bs4 import BeautifulSoup
from enchant.checker import SpellChecker

SENTENCE_SPLITTER = re.compile(r"([\.\?!]+)").finditer #splits text into sentences
WORD_SPLITTER = re.compile(r"(\w+)").finditer #splits sentence into words
EP_FINDER = re.compile(r"\!")
ELLIPSIS_FINDER = re.compile(r"\.{3,}")
FIRST_PERSON_SINGULAR_PRONOUNS = set(("i", "i'm", "i've", "i'll", "i'd", "me", "my", "mine"))
SPELLCHECKER = SpellChecker("en_US")

def calculate_feature_vector(post_dictionary):
    post_text = BeautifulSoup(post_dictionary['content']).get_text()
    url = post_dictionary['url']
    excerpt = post_dictionary['excerpt']
    title = post_dictionary['title']
    domain = post_dictionary['domain']
    total_words = post_dictionary['word_count']

    words = make_wordcount_dict(post_text)
    word_frequency_vector = utilities.generate_hashed_feature_vector(words)
    normalized_word_frequency_vector = normalize_word_frequency_vector(word_frequency_vector, total_words)

    I_count = int((count_i(words)/float(total_words))*1000)
    exclamation_count, ellipsis_count = count_punctuation(post_text)
    exclamation_count = int((exclamation_count/float(total_words))*1000)
    ellipsis_count = int((ellipsis_count/float(total_words))*1000)
    average_sentence_length = find_average_sentence_length(post_text)
    misspellings_count = int((count_misspellings(words)/float(total_words))*1000)

    style_feature_vector = [average_sentence_length, I_count, exclamation_count, ellipsis_count, misspellings_count]
    feature_vector = style_feature_vector + normalized_word_frequency_vector 
    return (feature_vector, url, title.encode("utf8"), excerpt.encode("utf8"), domain)

def count_i(words_dict):
    total = 0
    for word in words_dict:
        if word in FIRST_PERSON_SINGULAR_PRONOUNS:
            total += words_dict[word]
    return total 

def count_misspellings(words):
    misspellings = 0
    for word in words:
        if len(word) > 0 and SPELLCHECKER.check(word) == False:
            misspellings += 1
    return misspellings

def count_punctuation(sample):
    ep_count = len(EP_FINDER.findall(sample))
    ellipsis_count = len(ELLIPSIS_FINDER.findall(sample))
    return ep_count, ellipsis_count

def find_average_sentence_length(sample):
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
    text = re.sub(r"\.{2,}", " ", text)
    word_list = text.lower().split()
    clean_list = []
    for word in word_list:
        word = word.strip("?.,_;\":!'-*()")
        clean_list.append(word)
    return clean_list

def normalize_word_frequency_vector(frequency_vector, total_words):
    minimum_value = sorted(frequency_vector)[0]
    maximum_value = sorted(frequency_vector)[-1]
    spread = maximum_value - minimum_value
    normalized_word_frequency_vector = []
    for item in frequency_vector:
        normalized_item = int(((item-minimum_value)/float(spread+.001))*total_words)
        normalized_word_frequency_vector.append(normalized_item)
    return normalized_word_frequency_vector

