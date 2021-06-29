from flask import Flask, request
import sqlite3
import json
from db_utils import get_table

app = Flask(__name__)

ssoffices_json = get_table('sso.db','ssoffices_ssoffice')


@app.route('/api')
def hello_world():
    return 'API Home!'

@app.route('/api/ssa/offices')
def get_ssoffices():
    return ssoffices_json

@app.route('/api/ssa/staff')
def get_ssstaff():
   pass




if __name__ == '__main__':
        app.run()
