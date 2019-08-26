class Vanne():
    def __init__(self, nom):
        self.nom = nom
        self.mode = "off"
        self.prog = {}

    def new_mode(self, mode):
        if mode in ['on', 'off', 'prog']:
            self.mode = mode

    def actif(self):
        if self.mode == 'on':
            return 'open'
        if self.mode == 'off':
            return 'close'
        if self.mode == 'prog':
            result = 'check program'
            return result



if __name__ == "__main__":
    v1 = Vanne("vanne 1")
    print(v1.nom)
    print(v1.mode)
    print(v1.actif())
    v1.new_mode('on')
    print(v1.mode)
    print(v1.actif())
    v1.new_mode('prog')
    print(v1.mode)
    print(v1.actif())
