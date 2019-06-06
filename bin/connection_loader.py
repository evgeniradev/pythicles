import psycopg2
import time


def connection_loader(attempt=0, timeout=60):
    try:
        attempt += 1

        print('Waiting for database to start...')

        con = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            host='pythicles_postgres',
            password=''
        )

        print('Connection established')

        return con
    except psycopg2.OperationalError:
      if attempt < timeout:
          time.sleep(1)

          return connection_loader(attempt)
      else:
          print('Connection timeout reached.')

          exit()


if __name__ == '__main__':
    connection_loader()
