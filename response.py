import json
__author__ = 'johnson'


def response(*args, **kwargs):
    status = kwargs.get('status', 200)
    result = kwargs.get('result', None)
    return json.dumps({
        'status': status,
        'result': result
    })
