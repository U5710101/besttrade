'''
Create CRUD functions to interact with the database and manipulate account data
'''
from distutils.util import execute
from tkinter import E
from turtle import update
from app.src.api.blueprints.account_bp import delete_account
from app.src.db.portfoliodao import delete_portfolio_by_id
from app.src.domain.Investor import Investor
from mysql.connection import Mysqlconnection
from curses.ascii import RS
from fileinput import close
from sqlite3 import Cursor
import typing as t
from app.src.domain.Account import Account
from .dbutils import get_db_cnx
from app.src.dao.sql import sql
from .sql import get_account_by_id_sql

def get_all_accounts()  -> t.List[Account]: 
    try:
        db_cnx: Mysqlconnection = get_db_cnx()
        Cursor = db_cnx.cursor(dictionary=True) 
        Cursor = execute(sql.get_all_investors_sql)
        rs = Cursor.fetchall()
        if len(rs) == 0:
            return []
        else:
            accounts = []
            for row in rs:
                accounts.append(Account(row.get)('investor_id'), row.get ('balance'), row.get('id'))
            return accounts
    except Exception as e:
        print(f'An Exception occurred while trying to get a list of all accounts: {str(e)]}')
    finally:
        Cursor.close()
        get_db_cnx()            

def get_Account_by_id(id: int) -> t.Optional[Account]:
    try:
        get_db_cnx = get_db_cnx()
        Cursor = get_db_cnx.curser(dictionary=True)
        Cursor.execute(get_account_by_id_sql, (id,))
        rs = Cursor.fetchone()
        if rs is None:
            return None
        return Account(rs['investor_id'], rs['balance'], rs['id'])
    except Exception as e:
        print(f'An exception occurred while getting account with ID {id}: {str(e)}')
    finally:
        Cursor.close()
        get_db_cnx.close()

def create_account(investor_id, balance) -> None:
    try:
        db_cnx: Mysqlconnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.create_account, (investor_id, balance))
    except Exception as e:
            print (f'unable to create a new account:{str(e)}')
    finally:
        cursor.close
        db_cnx.close

def update_account(investor_id, balance) -> None:
    try:
        db_cnx: Mysqlconnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.update_account, (investor_id, balance))
    except Exception as e:
            print (f'unable to update account:{str(e)}')
    finally:
            cursor.close()
            db_cnx.close()

def delete_account_by_id (id:int) -> None:
    try:
        db_cnx: Mysqlconnection = get_db_cnx()
        Cursor = db_cnx.cursor()
        Cursor.execute(sql.delete_account_by_id,(id,))
        db_cnx.commit()
    except Exception as e:
        print(f'unable to delete an account: {str(e)}')
    finally:
        Cursor.close()
        db_cnx.close()

def sell_stock_id,ticker,quantity):
    try:
        db_cnx:Mysqlconnection = get_db_cnx()
        Cursor = db_cnx.cursor()
        db_cnx: Mysqlconnection = get_db_cnx()
        Cursor = db_cnx.cursor()
        db_cnx.commit()
        current_quantity= get_stock_quantity(account_id,ticker)  
        if sale_quantity == current_quantity:
            delete_portfolio_by_id
    except Exception as e:
        print(f'Unable to bring portfolio quantiy:{str(e)}')
    finally:
        cursor.close()
        db_cnx.close()      