import orjson

def sort_json(json_obj):
    if isinstance(json_obj, dict):
        sorted_dict = dict(sorted(json_obj.items(), key=lambda item: item[0]))
        for key, value in sorted_dict.items():
            sorted_dict[key] = sort_json(value)
    elif isinstance(json_obj, list):
        sorted_list = []
        for item in json_obj:
            sorted_list.append(sort_json(item))
    else:
        return json_obj


# 加载有序json
def order_json_loads(json_str):
    json_obj = orjson.loads(json_str)
    return sort_json(json_obj)

# 转储有序json
def order_json_dumps(json_obj):
    json_obj = sort_json(json_obj)
    return orjson.dumps(json_obj)
