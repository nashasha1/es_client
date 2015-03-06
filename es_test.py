from datetime import datetime
from elasticsearch import Elasticsearch
import os
host=os.getenv('ES_HOST','http://127.0.0.1')
port=os.getenv('ES_PORT','9200')
es_server = host + ":" + port
print "connect: ", es_server
es = Elasticsearch([es_server])

# doc = {
#     'author': 'xdzhang1',
#     'text': 'this is for xdzhang test elasticsearch1.',
#     'timestamp': datetime(2010, 10, 10, 10, 10, 10)
# }
# 
# res = es.index(index="test-index", doc_type='tweet', id=2, body=doc)
# 
# print res

res = es.get(index="test-index", doc_type='tweet', id=2)

print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

print res,type(res)
