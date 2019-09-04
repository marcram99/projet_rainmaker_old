from flask import Flask, redirect, render_template, request, url_for
import datetime as d
import json

app = Flask(__name__)

from .rainmaker import Vanne, Program

#---------------------
v1 = Vanne('vanne_1')
p1 = Program('prog_1')
p1.period['lundi'] = True
p1.period['dimanche'] = True
p1.start = d.time(22, 0)
p1.stop = d.time(22,30)
v1.add_prog(p1)
v_list = [v1]
#---------------------

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        params = request.form.to_dict()
        if params['command'] == 'on':
            return json.dumps({'retour':'commande on validée'})
        if params['command'] == 'off':
            return json.dumps({'retour':'commande off validée'})
        if params['command'] == 'prog':
            print (v1.prog.values())
            return json.dumps({'retour':'commande prog validée'})
        if params['command'] == 'update':
            print(params)
            return json.dumps({'retour':'ok'})

    return render_template('main.html')