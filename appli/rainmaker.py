import datetime as d
import logging
import json

class Vanne():
    def __init__(self, nom):
        self.nom = nom
        self.mode = "off"
        self.state = self.check_output()
        self.prog = {}

    def change_mode(self, mode):
        if mode in ['on', 'off', 'prog']:
            logging.debug('change mode de {} à {}'.format(self.mode, mode))
            self.mode = mode

    def add_prog(self, prog):
        logging.debug('add {}'.format(prog))
        self.prog.setdefault(prog.nom, prog)
    
    def del_prog(self, name):
        if name == 'all':
            logging.debug('del all')
            self.prog.clear()
        elif name in self.prog:
            logging.debug('del {}'.format(name))
            del self.prog[name]

    def check_output(self):
        if self.mode == 'on':
            return 'open'
        if self.mode == 'off':
            return 'closed'
        if self.mode == 'prog':
            maintenant = d.datetime.now()
            result = self.check_prog()
            for entries in result: 
                logging.debug('check: {}-{} period:{}'.format(entries.start,  entries.stop, [x for x in entries.period if entries.period[x]]))
                cond_1 =entries.start.hour < maintenant.hour or ((entries.start.hour == maintenant.hour) &( entries.start.minute <= maintenant.minute))
                cond_2 =entries.stop.hour > maintenant.hour or ((entries.stop.hour == maintenant.hour) &( entries.stop.minute > maintenant.minute))
                week = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
                liste_j = [week.index(x) + 1  for x in week if entries.period[x]]
                cond_3 = maintenant.isoweekday() in liste_j
                if cond_1 & cond_2 & cond_3:
                    logging.debug('Vanne ouverte pour {}'.format(entries.nom))
                    return 'open'
                else:
                    logging.debug('Vanne fermée pour {}'.format(entries.nom))
            return 'closed'

                
    def check_prog(self):
        result = []
        for v in self.prog.values():
            result.append(v)
        logging.debug('Vanne.check_prog: check: {}'.format(self.prog.keys()))
        return result
        
    def params(self):
        return {self.nom : [self.mode, self.state(), self.prog.keys()]}
    
    def infos(self):
        result = {'nom': self.nom}
        result.setdefault('mode', self.mode)
        result.setdefault('state', self.state)
        progs = []
        for k,v in self.prog.items():
            result.setdefault(k, v.infos())
        return json.dumps(result)



class Program():
    week = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
    def __init__(self,nom):
        self.nom = nom
        self.mode = "time"
        self.start = d.time(0, 0)
        self.stop = d.time(0, 0)
        self.period = {x: False for x in Program.week}

    def __str__(self):
        period = [x for x in self.period if self.period[x] ]
        return '{} => start:{} stop:{} période: {}'.format(self.nom, self.start, self.stop, period)
     
    def infos(self):
        result = {'nom': self.nom}
        result.setdefault('start', (self.start.hour, self.start.minute))
        result.setdefault('stop', (self.stop.hour, self.stop.minute))
        result.setdefault('period',self.period)
        return result

        
if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s:%(message)s', level='DEBUG')
    maintenant = d.datetime.now()
    logging.debug(maintenant)
    v1 = Vanne("vanne 1")
    prog1 = Program('prog_01')
    prog1.period['lundi'] = True
    prog1.period['dimanche'] = True
    prog1.start = d.time(22, 0)
    prog1.stop = d.time(22,30)
    prog2 = Program('prog_02')
    prog2.start = d.time(22,0)
    prog2.stop = d.time(23, 0)
    prog2.period['dimanche'] = True
    v1.add_prog(prog1)
    v1.add_prog(prog2)
    v1.change_mode('prog')
    print(v1.state)
   
    print(v1.infos())
  






