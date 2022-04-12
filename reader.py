import os
import sys
from classes import CSVFile, JSONFile, PickleFile


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

