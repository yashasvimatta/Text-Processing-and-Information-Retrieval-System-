import os
curr_dir = os.getcwd()
corpusroot = os.path.join(curr_dir, 'US_Inaugural_Addresses')
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import Counter
import os
import math
query_tf = Counter()
document_vectors = {}
query_vector = {}
porter_stemmer = PorterStemmer()
document_file_lengths = Counter()
document_tf = Counter()
total_documents = {} 
total_document_count = 0
def preprocess(doc):
    tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
    tokens = tokenizer.tokenize(doc)
    stop_words = stopwords.words('english')
    preprocessed_tokens =[]
    for x in tokens:
        if x not in stop_words:
            stemmed_token = porter_stemmer.stem(x)
            preprocessed_tokens.append(stemmed_token)
    return preprocessed_tokens

def getidf(term):
    stemmed_term = porter_stemmer.stem(term.lower())
    # print(f"Document Frequency for : {term,document_tf[stemmed_term]}")
    # print("total_document_count",total_document_count)
    if document_tf[stemmed_term] != 0:
        return math.log10(total_document_count / document_tf[stemmed_term])
    else:
        return -1
def getweight(filename, term):
    stemmed_term = porter_stemmer.stem(term.lower())
    document_word_count = total_documents[filename].get(stemmed_term, 0)
    if document_word_count > 0:
        tf = 1 + math.log10(document_word_count)
        idf = getidf(stemmed_term)
        return tf * idf
    else:
        return 0
def vector(query_str):
    query_terms = preprocess(query_str)
    temp = Counter(query_terms)
    for term in temp:
        tf = 1 + math.log10(temp[term])
        temp[term] = tf
    qvl = math.sqrt(sum(tf**2 for tf in temp.values()))
    if qvl > 0:
        for term in temp:
            temp[term] /= qvl
    return temp
def query(query_str):
    query_vector = vector(query_str)
    cosine_similarities = {}
    for i in total_documents:
        docvec = document_vectors.get(i, Counter())
        dot_product = 0
        for term in query_vector:
            tvd = docvec.get(term, 0)
            product = query_vector[term] * tvd
            dot_product += product
        cosine_similarities[i] = dot_product
    max_sim = max(cosine_similarities, key=cosine_similarities.get)
    return max_sim, cosine_similarities[max_sim]
total_document_count = -1
for j in os.listdir(corpusroot):
        total_document_count += 1
        with open(os.path.join(corpusroot, j), "r", encoding='windows-1252') as file:
            document_text = file.read().lower()
        doc_term = preprocess(document_text)
        document_tf.update(set(doc_term))
        total_documents[j] = Counter(doc_term)
        
for k in total_documents:
    document_vectors[k] = Counter()
    vec_length = 0
    for term in total_documents[k]:
        tf_idf = getweight(k, term) 
        if tf_idf != -1:
            document_vectors[k][term] = tf_idf
            vec_length = vec_length+ tf_idf ** 2
for y in document_vectors:
    vec_length = math.sqrt(sum(tf_idf ** 2 for tf_idf in document_vectors[y].values()))
    if vec_length > 0:
        for term in document_vectors[y]:
            document_vectors[y][term] /= vec_length
# Test cases
print("%.12f" % getidf('children'))
print("%.12f" % getidf('foreign'))
print("%.12f" % getidf('people'))
print("%.12f" % getidf('honor'))
print("%.12f" % getidf('great'))
print("--------------")
print("%.12f" % getweight('19_lincoln_1861.txt','constitution'))
print("%.12f" % getweight('23_hayes_1877.txt','public'))
print("%.12f" % getweight('25_cleveland_1885.txt','citizen'))
print("%.12f" % getweight('09_monroe_1821.txt','revenue'))
print("%.12f" % getweight('05_jefferson_1805.txt','press'))
print("--------------")
print("(%s, %.12f)" % query("pleasing people"))
print("(%s, %.12f)" % query("war offenses"))
print("(%s, %.12f)" % query("british war"))
print("(%s, %.12f)" % query("texas government"))
print("(%s, %.12f)" % query("cuba government"))