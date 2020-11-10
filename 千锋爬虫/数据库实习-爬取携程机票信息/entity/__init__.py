class Flight:
    def __init__(self, name, leave_city, arrive_city, leave_airport, arrive_airport, leave_time, arrive_time, capacity,
                 price, book_sum, income):
        self.name = name
        self.leave_city = leave_city
        self.arrive_city = arrive_city
        self.leave_airport = leave_airport
        self.arrive_airport = arrive_airport
        self.leave_time = leave_time
        self.arrive_time = arrive_time
        self.capacity = capacity
        self.price = price
        self.book_sum = book_sum
        self.income = income

    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s %s" % (
            self.name, self.leave_city, self.arrive_city, self.leave_airport, self.arrive_airport, self.leave_time,
            self.arrive_time, self.capacity, self.price, self.book_sum, self.income)

    def __repr__(self):
        return self.__str__()
