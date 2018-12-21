from conf import settings
import os, pickle

def save(obj):
    '''数据处理保存'''
    path_dir = os.path.join(settings.BASE_DB, obj.__class__.__name__.lower())
    if not os.path.isdir(path_dir):
        os.mkdir(path_dir)
    path_obj = os.path.join(path_dir, obj.name)
    with open(path_obj, 'wb') as f:
        pickle.dump(obj, f)


def select(obj_name, dir_name):
    '''数据处理查询'''
    path_dir = os.path.join(settings.BASE_DB, dir_name)
    if not os.path.isdir(path_dir):
        os.mkdir(path_dir)
    path_obj = os.path.join(path_dir, obj_name)
    if os.path.exists(path_obj):
        with open(path_obj, 'rb')as f:
            return pickle.load(f)
    else:
        return None