def funzione_doppio(x):
    """Questa funzione restituisce il doppio del argomento passato alla funzione"""
    # TODO: Implementare la funzione per restituire il doppio di x
    z = 2*x
    print(z)
    return z

def funzione_quadrato(y):
    """
    Questa funzione dovrebbe prendere un numero e restituire il suo quadrato.
    Completa l'implementazione.
    """
    # TODO: Implementare la funzione per restituire il quadrato di y
    return y*y

class ClasseParzialmenteImplementata:
    def __init__(self, nome):
        self.nome = nome
        self.valore = 13

    def metodo_esistente(self):
        return f"Ciao, sono {self.nome}!"

    def metodo_da_completare(self, valore):
        """
        Questo metodo dovrebbe aggiungere il 'valore' a un attributo interno
        e restituire il nuovo valore.
        """
        # TODO: Implementare l'aggiunta del valore e la restituzione
        y = self.valore + valore
        return f"Ciao, il mio numero fortunato è {y} !"