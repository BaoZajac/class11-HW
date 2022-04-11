import csv
import os
import sys
import json
import pickle


class OpenChangeSaveFile:
    def __init__(self, file_path_old, file_path_new):
        self.file_path_old = file_path_old
        self.file_path_new = file_path_new
        self.lista = []

    def check_file_ext_old(self):
        ext = os.path.splitext(self.file_path_old)[-1]
        return ext
    
    def check_file_ext_new(self):
        ext = os.path.splitext(self.file_path_new)[-1]
        return ext

    def open_file(self):
        ...
        # print(self.lista)       # TODO: 1) dlaczego to nie działa dla open_file w CSVFile?

    def switch_list(self):    # modyfikacja elementu listy na podstawie danych z std
        self.open_file()
        for idx in sys.argv[3:]:
            y, x, wartosc = idx.split(",")
            self.lista[int(y)][int(x)] = wartosc
        # print(self.lista)
        return self.lista

    def print_data(self):       # TODO: 4) czy ma wydrukować po prostu listę?
        self.switch_list()
        print(self.lista)
        
    def save_file(self):
        self.switch_list()
        with open(self.file_path_new, "w") as f:
            
        


class CSVFile(OpenChangeSaveFile):
    def open_file(self):
        # lista = []
        with open(self.file_path_old, "r") as f:
            reader = csv.reader(f)
            for linia in reader:
                self.lista.append(linia)
        # print(self.lista)
        return self.lista

    def save_file(self):
        with open(self.file_path_new, "w") as f:


class PickleFile(OpenChangeSaveFile):
    def open_file(self):                # TODO: sprawdzić działanie, gdy będę mieć plik typu pickle
        with open(self.file_path_old, "rb") as f:
            reader = pickle.load(f)
            print(reader)


class JSONFile(OpenChangeSaveFile):
    def open_file(self):                # TODO : 2) jak zmienić plik json na listę list, gdy nie znamy zawartości danego pliku?
        # lista = []
        with open(self.file_path_old, "r") as f:
            reader = json.load(f)
            print(reader)
            # print(reader)
            for k in reader:
                # self.lista.append(linia)
                print(k)
                # print(el2)
        # print(self.lista)


src_file = sys.argv[1]

# # OpenChangeSaveFile(src_file).check_file_ext_old()
# CSVFile(src_file).check_file_ext_old()

CSVFile(src_file).open_file()
# print(lista)
# JSONFile(src_file).open_file()
CSVFile(src_file).switch_list()

CSVFile(src_file).print_data()

# if not os.path.exists([sys.argv[1]])
