from pip._vendor.certifi import where

from dao.base import BaseDao
from entity import Student


class StuDao(BaseDao):
    def query(self, where=None, whereargs=None):
        ret = super(StuDao, self).query('Student', 'sno', 'sname', 'ssex','sbirthday', 'sdept', 'speciality', where=where, whereargs=whereargs)
        return [
            Student(item['sno'], item['sname'], item['ssex'], item['sbirthday'], item['sdept'], item['speciality'])
            for item in ret
        ]


if __name__ == '__main__':
    dao = StuDao()
    print(dao.query(where = 'where ssex = %s', whereargs = ('男')))
    print(dao.query(where='where ssex = %(sex)s', whereargs={'sex' : '男'}))
