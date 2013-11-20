def normalize(text):
    print "%r"%text
    mapping = [ (u"\u2018", "'"),
                (u"\u2019", "'") ]
    new_text = text

    for src, dst in mapping:
        print "Replacing %r with %r"%(src, dst)
        new_text = new_text.replace(src, dst)
    print "%r"%new_text.encode("utf8")
   
    return new_text.encode ("utf8")