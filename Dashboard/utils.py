import socket
import sys


def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

def convert (n):
    print(bytes2human(n)[:-1])
    return float(bytes2human(n)[:-1])

def convert1 (n):

    return round(n/1024/1024/1024,3)

def convert2 (n):

    return round((n*8)/1024,3)


def portScan (host):
    rapport = {}
    try:
        for port in range(1, 9090):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host, port))
            if result == 0:
                print("Port {}: 	 Open".format(port))
                rap = {}
                rap["port"] = port
                rap["etat"] = "Open"
                rapport[port] = rap


            sock.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    return rapport

