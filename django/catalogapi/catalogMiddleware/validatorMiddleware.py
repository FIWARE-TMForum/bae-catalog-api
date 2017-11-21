import json
from jsonschema import Draft4Validator
import os
from django.http import HttpResponse
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

catalog_schema_path = "./jsons/catalogResourceSchema.json"
catalog_example_path = "./jsons/catalogJSONExample.json"
category_schema_path = "./jsons/categoryResourceSchema.json"
category_example_path = "./jsons/catalogJSONExample.json"

schema_dict = {'catalog': json.load(open(catalog_schema_path)),
                'category': json.load(open(category_schema_path)) }

def validate(j, s):
    errors = sorted(Draft4Validator(s).iter_errors(j), key=lambda e: e.path)
    return [x.message for x in errors]


def validator_selector(path):
    return schema_dict[path.split("/")[2]]


class ValidatorMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # Code before view
        r = json.loads(request.body.decode('utf-8'))
        if r is not '':
            v = validate(r, validator_selector(request.META['PATH_INFO']))
            print(v)
            if v != []: 
                return HttpResponse(content=json.dumps({'error': v}, indent=4), status=400)
        response = self.get_response(request)

        # Code after view
        return response
