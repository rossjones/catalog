
from catalog import mongo

def package_show(data):
    dataset = mongo.db.datasets.find_one({'name': data.get('id')})
    return _prep_package(dataset)

def package_list(data):
    datasets = mongo.db.datasets.find({}, {'name': 1})
    return [d['name'] for d in datasets]


##############################################################################
# Helper functions
##############################################################################

def _prep_package(pkg):
    pkg['id']  = str(pkg['_id'])
    del pkg['_id']
    return pkg
