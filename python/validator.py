import json
import jsonschema
import catalog
import category

catalog_schema_path = "../jsons/catalogResourceSchema.json"
catalog_example_path = "../jsons/catalogJSONExample.json"
category_schema_path = "../jsons/categoryResourceSchema.json"
category_example_path = "../jsons/catalogJSONExample.json"

def validate_catalog(j):
    s = json.load(open(catalog_schema_path, 'r'))
    try:
        jsonschema.validate(j, s)
    except jsonschema.exceptions.ValidationError:
        return False
    
def validator_selector(obj):
    if type(obj) is catalog.Catalog:
        return validate_catalog(obj.__dict__['_Catalog__j']) is None

def main(test):
    catalog_ex = json.load(open(catalog_example_path, 'r'))
    catalog_sch = json.load(open(catalog_schema_path, 'r'))
    category_ex = json.load(open(category_example_path, 'r'))
    category_sch = json.load(open(category_schema_path, 'r'))
    if test == 1:
        categoryEntity = category.Category(category_ex, category_sch)
        return validator_selector(catalog.Catalog.build('name','fail type', [categoryEntity.get_all()], '42', 'https://www.github.com'))
    
    if test == 2:
        cat = catalog.Catalog(catalog_ex)
        return validator_selector(cat)
