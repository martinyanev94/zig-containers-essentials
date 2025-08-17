pip install gensim
from gensim.models import Word2Vec

# Sample data: a small corpus of sentences
sentences = [["the", "cat", "sat", "on", "the", "mat"],
             ["the", "dog", "sat", "on", "the", "log"],
             ["cats", "and", "dogs", "are", "great", "pets"]]

# Train a Word2Vec model
model = Word2Vec(sentences, vector_size=10, window=2, min_count=1, workers=4)

# Get the vector for a word
vector = model.wv['cat']
print(vector)
