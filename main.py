from NLP import NLPProcessor
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spacy
import config


# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Initialize VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Initialize the NLPProcessor with spaCy and VADER
nlp_processor = NLPProcessor(nlp, analyzer)

sentences = config.sentences

nlp_processor.cleaned_sentences = [nlp_processor.clean_text(sentence) for sentence in sentences]
nlp_processor.sentiment_scores = [nlp_processor.analyze_sentiment(sentence) for sentence in sentences]
nlp_processor.entities = [nlp_processor.extract_entities(sentence) for sentence in sentences]
nlp_processor.labels = [nlp_processor.label_word(sentence) for sentence in sentences]

print("Cleaned Sentences:")
for sentence in nlp_processor.cleaned_sentences:
    print(sentence)

print("Sentiment Scores:")
for score in nlp_processor.sentiment_scores:
    print(f"{score}")
    
print("Extracted Entities:")
for entity in nlp_processor.entities:
    print(entity)
    
print("Word Labels:")
for label in nlp_processor.labels:
    print(label)