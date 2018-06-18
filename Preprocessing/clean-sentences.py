from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps = PorterStemmer()

stops = set(stopwords.words("english"))

def review_to_words(raw_review):
    review_text=BeautifulSoup(raw_review).get_text()
    letters_only= re.sub("[^a-zA-Z]"," ", review_text)
    words=letters_only.lower().split()
    words= [w for w in words if not w in stops]
    words = [ps.stem(w) for w in words]
    return(" ".join(words))
   
   
# iterate over sentences and pass to the function
