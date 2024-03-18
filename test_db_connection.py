from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

database_url = 'mysql://root:aDbGfCCd533Da-CHcfgdGf3-Cg1hH1FF@roundhouse.proxy.rlwy.net:49193/railway'

try:
   
    engine = create_engine(database_url)


    with engine.connect() as connection:
        query = text('SELECT 1')

        result = connection.execute(query).scalar()

        print('Connected to the database successfully!')

except OperationalError as e:
    print('Failed to connect to the database:', e)
