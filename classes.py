import os
import sys
import csv
import json
import pickle


class OpenChangeSaveFile:
    def __init__(self, file_path_old, file_path_new):
        self.file_path_old = file_path_old
        self.file_path_new = file_path_new
        self.lista = []

    def check_file_ext_old(self):                       # TODO: sprawdzić czy to jest potrzebne w klasie
        ext_old = os.path.splitext(self.file_path_old)[-1]
        print("Old extension: ", ext_old)
        return ext_old

    def check_file_ext_new(self):                       # TODO: sprawdzić czy to jest potrzebne w klasie
        ext_new = os.path.splitext(self.file_path_new)[-1]
        print("New extension: ", ext_new)
        return ext_new

    def open_file(self):
        pass
        # print("To co jest wczytywane: ", self.lista)

    def switch_list(self):    # modyfikacja elementu listy na podstawie danych z std
        self.open_file()
        for idx in sys.argv[3:]:
            y, x, wartosc = idx.split(",")
            self.lista[int(y)][int(x)] = wartosc
        # print(self.lista)
        return self.lista

    def print_data(self):       # TODO: 3) czy ma wydrukować po prostu listę?
        self.switch_list()
        print(self.lista)

    # def save_file(self):
    #     self.switch_list()


class CSVFile(OpenChangeSaveFile):
    def open_file(self):
        with open(self.file_path_old, "r") as f:
            reader = csv.reader(f)
            for line in reader:
                self.lista.append(line)
        # super().open_file()
        # print(self.lista)
        # lista = self.lista
        # return lista
        return self.lista

    def save_file(self, implement_list):
        with open(self.file_path_new, "w", newline="") as f:
            writer = csv.writer(f)
            for line in implement_list:
                writer.writerow(line)
            # writer.writerows(self.lista)


class JSONFile(OpenChangeSaveFile):
    pass
#     def open_file(self):                # TODO : 2) jak zmienić plik json na listę list, gdy nie znamy zawartości danego pliku?
#         # lista = []
#         with open(self.file_path_old, "r") as f:
#             reader = json.load(f)
#             print(reader)
#             for idx in sys.argv[3:]:
#                 y, x, wartosc = idx.split(",")
#                 reader[int(y)][int(x)] = wartosc
#             print(reader)
            # return reader
            # for k, v in reader.items():
            #     self.lista.append([k, v])
            # print(reader)
            # for k in reader:
            #     # self.lista.append(linia)
            #     print(k)
            # print(el2)
        # print(self.lista)

    # def switch_list(self):    # modyfikacja elementu słownika na podstawie danych z std
    #     self.open_file()
    #     for idx in sys.argv[3:]:
    #         y, x, wartosc = idx.split(",")
    #         reader[int(y)][int(x)] = wartosc
    #     # self.reader[]
    #     print(reader)

    def save_file(self, implement_list):
        # self.switch_list()
        with open(sys.argv[2], "w") as f:
            json.dump(implement_list, f)


class PickleFile(OpenChangeSaveFile):
    def open_file(self):                # TODO: sprawdzić działanie, gdy będę mieć plik typu pickle
        with open(self.file_path_old, "rb") as f:
            self.lista = pickle.load(f)
        return self.lista

    def save_file(self, implement_list):
        with open(sys.argv[2], "wb") as f:
            pickle.dump(implement_list, f)


# wprowadzanie zmian w liście
def switch_list(lista):
    for idx in sys.argv[3:]:
        y, x, wartosc = idx.split(",")
        lista[int(y)][int(x)] = wartosc
    return lista
