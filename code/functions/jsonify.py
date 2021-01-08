import json


def json_output(object):
    jsonStr = json.dumps(object.__dict__, sort_keys=True, indent=4)

    return jsonStr