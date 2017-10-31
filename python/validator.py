import json
import jsonschema
import catalog
import category

catalog_schema_path = "../jsons/catalogResourceSchema.json"
catalog_example_path = "../jsons/catalogJSONExample.json"
category_schema_path = "../jsons/categoryResourceSchema.json"
category_example_path = "../jsons/catalogJSONExample.json"

schema_dict = {'<class \'catalog.Catalog\'>': ('_Catalog__j', catalog_schema_path),
                   '<class \'category.Category\'>': ('_Category__j', category_schema_path)}

def validate(j, s):
    try:
        return jsonschema.validate(j, s) is None
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        return False
    
def validator_selector(obj):
    t = schema_dict[str(type(obj))]
    return validate(obj.__dict__[t[0]], json.load(open(t[1], 'r')))

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
