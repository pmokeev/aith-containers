from DAO import DAO
import os

if __name__=='__main__':
    db_name = os.getenv('POSTGRES_DB')
    db_user = os.getenv('POSTGRES_USER')
    db_password = os.getenv('POSTGRES_PASSWORD')
    db_host = os.getenv('POSTGRES_HOST')

    print('ENV')
    print(db_name, db_host, db_password, db_user)

    dao = DAO(  
        db_name,
        db_user,
        db_password,
        db_host
    )

    dao.create_table()
    print('Table has been created')
