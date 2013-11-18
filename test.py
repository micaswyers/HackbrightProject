import sys, csv

def make_filenames_list():
    filenames = []
    for pathname in sys.argv[1:]:
        filenames.append([pathname])
    return filenames

def print_to_csv(filenames_list):
    f = open('blog_info.csv', 'wb')
    writer=csv.writer(f)
    writer.writerows(filenames_list)

def main():
    print_to_csv(make_filenames_list())

main()