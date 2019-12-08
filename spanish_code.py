# class Queue
class Cola:
    '''
   Representa a una cola, con operaciones de encolar y
   desencolar. El primero en ser encolado es también el primero
   en ser desencolado.

   Represents a queue, with gluing operations and
   decouple The first to be glued is also the first
   in being uncoupled.
   '''

    def __init__(self):
        '''
        Crea una cola vacía.

        Create an empty queue.
       '''
        self.items = []

    # def glue:
    def encolar(self, x):
        '''
       Encola el elemento x.

       Glue the element x.
       '''
        self.items.append(x)

    # def decouple:
    def desencolar(self):
        '''
       Elimina el primer elemento de la cola y devuelve su
       valor. Si la cola está vacía, levanta ValueError.

        Remove the first element from the queue and return its
       value. If the queue is empty, raise ValueError.
       '''
        if self.esta_vacia():
            # "Queue is empty"
            raise ValueError("La cola está vacía")
        return self.items.pop(0)

    # def it's empty:
    def esta_vacia(self):
        '''
       Devuelve True si la cola esta vacía, False si no.

        Returns True if the queue is empty, False if not.
       '''
        return len(self.items) == 0

    # Este método está para simplificar las pruebas (This method is to simplify the tests)
    # def glue many:
    def encolar_muchos(self, iterable):
        '''
       Encola todos los elementos del iterable en la cola.

        Glue all items of the iterable in the queue.
       '''
        for elem in iterable:
            self.encolar(elem)

    # Este método está para simplificar las pruebas (This method is to simplify the tests)
    def __str__(self):
        '''
       Devuelve una representación en la forma > [e1, e2, ...] -> de la cola.

        Returns a representation in the form> [e1, e2, ...] -> of the queue.
       '''
        return ', '.join(map(str, reversed(self.items)))

# class Node
class _Nodo:
    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox


# class Control tower
class TorreDeControl:
    def __init__(self):
        self.vip = Cola() # I do not know if I have to write something here
        self.plebeyos = Cola()

    # def new arrival
    def nuevo_arribo(self, vuelo):
        self.vip.encolar(vuelo)

    # def new game
    def nueva_partida(self, vuelo):
        self.plebeyos.encolar(vuelo)

    #def see_state
    def ver_estado(self):
        # "Flights waiting to land: | Flights waiting to take off:"
        return f"Vuelos esperando para aterrizar: {self.vip} \nVuelos esperando para despegar: {self.plebeyos}"


torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
print(torre.ver_estado())