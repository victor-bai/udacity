import urllib

def read_text():
    quotes = open('F:\udactiy\p2-python\ipnd-starter-code-master\movie_quotes.txt')
    s = quotes.read()
    print s
    quotes.close()
    check_porfanity(s)

def check_porfanity(text_to_check):
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q='+text_to_check)
    output = connection.read()
    print output
    connection.close()

read_text()