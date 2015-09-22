
from catalog import mongo

def resource_show(data):
    dataset = mongo.db.datasets.find_one({'resources.id': data.get('id')})
    for resource in dataset['resources']:
        if resource['id'] == data.get('id'):
            return resource
    return None


##############################################################################
# Helper functions
##############################################################################

