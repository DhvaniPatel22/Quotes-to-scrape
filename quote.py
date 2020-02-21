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


#age_number = 1
# while page_number < 11:

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
    #page_number = page_number + 1

# page_number = 2
# while page_number < 11:
#     next_page = 'http://quotes.toscrape.com/page/'+ str(page_number) + '/'
#     page_number += 1
#     if next_page:
#         url = base_url + next_page

# if page_number < 11:
#     page_number += 1
#     parse(respData, pageURL)
        # page_number = 2
    # next_page = 'http://quotes.toscrape.com/page/'+ str(page_number) + '/'

    # if page_number < 11:
    #     page_number += 1
    #     respData(next_page, pageURL)
    
    # try:
    #     response = respData.get(parse)
    #     content = response.text
    #     getpage = 1
    # except:
    #     # proxyconnection()
    #     getpage = 0
#next_page = re.findall(r'')



# print(data)

#sys.exit()


# store(quotes,author)
#tag = re.findall(r'')
#print(len(tags) )

