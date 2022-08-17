class Cola:#clase
    def __init__(self, tamano):#metodo constructor
        self.tamano = tamano
        self.cola=[]

    def menu_cola(self):
        opciones = ['COLA -> SELECCIONE UNA OPCION: ',
                    '1. Push', '2. Pop', '3. Show', '4. Eliminar',
                    '5. Insertar', '6. Buscar', '7. Salir']
        for i in range(len(opciones)):
            print('\033[1;34m',opciones[i],'\033[0;m')
        num = int(input('Ingrese una opción:'))
        if num == 1:
            self.push()
        elif num == 2:
            self.pop()
        elif num == 3:
            self.show()
        elif num == 4:
            self.eliminar()
        elif num == 5:
            self.insertar()
        elif num == 6:
            self.buscar()
        elif num == 7:
            self.salir()
        self.menu_cola()

    def push(self):#+
        if len(self.cola) == self.longitug():
            print('El tamaño maximo de la cola es de:',self.longitug(),'\n',
                  '\033[1;31m','YA NO SE PERMITEN MAS VALORES','\033[0;m')
        else:
            for i in range(1):
                self.cola.append(int(input('Ingrese un valor: ')))
            print(self.cola[::-1])

    def pop(self):#+
        if len(self.cola) != 0:
            self.cola.remove(self.cola[0])
            print('Cola actual: ',self.cola[::-1])
        else:
            print('\033[1;31m','-La Cola esta vacia-','\033[0;m')

    def buscar(self):
        if len(self.cola) != 0:
            busca=int(input('Ingrese el dato que desea buscar: '))
            if busca in self.cola:
                for i in range(len(self.cola)):
                    if busca == self.cola[i]:
                        print('Se encuentra en la pocicion: ', i+1)
            else:
                print('\033[1;31m','-No se encuentra en la cola-','\033[0;m')
        else:
            print('\033[1;31m','-La Cola esta vacia-','\033[0;m')

    def insertar(self):
        if len(self.cola) == self.longitug():
            self.show()
            self.cola.remove(self.cola[0])
        insert = int(input('Ingrese lo que desea insertar: '))
        posicion = int(input('Ingrese la posición en la que desea ingresar: '))
        self.cola.insert(posicion-1, insert)

    def longitug(self):#+
        return self.tamano

    def show(self):#+
        if len(self.cola) < 1:
            print('\033[1;31m','-La Cola esta vacia-','\033[0;m')
        else:
            print('\033[1;37m', 'Ejemplo: [inicio,....,final]', '\033[0;m'
                  , '\n', 'Su cola es:', self.cola)

    def eliminar(self):
        if len(self.cola) != 0:
            elimina = int(input('Ingrese el elemento a eliminar: '))
            if elimina in self.cola:
                self.show()
                posicion = int(input('posición del elemento: '))
                if self.cola[posicion-1]==elimina:
                    self.cola.remove(self.cola[posicion-1])
                else:
                    print('\033[1;31m','La posicion es incorrecta','\033[0;m',)
            else:
                print('\033[1;31m','-No se encuentra en la cola-','\033[0;m')

        else:
            print('\033[1;31m','-La Cola esta vacia-','\033[0;m')

    def salir(self):#+
        print('\033[1;31m','-off-','\033[0;m')
        exit()

class Pila:
    def __init__(self,tamano):
        self.tamano=tamano
        self.pila=[]

    def menu_pila(self):
        opciones = ['PILA -> SELECCIONE UNA OPCION: ',
                    '1. Push', '2. Pop', '3. Show', '4. Eliminar',
                    '5. Insertar', '6. Buscar', '7. Salir']
        for i in range(len(opciones)):
            print('\033[1;35m',opciones[i],'\033[0;m')
        num = int(input('Ingrese una opción:'))
        if num == 1:
            self.push()
        elif num == 2:
            self.pop()
        elif num == 3:
            self.show()
        elif num == 4:
            self.eliminar()
        elif num == 5:
            self.insertar()
        elif num == 6:
            self.buscar()
        elif num == 7:
            self.salir()
        self.menu_pila()

    def push(self):
        if len(self.pila) == self.longitug():
            print('El tamaño maximo de la pila es de:',self.longitug(),'\n',
                  '\033[1;31m','YA NO SE PERMITEN MAS VALORES','\033[0;m')
        else:
            for i in range(1):
                self.pila.append(int(input('Ingrese un valor: ')))
            print(self.pila[::-1])

    def pop(self):
        if len(self.pila) != 0:
            self.pila.remove(self.pila[-1])
            print('Pila actual: ',self.pila[::-1])
        else:
            print('\033[1;31m','-La pila esta vacia-','\033[0;m')

    def eliminar(self):
        if len(self.pila) != 0:
            elimina = int(input('Ingrese el elemento a eliminar: '))
            if elimina in self.pila:
                self.show()
                posicion = int(input('posición del elemento: '))
                if self.pila[posicion - 1] == elimina:
                    self.pila.remove(self.pila[posicion - 1])
                else:
                    print('\033[1;31m', 'La posicion es incorrecta', '\033[0;m', )
            else:
                print('\033[1;31m', '-No se encuentra en la pila-', '\033[0;m')
        else:
            print('\033[1;31m', '-La pila esta vacia-', '\033[0;m')

    def insertar(self):
        if len(self.pila) == self.longitug():
            self.show()
            self.pila.remove(self.pila[0])
        insert = int(input('Ingrese lo que desea insertar: '))
        posicion = int(input('Ingrese la posición en la que desea ingresar: '))
        self.pila.insert(posicion - 1, insert)

    def buscar(self):
        if len(self.pila) != 0:
            busca=int(input('Ingrese el dato que desea buscar: '))
            if busca in self.pila:
                for i in range(len(self.pila)):
                    if busca == self.pila[i]:
                        print('Se encuentra en la pocicion: ', i+1)
            else:
                print('\033[1;31m','-No se encuentra en la pila-','\033[0;m')
        else:
            print('\033[1;31m','-La pila esta vacia-','\033[0;m')

    def longitug(self):
        return self.tamano

    def show(self):
        if len(self.pila) < 1:
            print('\033[1;31m','-La pila esta vacia-','\033[0;m')
        else:
            print('\033[1;37m','Ejemplo: [inicio,....,final]','\033[0;m'
            ,'\n','Su pila es:',self.pila)

    def salir(self):
        print('\033[1;31m','-off-','\033[0;m')
        exit()

#INICIO DEL CODIGO
menu = ['SELECCIONE UN METODO:','1. Pilas', '2. Colas']
for i in range(len(menu)):
    print('\033[1;32m',menu[i],'\033[0;m')
op = int(input('Ingrese una opción: '))
while op <= 1 or op >= 2:
    if op == 1:
        tmn=int(input('Ingrese el tamaño de la pila: '))
        x = Pila(tmn)#tmn es el tamaño de la lista
        x.menu_pila()#llamada del metodo de la pila
    elif op == 2:
        tmn = int(input('Ingrese el tamaño de la cola: '))
        x = Cola(tmn)#tmn es el tamaño de la lista
        x.menu_cola()#llamada del metodo de la cola
    else:
        print('\033[1;31m','Opción incorrecta''\033[0;m')
        op = int(input('Ingrese una opción: '))