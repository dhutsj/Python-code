def get_lines(file_path):
    count = 0
    l = []
    with open(file_path, 'rb') as f:
        for i, line in enumerate(f):
            count += 1
            l.append(line)
            if count == 10:
                count = 0
                yield l
                l = []

if __name__ == "__main__":
    for data in get_lines("C:/Python27/vvvv.txt"):
        print data
