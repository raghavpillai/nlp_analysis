# Lemmatization vs Stemming Performance Comparison
This Python script is designed to compare the performance of lemmatization and stemming in terms of processing speed. It runs each process 10,000 times on a predefined set of words and calculates the average time taken for each method. 

## Overview
**Lemmatization** and **Stemming** are two common approaches in natural language processing for reducing words to their base or root form. While they aim to achieve a similar goal, they use different methods:

- **Lemmatization**: This involves a more sophisticated analysis of the word to return its base or dictionary form (lemma!). It considers the context and part of speech to accurately identify the lemma.
- **Stemming**: This is a more heuristic process that chops off the ends of words in the hope of correctly transforming the word into its root form.

## Implications
The choice between lemmatization and stemming depends on the requirements of the specific application:
- **Accuracy**: Lemmatization generally provides more accurate results as it uses more informed analysis of the word.
- **Speed**: Stemming is often faster as it involves simpler string operations.
Our script aims to quantify the speed difference between these two approaches.

## How It Works
### Dependencies
The script uses the `nltk` (Natural Language Toolkit) library in Python. This library provides the necessary tools for text processing, including both lemmatization and stemming.

### Script Structure
1. **Initialization**: The script begins by importing necessary libraries and initializing the lemmatizer and stemmer.
2. **Word Set**: A predefined set of words is defined. These words are processed repeatedly in each trial.
3. **Processing Functions**: Two functions are defined - one for lemmatization (lemmatize_words) and one for stemming (stem_words).
4. **Performance Measurement**: The script runs each function 100 times and records the time taken for each trial.
5. **Average Time Calculation**: After completing the trials, the script calculates the average time taken by each method.
6. **Results**: The average times are printed in milliseconds for easy comparison.

### Usage
To use this script, simply run it in a Python environment after installing the nltk library from the requirements.txt. The script will automatically download the necessary nltk data and execute the trials.
