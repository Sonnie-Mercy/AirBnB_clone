#!/usr/bin/python3
"""
that serializes instances to a JSON file and deserializes JSON file
"""


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, __obj):
        key = "{}.{}".format(obj.__class__.__name, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                serialized_objects = json.load(file)

            for key, obj_dict in serialized_objects.items():
                class_name, obj_id = key.split('.')
                class_module = __import__('models.' + class_name,
                                          fromlist=[class_name])
                class_ = getattr(class_module, class_name)
                obj = class_(**obj_dict)
                self.__objects[key] = obj
