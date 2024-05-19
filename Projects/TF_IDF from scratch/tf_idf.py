import pandas
from tools import *

doc_a = "the man went out for a walk"
doc_b = "the children sat around the fire"

bow_a = doc_a.split(' ')
bow_b = doc_b.split(' ')

uq = set(bow_a).union(set(bow_b))

na = dict.fromkeys(uq,0)
for w in bow_a:
    na[w] += 1

nb = dict.fromkeys(uq,0)
for w in bow_b:
    nb[w] += 1

tf_a = tf(na,bow_a)
tf_b = tf(nb,bow_b)

idf = idf([na,nb])

tf_idf_a = tf_idf(tf_a,idf)
tf_idf_b = tf_idf(tf_b,idf)

print(pandas.DataFrame([tf_idf_a,tf_idf_b]))
