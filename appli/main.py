from flask import Flask, redirect, render_template, request, url_for
import datetime as d
import json

app = Flask(__name__)

from .rainmaker import Vanne, Program

#---------------------
v1 = Vanne('vanne_1')

p1 = Program('prog01')
p1.period['lundi'] = True
p1.period['mardi'] = True
p1.period['jeudi'] = True
p1.period['dimanche'] = True
p1.start = d.time(1, 1)
p1.stop = d.time(2, 2)

p2 = Program('prog02')
p2.period['lundi'] = True
p2.start = d.time(22,0)
p2.stop = d.time(23, 2)

p3 = Program('prog03')
p3.period['jeudi'] = True
p3.period['dimanche'] = True
p3.start = d.time(12, 0)
p3.stop = d.time(14,0)

v1.add_prog(p1)
v1.add_prog(p2)
v1.add_prog(p3)

#---------------------
@app.template_filter()
def title(nom):
    return "{} {}".format(nom[:4].upper(), nom[4:])


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        params = request.form.to_dict()
        if params['command'] == 'on':
            return json.dumps({'retour':'commande on validée'})
        if params['command'] == 'off':
            return json.dumps({'retour':'commande off validée'})
        if params['command'] == 'prog':
            return json.dumps({'retour':'commande prog validée'})    
        if params['command'] == 'update':
            print(json.loads(v1.infos())['nb_prog']) 
            return v1.infos()

    return render_template('main.html')

@app.route('/modif/<prog>', methods=['POST', 'GET'])
def modif(prog):
    if request.method == 'POST':
        params = request.form.to_dict()
        if params['command'] == 'on':
            return json.dumps({'retour':'commande on validée'})
        if params['command'] == 'off':
            return json.dumps({'retour':'commande off validée'})
        if params['command'] == 'prog':
            return json.dumps({'retour':'commande prog validée'})    
        if params['command'] == 'update':
            return v1.infos()
    return render_template('modif.html',prog=prog)