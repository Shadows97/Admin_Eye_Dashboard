

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