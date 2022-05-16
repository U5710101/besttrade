'''
Create CRUD functions to interact with the database and manipulate portfolio data
'''

from logging import exception
from sqlite3 import Cursor
from tkinter import E
import typing as t
from mysql.connector import MySQLConnection
from .dbutils import get_db_cnx
from app.src.domain.Portfolio import protfolio
import app.src.dao.sql as sql

def get_portfolio_by_id(id: int) -> t.Optional[portfolio]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        cursor.execute.(sql.portfolio_by_id,(id),)
        rs = cursor.fetchone()
        if rs is None:
            return None
        return portfolio(rs['id'], rs['account_id'], rs['ticker'], rs ['quantity'])
    except Exception as e:
        print(f'Unable to retrive portfolio by.id {id}: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def create_portfolio(portfolio: Portfolio) -> None:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        Cursor = db_cnx.cursor()
        Cursor.execute(sql.create_portfolio,(portfolio.account_id.ticker.quantity))
        db_cnx.commit()
    except Exception as e:
            print(f'unable to create a new portfolio:{str(e)}')
    finally:
      Cursor.close()
      db_cnx.close()

def update_portfolio_quantity(id: int, quantity: int)  ->None:
    try:
        db_cnx:MySQLConnection = get_db_cnx()
        Cursor = db_cnx.cursor()
        Cursor.execute(sql.update_portfolio_quantity,(quantity, id))
        db_cnx.commit()
    except Exception as e:
        print(f'unable to update portfolio quantity:{str(e)}')
    finally:
        Cursor.close()
        db_cnx.close()

def delete_portfolio_by_id(id:int) -> None:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        Cursor = db_cnx.cursor()
        Cursor.execute(sql.delete_portfolio_by_id, (id,))
        db_cnx.commit()
    except Exception as e:
        print(f'unable to delete the portfolio: {str(e)}')
    finally:
        Cursor.close()
        db_cnx.close()