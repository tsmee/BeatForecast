import json
from pprint import pprint
data_storage = []
with open('data.json') as data_file:
    data = json.load(data_file)

items_on_page = data["pagination"]["per_page"]

def data_from_page(page_data, items):
    