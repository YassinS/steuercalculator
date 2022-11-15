import flask
import time
import sqlite3

def db():
    con = sqlite3.connect("./lohnsteuer.db")
    cur = con.cursor()
    return cur

def web():

    return 1