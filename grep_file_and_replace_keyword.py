from os import listdir
from os.path import isfile, isdir
import os

rel_path = "/home/tsj/"


def list_file_and_replace_keyword():
    for target_file in listdir(rel_path):
        abs_path = os.path.join(rel_path, target_file)
        if isfile(abs_path):
            file_data = ""
            with open(abs_path, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.__contains__("old_string"):
                        line = line.replace("old_string", "new_string")
                    file_data += line
            with open(abs_path, "w") as f:
                f.write(file_data)


if __name__ == "__main__":
    print(list_file_and_replace_keyword())
