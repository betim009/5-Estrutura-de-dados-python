class MainMemory:
    # Método construtor
    def __init__(self):
        # chama o método clean para inicializar a memória com uma lista vazia.
        self.clean()

    def load(self, value):
        # adiciona um valor à lista de memória.
        self.loaded_memory.append(value)

    def get(self, index):
        try:
            # Recupera um valor na posição especificada pelo index
            # O index é usado para acessar um elemento específico da lista.
            return float(self.loaded_memory[index])
        except IndexError:
            return 0

    def clean(self):
        self.loaded_memory = []
