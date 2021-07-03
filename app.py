from flask import Flask, request
import sqlite3
import json
from db_utils import get_table

app = Flask(__name__)

ssoffices_list = get_table('sso.db','ssoffices_ssoffice')


@app.route('/api')
def hello_world():
    return 'API Home!'

@app.route('/api/ssa')
def ssa_home():
    return "SSA HOME"

@app.route('/api/ssa/office')
def get_ssoffices():
    output_list = ssoffices_list
    args = request.args
    # Filter python objects with list comprehensions

    for key,val in args.items():
        if key in ('type', 'state', 'city', 'region'):
            param = key
            val = args.get(param)
            output_list = [d for d in output_list if d[param] == val]

    output_json = json.dumps(output_list)
    return output_json

@app.route('/api/ssa/staff')
def get_ssstaff():
   pass




if __name__ == '__main__':
        app.run()
