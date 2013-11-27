import mmh3



def generate_feature_vector(tokens):
    hashed_dict = {x:0 for x in range(50)} 

    for token in tokens:
        hashed_token = mmh3.hash(token) % 50
        hashed_dict[hashed_token] = hashed_dict.get(hashed_token) + 1


    return hashed_dict.values()