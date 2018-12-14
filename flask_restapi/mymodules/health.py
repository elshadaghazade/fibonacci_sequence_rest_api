import os, platform, socket, psutil, subprocess, requests, time

class SRM:
    
    data={}
    
    @staticmethod
    def get_datas():
    
        # PLATFORM
        plt={
            'hostname':platform.node(),
            'os':platform.system(),
            'processor':platform.processor(),
            'kernel_realease':platform.release(),
            'kernel_version':os.uname().version,
            'system_dist':' '.join(platform.linux_distribution()),
            'machine':platform.machine()
        }
        
        # CPU
        result,output = subprocess.getstatusoutput('cat /proc/cpuinfo')
        output = output.split('\n')
        
        cpu ={}
        for i in range(1,len(output)):
            if i==6:
                continue
            elif i>12:
                break
            else:
                element = output[i].split(':')
                cpu.update({element[0].strip().replace(' ', '_').lower():element[1].strip()})
        cpu.update({"cpu_logical_processors": psutil._pslinux.cpu_count_logical(),
                    "cpu_percantage_usage":psutil.cpu_percent(interval=0.1)})
        
        # NETWORK
        nt={}
        nt.update({"hostname":socket.gethostbyname(socket.gethostname())})
        import fcntl,struct
        
        def get_ip_address(ifname):
            s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            socket_fileno = s.fileno()
            sioc=0x8915
            struck = struct.pack('256s',ifname[:15])
            ioctl = fcntl.ioctl(socket_fileno,sioc,struck)
            ntoa = socket.inet_ntoa(ioctl[20:24])
            return ntoa
        for n in socket.if_nameindex():
            ifname = n[1].encode()
            try:
                ip = get_ip_address(ifname)
            except:
                ip=None
            nt.update({n[1]:ip})

        
        # MEMORY
        mem={}
        result,output = subprocess.getstatusoutput('free')
        memory = psutil.virtual_memory()
        mem.update({'total':memory.total,
                    'aviable': memory.available,
                    'percent': memory.percent,
                    'used': memory.used,
                    'free':memory.free,
                    'active':memory.active,
                    'inactive': memory.inactive,
                    'buffers': memory.buffers,
                    'cached': memory.cached,
                    'shared': memory.shared,
                    'slab': None, #memory.slab,
                    'swap':output.split("\n")[2].split()[1]
        });
           
        # filesystem
        fs={}
        result,output = subprocess.getstatusoutput('df -T')
        output = output.split('\n')[1:]
        free=0
        used=0
        total=0
        for i in output:
            k=i.split()
            fs.update({k[0]+' mounted on '+k[-1]:str(round(int(k[-3])))})
            free+=int(k[-3])
            used+=int(k[-4])
            total+=int(k[2])
        fs.update({'free':free,#/(1024**2),
                    'used':used,#/(1024**2),
                    'total':total#/(1024**2)
                    })
        SRM.data.update({
            "platform":plt,
            "CPU":cpu,
            "Networking":nt,
            "Memory":mem,
            "FileSystem":fs
        })

        return SRM.data


def endpointhealth(endpoint):
    t1 = time.time()
    r = requests.get('http://' + endpoint)
    if r.status_code != 200:
        raise Exception("Endpoint is down")
    t2 = time.time()

    return {
        'endpoint': 'http://' + endpoint,
        'response_time': round(t2 - t1, 5)
    }
