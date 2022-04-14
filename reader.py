import os
import sys
from classes import CSVFile, JSONFile, PickleFile, switch_list


file_old = sys.argv[1]
file_new = sys.argv[2]

if not os.path.exists(file_old) or os.path.isdir(file_old):
    print("Wprowadzono błędną nazwę pliku wejściowego. Dostępne pliki to:")
    os.system("ls")

available_ext = [".csv", ".json", ".pkl"]

ext_old = os.path.splitext(file_old)[-1]
ext_new = os.path.splitext(file_new)[-1]
if ext_old not in available_ext or ext_new not in available_ext:
    print("Nieobsługiwany format pliku")
else:
    if ext_old == ".csv":
        lista = CSVFile(file_old, file_new).open_file()
    elif ext_old == ".json":
        lista = JSONFile(file_old, file_new).open_file()
    elif ext_old == ".pkl":
        lista = PickleFile(file_old, file_new).open_file()

    lista = switch_list(lista)
    print(lista)

    if ext_new == ".csv":
        CSVFile(file_old, file_new).save_file(lista)
    elif ext_new == ".json":
        JSONFile(file_old, file_new).save_file(lista)
    elif ext_new == ".pkl":
        PickleFile(file_old, file_new).save_file(lista)

