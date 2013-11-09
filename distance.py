import random, sys
def k_cluster(rows, distance, k):
    #Determine the minimum and maximum values for each point
    ranges=[(min([row[i] for row in rows]), max([row[i] for row in rows])) for i in range(len(rows[0]))]

    #Create k randomly placed centroids
    clusters=[[random.random * () * (ranges[i][1] - ranges[i][0]) + ranges[i][0] for i in range(len(rows[0]))] for j in range(k)]

    last_matches=None
    for t in range(100):
        print 'Iteration %d' % t
        best_matches = [[] for i in range(k)]

        #Find which centroid is closest for each row
        for j in range(len(rows)):
            row = rows[j]
            best_match = 0
            for i in range(k):
                d=distance(clusters[i], row)
                if d < distance(clusters[best_match], row): best_match = i
            best_matches[best_match].append(j)

        #If the results are the same as last time, this is complete
        if best_matches==last_matches:
            break
        last_matches = best_matches

        #Move the centroids to the average of their members
        for i in range(k):
            avgs = [0.0] * len(rows[0])
            if len(best_matches[i]) > 0:
                for row_id in best_matches[i]:
                    for m in range(len(rows[row_id])):
                        avgs[m] += rows[row_id][m]
                for j in range(len(avgs)):
                    avgs[j]/=len(best_matches[i])
                clusters[i] = avgs
    return best_matches

def pearson(x,y):
    n = len(x)
    vals = range(n)

    #Simple sums
    sum_x = sum([float(x[i]) for i in vals])
    sum_y = sum([float(y[i]) for i in vals])

    #Sum up the squares
    sum_x_Sq = sum([x[i] ** 2.0 for i in vals])
    sum_y_Sq = sum([y[i] ** 2.0 for i in vals])

    #Sum up the products
    product_sum = sum([x[i] * y[i] for i in vals])

    #Calculate Pearson score
    num = product_sum - ((sum_x * sum_y)/n)
    density =((sum_x_Sq - pow(sum_x, 2)/n) * (sum_y_Sq - pow(sum_y, 2)/n)) ** .5
    if density == 0:
        return 0
    r = num/density

    return r


def mica_distance(row1, row2):
    row1_word_count = row1['word_count']
    row2_word_count = row2['word_count']
    p_i_word_ratio = pearson((row1['I_count']/row1_word_count), (row2['I_count']/row2_word_count))
    p_exclamation_ratio = pearson((row1['exclamation_count']/row1_word_count), (row2['exclamation_count']/row2_word_count))
    return (p_i_word_ratio/p_exclamation_ratio)/2 # return average of pearson scores

def get_rows(input=sys.stdin):
    rows = []
    for line in input:
        rows.append(eval(line))
    return rows


"""
Good thing to do is to wrap parse.py's main() function body in a try, except block, and print exceptions to stderr, and then keep going
so with a try/except block, parse.py will put its barf into the toilet, keeping the living room clean for distance.py

and then you can look at the output to stderr to see what is happening
"""
def main():
    best_matches = k_cluster(get_rows(), distance=mica_distance, k=2)
    print best_matches

for pathname in sys.argv[1:]:
    try:
        sys.stderr.write("Distance now trying %s" % pathname)
        main()
    except Exception, e:
        sys.stderr.write(pathname)
        sys.stderr.write(": ")
        sys.stderr.write(str(e))
        sys.stderr.write("\n")

