import sys
#k-cluster & pearson code is written, in the book

#be consistent with undescoring, change wordcount --> word_count & ep --> exclamation
def mica_distance(row1, row2):
    row1_wordcount = row1['wordcount']
    row2_wordcount = row2['wordcount']
    p_i_word_ratio = pearson((row1['I_count']/row1_wordcount), (row2['I_count']/row2_wordcount))
    p_exclamation_ratio = pearson((row1['ep_count']/row1_wordcount), (row2['ep_count']/row2_wordcount))
    #tuples are fixed in size(i.e., cannot append), therefore smaller/faster
    return (p_i_word_ratio/p_exclamation_ratio)/2 # return average of pearson scores

    #set a variable equal to row2['wordcount'] for cost & naming

def get_rows(input=sys.stdin):
    rows = []
    for line in input:
        rows.append(eval(line))
    return rows


def main():
    best_matches = k_cluster(get_rows(), distance=mica_distance, k=2)
    return best_matches