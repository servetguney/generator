from helper import get_last,get_third
import ipaddress

a = ipaddress.IPv4Address('192.168.1.10')

print(get_last(a),get_third(a))
