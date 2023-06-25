import pyshorteners


# function for long url to short url
def shorten_url(long_url):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(long_url)
    return shortened_url


long_url = input('Enter original URL Here: ')
short_url = shorten_url(long_url)
print('New URL: ', short_url)
