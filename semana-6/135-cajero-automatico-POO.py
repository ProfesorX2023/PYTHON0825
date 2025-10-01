import os

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} | Apelido: {self.apellido}\nNumero de Cuenta: {self.numero_cuenta}\nBalance de cuenta: {self.balance}"

    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Depósito Aceptado")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro: # 1000 queremos retirar 200
            self.balance -= monto_retiro
            print("Retiro Aceptado")
        else:
            print("No tienes disponibilidad")


def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese el numero de cuenta: ")
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta) # Creación del objeto o instancia
    return cliente

def inicio():
    mi_cilente = crear_cliente()
    os.system('cls')
    print(mi_cilente)
    opcion = ''
    while opcion != 'S':
        print("Elige: Depositar(D), Retirar(R), o Salir(S)")
        opcion = input().upper()
        if opcion == 'D':

            monto_dep = int(input("Ingresa el monto a Depositar: "))
            mi_cilente.depositar(monto_dep)
            os.system('cls')
        elif opcion == 'R':

            monto_ret = int(input("Ingresas el monto a Retirar: "))
            mi_cilente.retirar(monto_ret)
            os.system('cls')


        print(mi_cilente)


    print("Gracias por utilizar el banco Python")

inicio()


