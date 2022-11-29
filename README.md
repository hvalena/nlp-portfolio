# nlp-portfolio
This repository is Hannah Valena's portfolio for CS 4395.001: Human Language Technologies, taken in Fall 2022 with Dr. Karen Mazidi.

## 🌱 Assignment 0: Getting Started
You can find an [Overview of NLP here](Overview-Of-NLP.pdf)! 

## 📝 Assignment 1: Text Processing with Python
### Program overview
This program reads and processes a csv file of employee data. It makes the information more standardized by using
some basic regex expressions and text processing.  
  
You can find the [assignment description here](Homework01-TextProcessing/portfolio-component-1-instructions.pdf), the
[Homework 1 folder here](Homework01-TextProcessing), and the [Homework 1 python script here](Homework01-TextProcessing/homework1-hcv180000.py).
### How to run the program
You can run this program either from a terminal or in an IDE, like PyCharm:
#### Running from the terminal
1. Navigate to the directory where this program is stored
2. Run: `$ python3 homework1-hcv180000.py data/data.csv`  

#### Running from an IDE (PyCharm)
1. Open the directory where this program is stored in your IDE
2. Add a new run/debug configuration with the path to [homework1-hcv180000.py](Homework01-TextProcessing/homework1-hcv180000.py) as 
the script path and [data/data.csv](Homework01-TextProcessing/data/data.csv) as a parameter
3. Select this newly created run configuration and run the program  

### Strengths & weaknesses of Python for text processing
Python's NLTK provides many libraries that have many text processing functionalities, which makes Python a good choice
of language for NLP. Python syntax is also very similar to the English language, and it almost feels like writing
pseudocode. This makes Python pretty intuitive to learn and use. I haven't noticed any weaknesses yet for text 
processing with Python, but I know that Python's dynamic typing can lead to slower performance times than other
languages.  

### What I learned in this assignment
In this assignment, I learned how to use sysarg, open/read files regardless of OS, write classes, and use regex in
Python. I also learned that pickle files make it easier to save data structures to a file.  
  
## 🚀 Assignment 2: Exploring NLTK
This assignment explores Python's Natural Language Toolkit using Google Colab Notebook.  
  
You can find the [assignment description here](Homework02-ExploringNLTK/portfolio-component2-instructions.pdf), the [Homework 2 folder here](Homework02-ExploringNLTK), and the [Homework 2 Google Colab notebook here](Homework02-ExploringNLTK/cs4395_001_assignment2_hcv180000.ipynb).  
  
## ❓ Assignment 3: Word Guessing Game
This assignment uses Python and NLTK features to explore a text file and create a word guessing game!  
  
You can find the [assignment description here](Homework03-GuessingGame/cs4395-001-assignment3-instructions.pdf), the [Homework 3 folder here](Homework03-GuessingGame), the [Homework 3 Python script here](Homework03-GuessingGame/homework3-hcv180000.py), and a [screenshot of a sample run (word = chordae) here](Homework03-GuessingGame/homework3-sample-run-chordae.png).
  
### How to run the program
You can run this program either from a terminal or in an IDE, like PyCharm:
#### Running from the terminal
1. Navigate to the directory where this program is stored
2. Run: `$ python3 homework3-hcv180000.py anat19.txt`  

#### Running from an IDE (PyCharm)
1. Open the directory where this program is stored in your IDE
2. Add a new run/debug configuration with the path to [homework3-hcv180000.py](Homework03-GuessingGame/homework3-hcv180000.py) as 
the script path and [anat19.txt](Homework03-GuessingGame/anat19.txt) as a parameter
3. Select this newly created run configuration and run the program

## 🌐 Assignment 4: Exploring WordNet 
This assignment explores WordNet and SentiWordNet to extract and analyze synsets.  
  
You can find the [assignment description here](Homework04-WordNet/homework4-instructions.pdf), the [Homework 4 folder here](Homework04-WordNet), and the [Homework 4 Google Colab notebook here](Homework04-WordNet/cs4395_001_assignment4_hcv180000.ipynb).

## 🇮🇹 Assignment 5: Ngrams
This assignment creates ngrams from training data and builds language models from the created ngrams. Language models for 3 languages are built
from the training data: English, French, and Italian. Then, these models are used to predict the language of each line in the testing data. 
The accuracy of the models is calculated by comparing a predictions file with a solutions file. I collaborated with [Ryan Dimaranan](https://github.com/ryannd) for this
assignment, and the accuracy of our predictions was 98.33%.  
  
This assignment was split into 2 programs. The first program builds the language models and pickles them, and the second program uses these
training models to predict languages in the testing data. We split the assignment into 2 programs to save time on predictions
since NLTK ngrams() in program 1 is very slow.  
  
You can find the:
- [assignment description here](Homework05-NgramLanguagePrediction/cs4395-001-assignment5-instructions.pdf)
- [Homework 5 folder here](Homework05-NgramLanguagePrediction)
- [training, testing, predictions, and solutions datasets here](Homework05-NgramLanguagePrediction/ngrams/ngram_files)
- [training models created from program 1 here](Homework05-NgramLanguagePrediction/ngrams/dicts)
- [program 1 here](Homework05-NgramLanguagePrediction/ngrams/program_1.py)
- [program 2 here](Homework05-NgramLanguagePrediction/ngrams/program_2.py)
- [more info about ngrams here](Homework05-NgramLanguagePrediction/ngrams_narrative.pdf)

### How to run the program
You can run this program either from a terminal or in an IDE, like PyCharm:
#### Running from the terminal
1. Navigate to the directory where the programs are stored
2. Run: `$ python3 program_1.py`
3. Run: `$ python3 program_2.py`

#### Running from an IDE (PyCharm)
1. Open the directory where this program is stored in your IDE
2. Add a new run/debug configuration with the path to [program_1.py](Homework05-NgramLanguagePrediction/ngrams/program_1.py) as 
the script path.
3. Select this newly created run configuration and run program 1
4. Repeat steps 2-3 for [program_2.py](Homework05-NgramLanguagePrediction/ngrams/program_2.py)

## 🌌 Assignment 6: Web Crawler
This assignment crawls a starter URL for related links, scrapes text from these links, cleans the scraped text, finds keywords from the cleaned text,
and builds a knowledge base for the key terms using the cleaned text. I collaborated with [Ryan Dimaranan](https://github.com/ryannd) for this project, and the topic we chose was space.  
  
You can find the:
- [assignment description here](Homework06-WebCrawler/WebCrawler-Assignment-Instructions.pdf)
- [Homework 6 folder here](Homework06-WebCrawler)
- [program here](Homework06-WebCrawler/web_crawler.py)
- [knowledge base creation document here](Homework06-WebCrawler/WebCrawler-KnowledgeBase.pdf)  
  
### How to run the program
You can run this program either from a terminal or in an IDE, like PyCharm:
#### Running from the terminal
1. Navigate to the directory where the programs are stored
2. Run: `$ python3 web_crawler.py`

#### Running from an IDE (PyCharm)
1. Open the directory where this program is stored in your IDE
2. Add a new run/debug configuration with the path to [web_crawler.py](Homework06-WebCrawler/web_crawler.py) as 
the script path.
3. Select and run this newly created run configuration

## 📓 Assignment 7: Syntax Parsing
This assignment explores syntax parsing with phrase structure grammar(PSG)/constituency parsers, dependency parsers, and semantic role labeling(SRL)/shallow semantic parsers.  
  
You can find the:
- [assignment description here](Homework07-SyntaxParsing/sentence-parsing-instructions.pdf)
- [assignment work here](Homework07-SyntaxParsing/syntax-parsing-hcv180000.pdf)

## 📃 Assignment 8: ML using Sklearn
This assignment explores machine learning using sklearn by attempting authorship attribution:  identifying the author of a document given samples of authors' work.  
  
You can find the:
- [assignment description here](Homework08-AuthorAttribution/asg8-instructions.pdf)
- [google colab notebook here](Homework08-AuthorAttribution/cs4395_001_asg8_hcv180000.ipynb)
