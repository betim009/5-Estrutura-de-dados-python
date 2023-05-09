# Importando os módulos necessários
from os import mkdir, listdir
from os.path import join
from shutil import rmtree

# Define o caminho do diretório para a memória secundária
DISK_PATH = "./disk"


# Define a classe SecondaryMemory
class SecondaryMemory:
    # O método construtor
    def __init__(self, disk_path=DISK_PATH):
        # Define o caminho para o diretório da memória secundária
        self.disk_path = disk_path
        # Tenta criar o diretório (se ele já existir, nada acontece)
        try:
            mkdir(self.disk_path)
        except FileExistsError:
            pass

    # Método para carregar um valor na memória secundária
    def load(self, value):
        # Converte o valor para uma string
        value = str(value)
        # Define o nome do próximo arquivo na sequência
        next_index = str(len(listdir(self.disk_path)))
        # Define o caminho completo para o novo arquivo
        next_file_name = join(self.disk_path, next_index)
        # Abre o arquivo e escreve o valor nele
        with open(next_file_name, "w", encoding="UTF-8") as file:
            file.write(value)

    # Método para recuperar um valor da memória secundária
    def get(self, index):
        # Converte o índice para uma string
        index = str(index)
        # Define o caminho completo para o arquivo com o índice especificado
        file_name = join(self.disk_path, index)
        # Abre o arquivo e lê o valor nele
        with open(file_name) as file:
            return float(file.read())

    # Método para limpar a memória secundária
    def clean(self):
        # Remove o diretório e todos os arquivos dentro dele
        rmtree(self.disk_path)
        # Cria um novo diretório vazio
        mkdir(self.disk_path)
