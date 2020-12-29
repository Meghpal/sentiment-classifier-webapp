import bs4
import re

from nltk.corpus import stopwords


def review_cleaner(review):

    review = bs4.BeautifulSoup(review, features="html.parser").text
    emoticons = re.findall(r"(?::|;|=)(?:-)?(?:\)|\(|D|P)", review)
    review = re.sub("[^a-zA-Z]", " ", review)
    review = review.lower().split()
    eng_stopwords = set(stopwords.words("english"))
    review = [w for w in review if not w in eng_stopwords]
    review = " ".join(review + emoticons)

    return review
