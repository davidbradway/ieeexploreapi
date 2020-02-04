import os
import xplore

API_SECRET = os.environ.get("IEEE_SECRET_KEY")

query = xplore.xploreapi.XPLORE(API_SECRET)
query.authorText('Gregg Trahey')
data = query.callAPI()
query.dataFormat('object')
dataobj = query.formatData(data)
#dataobj['articles'][0]['authors']['authors'][0]['full_name']

author_list = list()
articles = dataobj['articles']
for article in articles:
    authors = article['authors']['authors']
    for author in authors:
        name = author['full_name']
        if name not in author_list:
           author_list.append(name)

with open('data.json', 'w') as f:
    json.dump(data.decode("utf-8"), f)
