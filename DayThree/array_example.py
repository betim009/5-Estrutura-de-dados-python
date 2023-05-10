import sys


class ListaArray:
    def __init__(self):
        self.data = []

    def __len__(self):
        # retorna o tamanho de data
        return len(self.data)

    def __str__(self):
        # converte para str e exibe valores
        return str(self.data)

    def get(self, index):
        # recupera o elemento pelo index
        return self.data[index]

    def set(self, index, value):
        # insere um elemento no index informado
        return self.data.insert(index, value)


# preenchendo uma estrutura de array de dados
array = ListaArray()
array.set(0, "Alberto")
array.set(1, "Creusa")
array.set(2, "Carlos")
array.set(3, "Marcela")

# acessando o elemento do array pelo index
print(array.get(0))
print(array.get(1))
print(array.get(2))
print("---------- fim do print ----------")

# tamanho da memoria
array_memory_size = sys.getsizeof(array.data)
print(f"Memory size: {array_memory_size}")
print("--------------------")

# podemos iterar sobre seus elementos da seguinte maneira
index = 0
# enquanto há elementos no array
while index < len(array):
    # recupera o elemento através de um índice
    print("Index:", index, ", Nome:", array.get(index))
    index += 1
