class Vanne():
    def __init__(self, nom):
        self.nom = nom
        self.mode = "off"
        self.prog = {"prog_1": "no prog"}

    def change_mode(self, mode):
        if mode in ['on', 'off', 'prog']:
            self.mode = mode

    def state(self):
        if self.mode == 'on':
            return 'open'
        if self.mode == 'off':
            return 'close'
        if self.mode == 'prog':
            result = []
            for k,v in self.prog.items():
                result.append('{}: {}'.format(k, v))  
            return result
    def add_prog(self, dico):
        for k,v in dico.items():
            self.prog.setdefault(k,v)
        


if __name__ == "__main__":
    v1 = Vanne("vanne 1")
    print(v1.state())
    v1.change_mode('on')
    print(v1.state())
    v1.change_mode('prog')
    print(v1.state())
    v1.add_prog({"prog2":"run a fond"})
    print(v1.state())




