class FileStorage:
    __file_path = ''
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        