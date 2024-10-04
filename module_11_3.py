import inspect


class SomeClass:
    class_attr = 123
    def __init__(self, attribute=1):
        self.attribute = attribute

    def class_func(self):
        print(self.attribute)


def introspection_info(obj):
    info = {}
    info['type'] = str(type(obj)).split(sep="'")[1]
    attributes = []
    methods = []
    for i, item in inspect.getmembers(obj):
        if callable(item) or '__' in i:
            methods.append(i)
        else:
            attributes.append(i)
    info['attributes'] = attributes
    info['attrs'] = [getattr(obj, i, 'None') for i in attributes]
    info['methods'] = methods
    if inspect.getmodule(obj):
        info['module'] = inspect.getmodule(obj).__dict__['__name__']
    else:
        info['module'] = __name__
    info['isclass'] = inspect.isclass(obj)
    return info


number = 42
class_obj = SomeClass(number)

number_info = introspection_info(number)
class_obj_info = introspection_info(class_obj)
class_info = introspection_info(SomeClass)

print(number_info)
print(class_obj_info)
print(class_info)

