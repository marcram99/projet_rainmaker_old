import datetime as d
import logging




class Vanne():
    def __init__(self, nom):
        self.nom = nom
        self.mode = "off"
        self.state = self.check_output
        self.prog = {}

    def change_mode(self, mode):
        if mode in ['on', 'off', 'prog']:
            logging.debug('Vanne.change_mode: de {} à {}'.format(self.mode, mode))
            self.mode = mode

    def add_prog(self, prog):
        logging.debug('Vanne.add_prog: add {}'.format(prog))
        self.prog.setdefault(prog.nom, prog)
    
    def del_prog(self, name):
        if name == 'all':
            logging.debug('Vanne.del_prog: del all')
            self.prog.clear()
        elif name in self.prog:
            logging.debug('Vanne.del_prog: del {}'.format(name))
            del self.prog[name]

    def check_output(self):
        logging.debug('Vanne.check_output: check: {}'.format(self.mode))
        if self.mode == 'on':
            logging.debug('Vanne.check_output: return OPEN')
            return 'open'
        if self.mode == 'off':
            logging.debug('Vanne.check_output: return CLOSED')
            return 'closed'
        if self.mode == 'prog':
            maintenant = d.datetime.now()
            logging.debug('Vanne.check_output: maintenant: {}:{}'.format(maintenant.hour, maintenant.minute))
            
            result = self.check_prog()
            for entries in result:
                
                logging.debug('Vanne.check_output: hour= {} / {} minute= {}/{}'.format(maintenant.hour,entries.start.hour, maintenant.minute, entries.start.minute))
                if entries.start.hour < maintenant.hour or ((entries.start.hour == maintenant.hour) &( entries.start.minute <= maintenant.minute)):
                    logging.debug('plus petit que start...')
                

    def check_prog(self):
        logging.debug('Vanne.check_prog')
        result = []
        for v in self.prog.values():
            result.append(v)
        logging.debug('Vanne.check_prog: check: {}'.format(self.prog))
        return result
        
    def __str__(self):
        return '{}: mode={} prog={}'.format(self.nom, self.mode, self.prog.keys())


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
    
    def params(self):
        return {self.nom : [self.start,self.stop, self.period]}

        
if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s:%(message)s', level='DEBUG')
    maintenant = d.datetime.now()
    logging.debug(maintenant)
    v1 = Vanne("vanne 1")
    v1.change_mode('prog')
    prog1 = Program('prog_01')
    prog1.period['lundi'] = True
    prog1.start = d.time(1,38)
    prog1.stop = d.time(2,0)
    v1.add_prog(prog1)
    print(v1.state())
  






