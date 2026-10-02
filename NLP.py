import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Initialize VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

class NLPProcessor:
    def __init__(self, nlp, analyzer):
        self.nlp = nlp
        self.analyzer = analyzer

    def clean_text(self, text):
        """
        Clean the input text by removing unwanted characters and formatting.
        """
        # Remove URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        # Remove special characters and numbers
        text = re.sub(r'\W', ' ', text)
        text = re.sub(r'\d', ' ', text)
        # Remove extra spaces
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    def label_word(self, text):
        doc = self.nlp(text)
        print(doc)
        lblz = []
        for token in doc:
            if token.pos_ in ["NOUN", "PROPN", "PRON"]:
                lblz.append("S")  # Subject
            elif token.pos_ in ["VERB", "AUX"]:
                lblz.append("V")  # Verb
            elif token.pos_ in ["ADJ", "ADV", "DET", "ADP"]:
                lblz.append("M")  # Modifier
            elif token.dep_ in ["dobj", "pobj", "obj"]:
                lblz.append("O")  # Object
        return lblz  # Return all labels

    def analyze_sentiment(self, text):
        """
        Analyze the sentiment of the input text using VADER.
        Returns a dictionary with sentiment scores.
        """
        sentiment_scores = {}
        sentiment_scores[text] = self.analyzer.polarity_scores(text)["compound"]
        return sentiment_scores

    def extract_entities(self, text):
        """
        Extract named entities from the input text using spaCy.
        Returns a list of entities with their labels.
        """
        doc = self.nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities