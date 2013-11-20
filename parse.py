import sys, re, csv
from bs4 import BeautifulSoup
SENTENCE_SPLITTER = re.compile(r"([\.\?!]+)").finditer
WORD_SPLITTER = re.compile(r"(\w+)").finditer

def count_i(words):  #use Postgres full-text search 
    first_person_singular_pronouns = ["I", "I'm", "I've", "I'll", "I'd", "Me", "i", "i'm", "i've", "i'll", "i'd", "me"] #Me + punctuation? 
    total = 0
    for pronoun in first_person_singular_pronouns:
        total += words.get(pronoun, 0)
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
    tokens = sample.split()
    tokens = [token.strip("!?.;-") for token in tokens]
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
    soup = BeautifulSoup(open_file(input_blog))
    sections = soup.find_all('post')

    for section in sections:
        post = section.contents[0].strip()
        post_list.append(post)

    return post_list

def process_one_blog(filename):
    posts = separate_posts(filename)

    for post in posts:
        words, exclamation_count = make_wordcount_dict(post)
        I_count = count_i(words)
        total_words = 0
        average_sentence_length = find_average_sentence_length(post)

        for word in words:
            total_words += words[word]
        scores = [total_words, I_count, exclamation_count, average_sentence_length] 
        scores = [x+0.001 for x in scores] #prevents divide-by-0 errors
        index = filename.rfind("/")
        shortened_filename = filename[index+1:]

        print repr((scores, shortened_filename, post))


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
