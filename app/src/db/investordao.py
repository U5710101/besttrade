import typing as t
from mysql.connector import MySQLConnection
from app.src.domain.Investor import Investor
from app.src.db.dbutils import get_db_cnx
import app.src.db.sql as sql

# CRUD: Create / Read / Update / Delete

def get_all_investors() -> t.List[Investor]: # empty list if no investors are created in the db
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True) # results will return as a dict
        cursor.execute(sql.get_all_investors_sql)
        rs = cursor.fetchall()
        if len(rs) == 0:
            return []
        else:
            investors = []
            for row in rs:
                investors.append(Investor(row.get('name'), row.get('address'), row.get('status'), row.get('id')))
            return investors
    except Exception as e:
        print(f'An exception occurred while trying to get a list of all investors: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close() # to prevent any memory leaks


# create a function that will return an investor by ID
def get_investor_by_id(id: int) -> t.Optional[Investor]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        cursor.execute(sql.get_investor_by_id_sql, (id,))
        rs = cursor.fetchone() # because ID is a primary key
        if rs is None: # if no investor exists with provided ID
            return None
        else:
            investor = Investor(rs['name'], rs['address'], rs['status'], rs['id'])
            return investor
    except Exception as e:
        print(f'Unable to retreive investor with ID {id}: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def get_investor_with_name(name: str) -> t.List[Investor]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        cursor.execute(sql.get_investors_by_name_sql, (name, ))
        rs = cursor.fetchall() # expected multiple rows because name is not unique
        if len(rs) == 0:
            return []
        else:
            investors = []
            for row in rs:
                investors.append(Investor(row['name'], row['address'], row['status'], row['id']))
            return investors
    except Exception as e:
        print(f'Unable to retrieve investors with names = {name}: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def create_investor(investor: Investor) -> None:
    if investor is None:
        raise Exception('Found None object for investor')
    try:
        db_cnx = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.create_investor, (investor.name, investor.address, investor.status))
        db_cnx.commit() # because we're creating data not reading data 
    except Exception as e:
        print(f'Unable to create a new investor: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()


def update_investor_address(id: int, address: str) -> None:
    try:
        db_cnx = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.update_investor_address_sql, (address, id))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to update investor address: str(e)')
    finally:
        cursor.close()
        db_cnx.close()

def delete_investor_by_id(id: int) -> None: 
    try:
        db_cnx = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.delete_investor_by_id, (id,))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to delete investor: str(e)')
    finally:
        cursor.close()
        db_cnx.close()