import datetime
import re
import orjson
import jmespath
import concurrent.futures as futures
import multiprocessing as mp

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
def order_json_dumps(json_obj, encoding='utf-8'):
    json_obj = sort_json(json_obj)
    return orjson.dumps(json_obj).decode(encoding)

def path_exists(path):
    return True

def compare(json_obj1, json_obj2):
    if isinstance(json_obj1, dict) and isinstance(json_obj2, dict):
        pass

def is_dict(obj) -> bool:
    return type(obj) is dict

def is_list(obj) -> bool:
    return type(obj) is list

class CompareResult:
    def __init__(self, diff_fields, only_a_has, only_b_has, wildcard_similarity):
        pass

# 与通配路径的匹配
def match_wildcard(path, wildcard_path):
    def match_helper(node, wildcard_node):
        if wildcard_node == '*':
            return True
        elif wildcard_node.find('*') != -1:
            regex = re.escape(wildcard_node).replace(r'\*', r'\d+')
            pattern = re.compile(regex)
            result = bool(pattern.match(node))
            return result
        else:
            return node == wildcard_node

    path = path.split(".")
    wildcard_path = wildcard_path.split(".")
    if len(path) != len(wildcard_path):
        return False

    for node, wildcard_node in zip(path, wildcard_path):
        if not match_helper(node, wildcard_node):
            return False

    return True


def _get_all_jmespath(json_obj, path, node, skip_paths):
    for skip_path in skip_paths:
        if match_wildcard(path, skip_path):
            return []

    if not is_dict(node) and not is_list(node):
        return [path]
    elif is_dict(node):
        temp = [path]
        for key in node.keys():
            temp += _get_all_jmespath(json_obj, f"{path}.{key}", node[key], skip_paths)
        return temp
    elif is_list(node):
        temp = [path]
        for index, sub_node in enumerate(node):
            temp += _get_all_jmespath(json_obj, f"{path}[{index}]", sub_node, skip_paths)
        return temp

def _compare(json_obj1, json_obj2, jmespath, wildcard_path):
    pass

skip_fields = [
    '@.*.English',
    '@.*.extMap.score'
]

if __name__ == '__main__':
    json_obj = [
        {
            "Math": 85,
            "English": 90,
            "Science": 78
        },
        {
            "Math": 92,
            "English": 88,
            "Science": 95
        },
        {
            "Math": 70,
            "English": 75,
            "Science": 80
        }
    ] * 200

    s = datetime.datetime.now()
    with mp.Pool(processes=8) as pool:
        tasks_param = [
            (json_obj, '@', json_obj, ['@[*][*].English'])
        ] * 10000
        results = pool.starmap(_get_all_jmespath, tasks_param)
    e = datetime.datetime.now()
    print(e- s)

