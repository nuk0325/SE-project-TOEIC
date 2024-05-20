# vo.py

class Member:
    def __init__(self, id=None, name=None, password=None):
        self.id = id
        self.name = name
        self.password = password

    def __str__(self):
        return 'id:'+self.id+', name:'+self.name+', password:'+self.password
