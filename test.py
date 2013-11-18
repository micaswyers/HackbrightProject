import sys, csv

def make_filenames_list():
    filenames = []

    for pathname in sys.argv[1:]:
        index = pathname.rfind("/")
        shortened_pathname = pathname[index+1:]
        filenames.append(shortened_pathname)

    return filenames

def print_filenames_to_csv(filenames_list):
    f = open('blog_info.csv', 'wb')
    writer=csv.writer(f, delimiter = "\n")
    writer.writerow(filenames_list)

def main():
    print_filenames_to_csv(make_filenames_list())
    
def print_posts_to_csv(posts_list):
    pass
    

main()