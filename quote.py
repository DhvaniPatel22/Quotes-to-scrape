import urllib.request
import urllib.parse
import re
import pymysql
import sys

conn = pymysql.connect(host="localhost", user="quotetb", passwd="cLIDakBLyujcyG4d", db="quotedb", charset="utf8")
cur = conn.cursor()

def store(data):
    for x in data:
        cur.execute("INSERT INTO quote_tb (quotes, author, tags) VALUES ('" + str(x['name']) + "', '" + str(x['author']) + "', '" + str(x['tags']).strip(",") + "')")
        cur.connection.commit()


#url = 'http://quotes.toscrape.com/page/'+ str(page_number) + '/'
url = 'http://quotes.toscrape.com/'
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

#for text in respData:
#for i in re.findall:

# for text in str(respData):

quotes = re.findall(r'<span class="text" itemprop="text">(.*?)</span>',str(respData))
author = re.findall(r'<small class="author" itemprop="author">(.*?)</small>',str(respData))
tags = re.findall(r'<div class="tags">(.*?)</div>',str(respData))

# print(quotes)
# print(author)
# print(x)
# sys.exit()

data = []
for k, x in enumerate(tags):
    # print(quotes[k])
    # sys.exit()
    tmpData = {
        'name': quotes[k],
        'author': author[k],
        'tags':'' 
    }

    tag = re.findall(r'<a class="tag" (.*?)>(.*?)</a>',str(x))

    for t in tag:
        tmpData['tags'] = tmpData['tags'] + ',' + str(t[1])
                #+ ', ' +
    data.append(tmpData)

store(data)

