import getopt
import sys

def Usage():
    print """
     Usage:
          -s(mandatory): server,
          -p(mandatory): port,
          -c(mandatory): command,
          -k(mandatory): key

     Example: python demo_getopt.py -s "127.0.0.1" -p 1025 -c "ls" -k "-l"
          """


if __name__ == "__main__":
    try:
        '''
        C:\Python27>python nnn.py --server="aaa" --port=123 --command="ls" --key="gg"
aaa 123 ls gg

        C:\Python27>python nnn.py -s "aaa" -p 123 -c "ls" -k "gg"
aaa 123 ls gg

        '''
        options, args = getopt.getopt(
            sys.argv[1:], "-s:-p:-c:-k:",
            ["server=", "port=", "command=", "key="])
        if len(options) <= 3:
            print "Not enough arguments, please check help info."
            Usage()
            sys.exit(1)
        for name, value in options:
            if name in ('-s', '--server'):
                host = value
            if name in ('-p', '--port'):
                port = value
            if name in ('-c', '--command'):
                command = value
            if name in ('-k', '--key'):
                key = value
        print host, port, command, key
    except getopt.GetoptError, err:
        print str(err)
        Usage()
        sys.exit(1)
