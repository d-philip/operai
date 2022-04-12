# Imports the Google Cloud client library
from google.cloud import language_v1

# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
filename = 'data/chamounix_synopsis.txt'
file = open(filename, 'r')
text = file.read()

document = language_v1.Document(
    content=text, type_=language_v1.Document.Type.PLAIN_TEXT
)
encoding_type = language_v1.EncodingType.UTF8

# Detects the sentiment of the text
sentiment_response = client.analyze_sentiment(
    request={"document": document, "encoding_type": encoding_type}
)
sentiment = sentiment_response.document_sentiment

#  Detects keywords in the text
entity_response = client.analyze_entities(
    request={"document": document, "encoding_type": encoding_type}
)

# Classifies text into a category or several categories
categories_response = client.classify_text(
    request={"document": document}
)
categories = categories_response.categories


# print("Text: {}".format(text))
print("Sentiment | Score: {}, Magnitude: {}".format(sentiment.score, sentiment.magnitude))
for entity in entity_response.entities:
    print('=' * 20)
    print('name: {0}'.format(entity.name))
    print('type: {0}'.format(entity.type))
    print('metadata: {0}'.format(entity.metadata))
    print('salience: {0}'.format(entity.salience))
print('=' * 20)
print("Categories: {}".format(categories))