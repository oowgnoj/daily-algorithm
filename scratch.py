from urllib import urlopen
url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1'
data = urlopen(url).read()
print(data)