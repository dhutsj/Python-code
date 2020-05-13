import os


def print_file_path(file_path):
    for _ in os.listdir(file_path):
        if os.path.isdir(_):
            print_file_path(os.path.join(file_path, _))
        else:
            if _.endswith(".pyc"):
                print os.path.join(file_path, _)


print_file_path('C:/Python27')
