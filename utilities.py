import mmh3

STOPWORDS = ['a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am', 'among', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'being', 'because', 'been', 'but', 'by', 'can', 'cannot', 'could', 'dear', 'did', 'do', 'does', 'either', 'else', 'ever', 'every', 'for', 'from', 'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers', 'him', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'least', 'let', 'like', 'likely', 'may', 'me', 'might', 'most', 'must', 'my', 'neither', 'no', 'nor', 'not', 'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our', 'own', 'rather', 'said', 'say', 'says', 'she', 'should', 'since', 'so', 'some', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'this', 'to', 'too', 'us', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet', 'you', 'your']

def generate_hashed_feature_vector(tokens):
    hashed_dict = {x:0 for x in range(50)} 

    filtered_tokens = [token for token in tokens if not token in STOPWORDS ]

    for token in filtered_tokens:
        hashed_token = mmh3.hash(token) % 50
        hashed_dict[hashed_token] = hashed_dict.get(hashed_token) + 1

    return hashed_dict.values()
def normalize(text):
    mapping = [ (u"\u2018", "'"),
                (u"\u2019", "'"),
                (u"\u2014", " "), 
                (u"\u2026", "...")]
    new_text = text

    for src, dst in mapping:
        new_text = new_text.replace(src, dst)
   
    return new_text