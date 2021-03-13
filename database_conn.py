import pymysql
import config
def connection():

    conn = pymysql.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        db=config.db,
    )

    return conn

