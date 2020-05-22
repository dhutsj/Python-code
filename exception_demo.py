class URLError(Exception):
    pass

if __name__ == '__main__':
    try:
        raise URLError("URL Error")
    except URLError as e:
        print e.args[0]
