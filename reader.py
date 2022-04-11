import csv
import os
import sys
import json


class OpenChangeSaveFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.lista = []

    def check_file_ext(self):
        ext = os.path.splitext(self.file_path)[-1]
        # print(ext)
        return ext

    def open_file(self):
        print(self.lista)       # TODO: dlaczego to nie działa dla open_file w CSVFile?


class CSVFile(OpenChangeSaveFile):
    def open_file(self):
        # lista = []
        with open(self.file_path, "r") as f:
            reader = csv.reader(f)
            for linia in reader:
                self.lista.append(linia)
        # print(self.lista)


class PickleFile(OpenChangeSaveFile):
    with open(self.file_path)


class JSONFile(OpenChangeSaveFile):
    def open_file(self):
        # lista = []
        with open(self.file_path, "r") as f:
            reader = json.load(f)
            print(reader)
            # print(reader)
            for k in reader:
                # self.lista.append(linia)
                print(k)
                # print(el2)
        # print(self.lista)


src_file = sys.argv[1]

# # OpenChangeSaveFile(src_file).check_file_ext()
# CSVFile(src_file).check_file_ext()

CSVFile(src_file).open_file()
JSONFile(src_file).open_file()

# if not os.path.exists([sys.argv[1]])
