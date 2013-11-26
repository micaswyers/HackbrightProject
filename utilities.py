def normalize(text):
    mapping = [ (u"\u2018", "'"),
                (u"\u2019", "'"),
                (u"\u2014", " ") ]
    new_text = text

    for src, dst in mapping:
        new_text = new_text.replace(src, dst)
   
    return new_text