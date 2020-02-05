import os
import xplore

API_SECRET = os.environ.get("IEEE_SECRET_KEY")

query = xplore.xploreapi.XPLORE(API_SECRET)
query.dataFormat('object')
query.booleanText('"David Bradway" OR "David P. Bradway" OR "D. P. Bradway"')
data = query.callAPI()
#data['articles'][0]['authors']['authors'][0]['full_name']

author_list = list()
articles = data['articles']
for article in articles:
    authors = article['authors']['authors']
    for author in authors:
        name = author['full_name']
        if name not in author_list:
           author_list.append(name)

print(*author_list, sep = "")

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)

rev_list = [i[::-1] for i in author_list]
rev_list.sort()
new_list = [i[::-1] for i in rev_list]
