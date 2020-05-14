# pip install spacy 
# conda install -c conda-forge spacy
# python -m spacy download en_core_web_sm

import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")

doc1 = open("process.txt", "r")
doc1Txt = doc1.read()

doc = nlp(doc1Txt)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)


#perform sentiment analysis
from textblob import TextBlob
#opinion = TextBlob("EliteDataScience.com is dope.")
opinion = TextBlob("I love EliteDataScience.com.")
sentiment = opinion.sentiment
polarity = opinion.sentiment.polarity
print(sentiment)
print(polarity)
 
 #Get the numeric score of the document
emotion = "negative"
 #If it's more than 0.5, consider the emotion to be positive
if(opinion.sentiment.polarity >= 0.5):
	emotion = "positive"
print("Document is: " + emotion)