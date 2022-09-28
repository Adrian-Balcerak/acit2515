class Person:
    def __init__(self, name, age):
        if (isinstance(name, str) and isinstance(age, int)):
            if len(name) > 2 and age > 0:
                self.name = name
                self.age = age
            else:
                raise AttributeError
        else:
            raise AttributeError
        
    def get_name(self):
        return f'{self.name.upper()} / {self.age}'