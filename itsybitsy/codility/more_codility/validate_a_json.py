import json


def validate_json(check_me):
    try:
        json.loads(check_me)
    except ValueError as e:
        print(e.args)
        return False
    return True


check_me = '{"key": "val"}'
print(validate_json(check_me))
