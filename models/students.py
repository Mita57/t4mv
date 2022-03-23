import datetime
from .BasicModel import BasicModel


class Student(BasicModel):
    _DATABASE = 'students'
    _TABLE = 'students'
    _USER = 'postgres'
    _PASSWORD = 'postgres'
    _HOST = '127.0.0.1'
    _PORT = '5432'
    id: int
    name: str
    group: str
    year: int

    _FIELDS_MAPPING = {
        'id': int,
        'name': str,
        'group': str,
        'year': int
    }


    def get_by_id(self, id):
        pass

    def get_all_students(self):
        pass

    def remove_stud(self, id):
        pass

    def __init__(self, nickname, email, password, join_date, birth_date):
        self.nickname = nickname
        self.email = email
        self.password = password
        self.join_date = join_date
        self.status = type(self).__name__
        self.birth_date = birth_date
