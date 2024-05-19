import math

# TF which is also called Term Frequency is used to calculate the commonality of a word in a specific document
def tf(wdict,bow):
    tf= {}
    count = len(bow)
    for k,v in wdict.items():
        tf[k] = v / float(count)
    
    return tf


# IDF which is abbreviation of Inverse Document Frequency is used to calculate the commonality of a word in a across all documents
def idf(docs):
    tf_idf = dict.fromkeys(docs[0].keys(),0)
    n = len(docs)
    for doc in docs:
        for w,v in doc.items():
            if v != 0:
                tf_idf[w] += 1
    
    for w,v in tf_idf.items():
        tf_idf[w] = math.log(n / float(v))
    
    return tf_idf


# Applying the TF-IDF formula which determines if the word is important or not by assigning higher weights for the important ones 
def tf_idf(tf,idf):
    tf_idf = {}
    for k,v in tf.items():
        tf_idf[k] = v * idf[k]
    
    return tf_idf
