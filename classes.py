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


class CSVFile(OpenChangeSaveFile):
    def open_file(self):
        if os.path.exists(self.file_path_old):
            with open(self.file_path_old, "r") as f:
                reader = csv.reader(f)
                for line in reader:
                    self.lista.append(line)
            return self.lista

    def save_file(self, implement_list):
        with open(self.file_path_new, "w", newline="") as f:
            writer = csv.writer(f)
            for line in implement_list:
                writer.writerow(line)
            # writer.writerows(self.lista)


class JSONFile(OpenChangeSaveFile):
    def open_file(self):
        if os.path.exists(self.file_path_old):
            with open(self.file_path_old, "r") as f:
                self.lista = json.load(f)
            return self.lista

    def save_file(self, implement_list):
        with open(sys.argv[2], "w") as f:
            json.dump(implement_list, f)


class PickleFile(OpenChangeSaveFile):
    def open_file(self):
        if os.path.exists(self.file_path_old):
            with open(self.file_path_old, "rb") as f:
                self.lista = pickle.load(f)
            return self.lista

    def save_file(self, implement_list):
        with open(sys.argv[2], "wb") as f:
            pickle.dump(implement_list, f)


# wprowadzanie zmian w liście
def switch_list(lista):
    if lista:
        for idx in sys.argv[3:]:
            y, x, wartosc = idx.split(",")
            lista[int(y)][int(x)] = wartosc
    return lista
