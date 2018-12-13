import socket, fcntl, struct, subprocess

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_fileno = s.fileno()
    SIOCGIFADDR = 0x8915

    structpack = struct.pack('256s', ifname[:15])
    ioctl = fcntl.ioctl(socket_fileno, SIOCGIFADDR, structpack)
    ntoa = socket.inet_ntoa(ioctl[20:24])
    
    return ntoa

for ni in socket.if_nameindex():
    ifname = ni[1].encode()
    
    if not ifname == b'lo':
        try:
            ip = get_ip_address(ifname)
        except OSError as err:
            ip = None
        
        break

subprocess.call(['python3', '/app/manage.py', 'runserver', f"{ip}:8000"])