'Part 2: Connecting postgresql to Python'
import psycopg2
from config import config

def connect():
    # start with a connection placeholder
    connection = None
    try:
        params = config() # instance of config
        print('Connecting to the postgres dB...')
        connection = psycopg2.connect(**params) # connect with params
        
        # create a cursor
        crsr = connection.cursor()
        print('Postgres dB version: ')
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close()
    except(Exception, psycopg2.DatabaseError) as e:
        print(e)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')

# if run as main module call mtd connect    
if __name__ == "__main__":
    connect()
    
        