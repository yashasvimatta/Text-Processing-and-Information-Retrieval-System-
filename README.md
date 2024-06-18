# Text-Processing-and-Information-Retrieval-System-


## Overview
This project involves the implementation of a simple search engine using Python. The search engine reads a corpus of 30 inaugural addresses of U.S. Presidents, processes the text, and responds to queries by returning the document that best matches the query based on TF-IDF vectors and cosine similarity.

## Features
- **Text Processing:** Converts text to lower case, tokenizes, removes stopwords, and stems the words.
- **TF-IDF Vector Calculation:** Calculates Term Frequency-Inverse Document Frequency vectors for each document.
- **Query Processing:** Processes query strings and computes cosine similarity between the query vector and document vectors to find the best match.
- **NLTK Library:** Utilizes the Natural Language Toolkit (NLTK) for text processing.

## Installation

To run this project, you need Python 3.5.1 or later. The project also requires the installation of Jupyter and NLTK.

1. Install Jupyter:
   ```bash
   pip install jupyter
   pip install notebook

2. Install NLTK:
   ```bash
   pip install nltk
   
After installing NLTK, you need to download the necessary datasets:
   ```bash
   import nltk
   nltk.download()

### Key Functions
- `getidf(token)`: Returns the inverse document frequency of a token.
- `getweight(filename, token)`: Returns the TF-IDF weight of a token in a specified document.
- `query(qstring)`: Returns the filename and score of the document that best matches the query.

## Dataset
The dataset includes 30 .txt files, each containing one of the U.S. Presidential inaugural addresses. The files are located in the `US_Inaugural_Addresses` directory.

## License
This project is licensed under the terms of the MIT license.
