from connection_loader import connection_loader
import psycopg2
import time

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_database():
    con = connection_loader()

    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cur = con.cursor()

    cur.execute('DROP DATABASE IF EXISTS pythicles;')

    cur.execute('CREATE DATABASE pythicles;')

    print('Database created successfully')


if __name__ == '__main__':
    create_database()
