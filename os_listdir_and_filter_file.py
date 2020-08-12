from os import listdir
from os.path import isfile, isdir

def grep_config_file():
    target_dir = {}
    for directory in listdir("/data/jenkins/jobs"):
        if isdir("/data/jenkins/jobs/" + directory):
            for target_file in listdir("/data/jenkins/jobs/" + directory):
                if target_file == "config.xml":
                    with open("/data/jenkins/jobs/" + directory + "/" + target_file, "r") as f:
                        script_list = []
                        lines = f.readlines()
                        for line in lines:
                            if line.__contains__(".sh") or line.__contains__(".py"):
                                script_list.append(line)
                    target_dir[directory] = script_list
    return target_dir


if __name__ == "__main__":
    print(grep_config_file())
