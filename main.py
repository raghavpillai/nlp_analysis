import nltk
import time
from nltk.stem import WordNetLemmatizer, PorterStemmer

# Download necessary data for nltk
nltk.download('wordnet')

# Define a set of words to process
words = ["running", "jumps", "better", "best", "run", "jumped", "happily", "happier"] * 50  # Extend the list to have more data

# Initialize lemmatizer and stemmer
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

def lemmatize_words(words):
    return [lemmatizer.lemmatize(word) for word in words]

def stem_words(words):
    return [stemmer.stem(word) for word in words]

# Running the trials
lemmatization_times = []
stemming_times = []

for _ in range(10000):
    start_time = time.time()
    lemmatize_words(words)
    lemmatization_times.append(time.time() - start_time)

    start_time = time.time()
    stem_words(words)
    stemming_times.append(time.time() - start_time)

# Calculate average times
avg_lemmatization_time = sum(lemmatization_times) / len(lemmatization_times)
avg_stemming_time = sum(stemming_times) / len(stemming_times)

# Print results
print(f"Average Lemmatization Time: {avg_lemmatization_time} seconds")
print(f"Average Stemming Time: {avg_stemming_time} seconds")
