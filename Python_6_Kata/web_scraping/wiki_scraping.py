from re import compile
from requests import get
from bs4 import BeautifulSoup

full = "https://en.wikipedia.org{}".format
pair = lambda link: (link.get('title'), full(link.get('href')))

# You can change it into a oneline if you want
def wikiscraping(url):
    text = get(url).text
    soup = BeautifulSoup(text, "html.parser")
    links = soup.find(id='bodyContent').find_all('a', attrs={'href': compile("^\/wiki\/[^:]+$")})
    return dict(map(pair, links))

# So there are no tests for this as I really didn't have a clue what I was doing here.
# As this was all so new to me, I decided that the best thing for my learning was to see how it had been done.
# After having looked at some other tutorials, I feel more confident that next time I could do this on my own!
# it's not hard, it's new!
