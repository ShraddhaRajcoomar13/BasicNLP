# NLP Processor

A comprehensive Natural Language Processing (NLP) pipeline that performs text cleaning, sentiment analysis, named entity recognition, and part-of-speech labeling on a collection of sentences.

## 📋 Overview

This project leverages the power of **spaCy** and **VADER Sentiment** to process natural language text through a modular `NLPProcessor` class. It reads sentences from a configuration file and outputs cleaned text, sentiment scores, extracted entities, and word-level grammatical labels.

## ✨ Features

- **Text Cleaning** – Normalizes and cleans raw input sentences
- **Sentiment Analysis** – Assigns sentiment scores using VADER
- **Named Entity Recognition (NER)** – Extracts entities (people, places, organizations, etc.) using spaCy
- **Part-of-Speech Labeling** – Labels each word with its grammatical role
- **Modular Design** – Encapsulated in a reusable `NLPProcessor` class

## 🛠️ Requirements

- Python 3.8+
- [spaCy](https://spacy.io/)
- [vaderSentiment](https://github.com/cjhutto/vaderSentiment)

### Install Dependencies

```bash
pip install spacy vaderSentiment
python -m spacy download en_core_web_sm
```

## 📁 Project Structure

```
.
├── main.py              # Entry point (the script provided)
├── NLP.py               # Contains the NLPProcessor class
├── config.py            # Contains the `sentences` list
└── README.md
```

### `config.py` Example

```python
sentences = [
    "Apple Inc. is looking to buy a startup in the UK for $1 billion.",
    "I absolutely love this product! It works great.",
    "The weather in New York is terrible today.",
]
```

### `NLP.py` — NLPProcessor Interface

The `NLPProcessor` class is expected to expose the following methods:

| Method | Description |
|--------|-------------|
| `clean_text(sentence)` | Returns a cleaned/normalized version of the sentence |
| `analyze_sentiment(sentence)` | Returns sentiment scores via VADER |
| `extract_entities(sentence)` | Returns named entities via spaCy |
| `label_word(sentence)` | Returns POS labels for words in the sentence |

## 🚀 Usage

Run the main script:

```bash
python main.py
```

### Sample Output

```
Cleaned Sentences:
apple inc. is looking to buy a startup in the uk for $1 billion.
i absolutely love this product! it works great.
the weather in new york is terrible today.

Sentiment Scores:
{'neg': 0.0, 'neu': 0.74, 'pos': 0.26, 'compound': 0.34}
{'neg': 0.0, 'neu': 0.29, 'pos': 0.71, 'compound': 0.85}
{'neg': 0.55, 'neu': 0.45, 'pos': 0.0, 'compound': -0.65}

Extracted Entities:
[('Apple Inc.', 'ORG'), ('UK', 'GPE'), ('$1 billion', 'MONEY')]
...

Word Labels:
[('apple', 'NOUN'), ('inc.', 'PROPN'), ...]
```

## 🔄 Workflow

The pipeline follows this sequential workflow for each sentence:

```
┌──────────────────┐
│  config.sentences│
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│   clean_text()   │  →  Remove noise, normalize casing
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ analyze_sentiment│  →  VADER polarity scores
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ extract_entities │  →  spaCy NER (PERSON, ORG, GPE...)
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│   label_word()   │  →  POS tagging (NOUN, VERB, ADJ...)
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Print Results   │
└──────────────────┘
```

### Step-by-Step Workflow

1. **Load Models** – spaCy's `en_core_web_sm` and VADER's `SentimentIntensityAnalyzer` are initialized.
2. **Instantiate Processor** – An `NLPProcessor` is created with both models injected.
3. **Read Sentences** – Sentences are pulled from `config.sentences`.
4. **Process Each Sentence**:
   - Clean the text
   - Analyze sentiment
   - Extract named entities
   - Label each word with its POS tag
5. **Output Results** – Results are printed to the console grouped by task.

## 🧩 Extending the Pipeline

To add a new processing step:

```python
nlp_processor.new_feature = [nlp_processor.your_method(s) for s in sentences]
```

And add a corresponding print block:

```python
print("New Feature:")
for item in nlp_processor.new_feature:
    print(item)
```

## 📝 Notes

- The spaCy model `en_core_web_sm` is a small English model — for higher accuracy, consider `en_core_web_md` or `en_core_web_lg`.
- VADER is particularly tuned for **social media text** and works well on short sentences.
- Ensure `config.py` is present with a defined `sentences` list before running.

## 📄 License

This project is provided as-is for educational and demonstration purposes.