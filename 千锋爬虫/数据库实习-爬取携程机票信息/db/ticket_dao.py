from Dao.base import BaseDao
from TEST.entity import Flight


class FlightDao(BaseDao):
    def query(self, where=None, whereargs=None):
        ret = super(FlightDao, self).query('booksystem_Flight', 'name', 'leave_city', 'arrive_city', 'leave_airport',
                                           'arrive_airport', 'leave_time', 'arrive_time', 'capacity',
                                           'price', 'book_sum', 'income', where=where, whereargs=whereargs)
        return [
            Flight(item['name'], item['leave_city'], item['arrive_city'], item['leave_airport'], item['arrive_airport'],
                   item['leave_time'], item['arrive_time'], item['capacity'], item['price'], item['book_sum'],
                   item['income'])
            for item in ret
        ]
