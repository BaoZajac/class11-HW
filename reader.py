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
        ext_old = os.path.splitext(self.file_path_old)[-1]      # TODO: 4) jak skierować do odpowiedniej klasy po spr.rozszerzenia?
        print("Old extension: ", ext_old)
        return ext_old
    
    def check_file_ext_new(self):
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
            for linia in reader:
                self.lista.append(linia)
        # super().open_file()
        # print(self.lista)
        return self.lista

    def save_file(self):
        self.switch_list()
        # print(self.lista)
        with open(self.file_path_new, "w", newline="") as f:
            writer = csv.writer(f)
            for linia in self.lista:
                writer.writerow(linia)
            # writer.writerows(self.lista)


class PickleFile(OpenChangeSaveFile):
#     def open_file(self):                # TODO: sprawdzić działanie, gdy będę mieć plik typu pickle
#         with open(self.file_path_old, "rb") as f:
#             reader = pickle.load(f)
#             print(reader)

    def save_file(self):
        self.switch_list()
        # print(self.lista)
        with open(self.file_path_new, "wb") as f:
            pickle.dump(self.lista, f)
            # writer = csv.writer(f)
            # for linia in self.lista:
            #     writer.writerow(linia)


class JSONFile(OpenChangeSaveFile):
    def open_file(self):                # TODO : 2) jak zmienić plik json na listę list, gdy nie znamy zawartości danego pliku?
        # lista = []
        with open(self.file_path_old, "r") as f:
            reader = json.load(f)
            print(reader)
            # for k, v in reader.items():
            #     self.lista.append([k, v])
            # print(reader)
            # for k in reader:
            #     # self.lista.append(linia)
            #     print(k)
                # print(el2)
        # print(self.lista)

    def switch_list(self):    # modyfikacja elementu słownika na podstawie danych z std
        self.open_file()


# ------------------------------------------------------------------------------------

file_old = sys.argv[1]
file_new = sys.argv[2]

if not os.path.exists(file_old) or os.path.isdir(file_old):
    print("Wprowadzono błędną nazwę pliku wejściowego. Dostępne pliki to:")
    os.system("ls")

# available_ext = {".csv": "CSVFile", ".json": "JSONFile", ".pkl": "PickleFile"}
available_ext = [".csv", ".json", ".pkl"]

ext_old = os.path.splitext(file_old)[-1]
ext_new = os.path.splitext(file_new)[-1]
if ext_old not in available_ext or ext_new not in available_ext:
    print("Nieobsługiwany format pliku")
else:
    if ext_old == ".csv":
        CSVFile(file_old, file_new).print_data()        # +
    elif ext_old == ".json":
        ...
    elif ext_old == ".pkl":
        ...
    if ext_new == ".csv":
        CSVFile(file_old, file_new).save_file()         # +
    elif ext_new == ".json":
        ...
    elif ext_new == ".pkl":
        print("wyjście to pickle")



# # OpenChangeSaveFile(file_old).check_file_ext_old()
# CSVFile(file_old, file_new).check_file_ext_old()    +
# CSVFile(file_old, file_new).check_file_ext_new()    +
#
# # CSVFile(file_old, file_new).open_file()
# # CSVFile(file_old, file_new).switch_list()
#
# CSVFile(file_old, file_new).print_data()        +
# CSVFile(file_old, file_new).save_file()         +

# PickleFile(file_old, file_new).save_file()        -


# JSONFile(file_old, file_new).open_file()

