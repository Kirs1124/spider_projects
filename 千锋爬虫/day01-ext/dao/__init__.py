import pymysql
from pymysql.cursors import DictCursor


class Connection:
    def __init__(self):
        # 连接database
        self.conn = pymysql.Connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    password='20000819wjw',
                                    db='jxgl',
                                    charset='utf8')

    def __enter__(self):
        # DictCursor 针对查询的结果进行dict化
        # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
        return self.conn.cursor(cursor=DictCursor)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:       # 异常种类
            self.conn.rollback()  # 回滚事务
            # 日志收集异常信息，上报给服务器
        else:
            self.conn.commit()  # 提交事务

    def close(self):
        try:
            # 关闭数据库连接
            self.conn.close()
        except:
            pass
