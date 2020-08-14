from os import listdir
from os.path import isfile, isdir


def list_file_and_replace_keyword():
    for target_file in listdir("/home/tsj/test"):
        if isfile(target_file):
            file_data = ""
            with open("/home/tsj/test/" + target_file, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.__contains__("old_string"):
                        line = line.replace("old_string", "new_string")
                    file_data += line
            with open("/home/tsj/test/" + target_file, "w") as f:
                f.write(file_data)


if __name__ == "__main__":
    print(list_file_and_replace_keyword())
