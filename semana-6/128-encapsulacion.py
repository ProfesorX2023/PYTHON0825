class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo


cuenta_1 = Cuenta(150)

print(cuenta_1.saldo)