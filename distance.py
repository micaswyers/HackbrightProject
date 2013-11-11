import random, sys
def k_cluster(rows, distance, k):
    #Determine the minimum and maximum values for each attribute (!,I, # of words)
    ranges=[(min([row[i] for row in rows]), max([row[i] for row in rows])) for i in rows[0].keys()]

    # !-min = 5, !-max = 105 

    #Create k randomly placed centroids between ranges calculated above
    # clusters=[[random.random() * (ranges[i][1] - ranges[i][0]) + ranges[i][0] for i in range(len(rows[0]))] for j in range(k)]

    #list of dictionaries, each representing one centroid's values for !, I's, & word count
    clusters=[{rows[0].keys()[i]: random.random() * (ranges[i][1] - ranges[i][0]) + ranges[i][0] for i in range(len(rows[0]))} for j in range(k)]

    last_matches=None
    for t in range(100):
        print 'Iteration %d' % t
        best_matches = [[] for i in range(k)]

        #Find which centroid is closest for each row
        for j in range(len(rows)):
            row = rows[j]
            best_match = 0
            for i in range(k):
                d = distance(clusters[i], row)
                if d < distance(clusters[best_match], row): best_match = i
            best_matches[best_match].append(j)

        #If the results are the same as last time, this is complete
        if best_matches==last_matches:
            break
        last_matches = best_matches

        #Move the centroids to the average of their members
        for i in range(k):
            avgs = {key: 0.0 for key in rows[0].keys()} 
            if len(best_matches[i]) > 0:
                for row_id in best_matches[i]:
                    for m in rows[row_id].keys():
                        avgs[m] += rows[row_id][m]
                for key in avgs.keys():
                    avgs[key]/=len(best_matches[i])
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


def euclidean(dict1, dict2):
    sumSq = 0.0

    #adds up the squared distances
    for i in dict1.keys():
        sumSq += (dict1[i] - dict2[i]) ** 2

    #take the square root
    return (sumSq ** 0.5)


def get_rows(input=sys.stdin):
    rows = []
    for line in input:
        rows.append(eval(line))
    return rows

def main():
    best_matches = k_cluster(get_rows(), distance=euclidean, k=3)
    print best_matches

main()

# for pathname in sys.argv[1:]:
#     try:
#         sys.stderr.write("Distance now trying.")
#         main()
#     except Exception, e:
#         sys.stderr.write(pathname)
#         sys.stderr.write(": ")
#         sys.stderr.write(str(e))
#         sys.stderr.write("\n")

