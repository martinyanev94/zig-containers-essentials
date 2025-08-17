import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample labeled data
data = [("I love cats", 1),
        ("Dogs are great", 1),
        ("I hate the rain", 0),
        ("Cats are annoying", 0)]

# Prepare input and output
X = []
y = []
for sentence, label in data:
    words = sentence.lower().split()
    vecs = [model.wv[word] for word in words if word in model.wv]
    if vecs:  # Keep only sentences with valid word vectors
        X.append(np.mean(vecs, axis=0))  # Average the word vectors
        y.append(label)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# Train a logistic regression model
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

# Make predictions
predictions = classifier.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")
