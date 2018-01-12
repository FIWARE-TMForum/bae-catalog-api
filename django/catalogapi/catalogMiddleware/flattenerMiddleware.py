import json


def flatten_by_key(d, key):
    ret = {}

    for k, v in d.items():
        if k == key:
            ret.update(flatten_dict_with_key(v, key))
        elif isinstance(v, dict):
            ret.update({k: flatten_by_key(v, key)})
        elif isinstance(v, list):
            lst = [flatten_by_key(i, key) for i in v]
            ret.update({k: lst})
        else:
            ret.update({k: v})

    return ret


def unflatten_by_key(d, key):
    ret = {}
    ret[key] = {}

    for k, v in d.items():
        nk = k.split("_")
        if (len(nk) > 1) and (nk[0] == key):
            try:
                ret[key].update({nk[1]: v})
            except KeyError:
                continue
        elif isinstance(v, dict):
            ret.update({k: unflatten_by_key(v, key)})
        elif isinstance(v, list):
            lst = [unflatten_by_key(i, key) for i in v]
            ret.update({k: lst})
        else:
            ret.update({k: v})
    if ret[key] == {}:
        ret.pop(key)

    return ret


def flatten_dict_with_key(d, key):
    ret = {}

    for k, v in d.items():
        ret.update({(key + "_" + k): v})

    return ret


class FlattenerMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # before view

        if request.body and request.META['REQUEST_METHOD'] != 'GET':
            flattened_data = flatten_by_key(json.loads(request.body.decode('utf-8')), 'validFor')
            request._body = json.dumps(flattened_data).encode('utf-8')

        response = self.get_response(request)
        # after view

        if isinstance(response.data, list):
            response.data = [unflatten_by_key(response[x], 'validFor') for x in response.data]
            response._container = [json.dumps(response.data).encode('utf-8')]
        else:
            response.data = unflatten_by_key(response.data, 'validFor')
            response._container = [json.dumps(response.data).encode('utf-8')]

        return response
