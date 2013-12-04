CATABLOG
=================

CATABLOG is a web application that clusters and recommends blog text based on writing style. It uses Python, the Readability API, ScraPy, BeautifulSoup, SciPy, NumPy, SQLAlchemy, Postgresql Flask, JS/Jquery, HTML, and Rickshaw. 

##Scraping blogs with Blogscraper
######(blogspider.py in blogscraper/)

Crawls the links for trending tags on *wordpress.com/tags*. The spider then scrapes the links to recently-posted blogs and saves them in a CSV file.

##Building a corpus and clustering
######(build_corpus.py, calculate_feature_vector.py, utilities.py)

###Calculating the Feature Vector

A call is made for each scraped link to the Readability API which returns salient data from the page. The script extracts the text using BeautifulSoup and calculates a feature vector based on stylistic characteristics such as average sentence length and number of exclamation points. 

####Zipf's law

To calculate the word frequencies, the script exploits [Zipf's law](http://en.wikipedia.org/wiki/Zipf's_law), which states that the frequency of any word is inversely proportional to its rank in the frequency table. The script uses MurmurHash3 to employ a ["hashing trick"](http://en.wikipedia.org/wiki/Hashing_trick) before performing a word count. This essentially forces common words into the same "buckets," and distributes the uncommon word counts evenly throughout the vector. 

###K-means clustering

The script uses SciPy's k-means clustering algorithm to cluster feature vectors for all posts. Prior to clustering, NumPy's standard deviation function is called to whiten features evenly.

###Saving to CSV files

The relevant post data (including the feature vectors), parent blog information, and cluster centroid data are saved to three separate CSV files in seed_data/.

##Seeding the database
######(seed.py, seed_data/, & model.py)

Every time seed.py is called, it uses SQLAlchemy to recreate a Postgresql database and insert the data into three data tables: posts, blogs, and clusters. 

##Web Framework
######(app.py, model.py, calculate_feature_vector.py, utilities.py)

The web framework is built using Flask. The script uses AJAX to send the user-input URL to the server and call the route which works backend magic. Using the URL, a call is made to the Readability API, and a feature vector is calculated on the returned data. Then the script calculates the nearest (using Euclidean distance) centroid from those stored in the database, identifying the cluster of posts most similar to the user-input post. Posts from that cluster are then selected at random from the database and returned in JSON.

##Displaying Data

######(main.html, myjs.js, stats.js)

After receiving the JSON data from the server, the script displays the relevant title, excerpt, and link for the post. The stylistic features for both the sample post (from the user) and the recommended post (pulled from the database) are displayed side-by-side in both a stats table and a graph (created with Rickshaw).
