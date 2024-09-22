import nltk
nltk.download('punkt_tab')

from textblob import TextBlob
from newspaper import Article

url="https://www.icis.com/chemicals-and-the-economy/2024/09/chinas-economy-risks-heading-into-recession-as-producer-prices-enter-deflation/"
article=Article(url)

article.download()
article.parse()
article.nlp()

text=article.summary
print(text)

blob= TextBlob(text)
sentiment= blob.sentiment.polarity
print(sentiment)