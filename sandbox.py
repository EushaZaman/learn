import pprint
headings = [item for item in range(10)]
dataitem = [item+2 for item in range(10)]
json_data = dict(zip(headings, dataitem))
pprint.pprint(json_data)
