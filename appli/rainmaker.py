import datetime as d


class Vanne():
    def __init__(self, nom):
        self.nom = nom
        self.mode = "off"
        self.prog = {}

    def change_mode(self, mode):
        if mode in ['on', 'off', 'prog']:
            self.mode = mode

    def add_prog(self, prog):
        self.prog.setdefault(prog.nom, prog)
    
    def del_prog(self, name):
        if name in self.prog

    def state(self):
        if self.mode == 'on':
            return 'open'
        if self.mode == 'off':
            return 'close'
        if self.mode == 'prog':
            return self.check_prog()

    def check_prog(self):
        result = []
        for k,v in self.prog.items():
            result.append('{}: {}'.format(k, v))
        return result


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

    v1 = Vanne("vanne 1")
    v1.change_mode('prog')
    prog1 = Program('prog_01')
    prog1.period['lundi'] = True
    prog1.start = d.time(22, 45)
    prog2 = Program('prog_02')
    v1.add_prog(prog1)
    print(v1.state())
    v1.add_prog(prog2)
    print(v1.state())
    v1.change_mode('on')
    print(v1.state())






