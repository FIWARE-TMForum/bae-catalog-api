import json
from jsonschema import Draft4Validator
from django.http import HttpResponse

catalog_schema_path = "./jsons/catalogResourceSchema.json"
catalog_example_path = "./jsons/catalogJSONExample.json"
category_schema_path = "./jsons/categoryResourceSchema.json"
category_example_path = "./jsons/catalogJSONExample.json"

schema_dict = {'catalog': json.load(open(catalog_schema_path)),
               'category': json.load(open(category_schema_path))}


def validate(j, s):
    errors = sorted(Draft4Validator(s).iter_errors(j), key=lambda e: e.path)
    return [x.message for x in errors]


def validator_selector(path):
    return schema_dict[path.split("/")[2]]


class ValidatorMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # import ipdb
        # ipdb.sset_trace()
        # Code before view
        if request.body and request.META['REQUEST_METHOD'] != 'GET':
            req = json.loads(request.body.decode('utf-8'))
            # print(req)
            if req is not '':
                v = validate(req, validator_selector(request.META['PATH_INFO']))
                if v != []:
                    return HttpResponse(content=json.dumps({'error': v}, indent=4), status=400)
        response = self.get_response(request)
        # print("Response: {}".format(response.data))
        # Code after view
        return response
