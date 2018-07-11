import ipaddress
def makeaddr(a,b,c,d):
    return ipaddress.IPv4Address(bytes([a,b,c,d]))

def ip():
    for x in range(256):
        print(makeaddr(0, 0, 0, x))
    for x in range(256):
        print(makeaddr(0, 0, x, 255))
    for x in range(256):
        print(makeaddr(0, x, 255, 255))
    for x in range(256):
        print(makeaddr(x, 255, 255, 255))



for addr in ip():
    print(addr)
    

