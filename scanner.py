from socket import *
import concurrent.futures

def scan_ip(ip_address):
    try:
        s = socket(AF_INET, SOCK_STREAM) 
        s.settimeout(1) 
        result = s.connect_ex((ip_address, 80))
        s.close()

        if result == 0:
            try:
                hostname = socket.gethostbyaddr(ip_address)[0]
            except:
                hostname = "Unkown Hostname"
            print(f"{hostname}, {ip_address} is open ")
    except Exception:
        pass

def Scan():
    ip_range1 = input("Enter the 'lowest' ip in the range of ip addresses you want to scan: ")
    ip_range2 = input("Now enter the 'highest' ip in your chosen range of ip addresses: ")

    print("Scanning...")

    basic_ip = ".".join(ip_range1.split(".")[:3])
    start = int(ip_range1.split(".")[-1]) 
    end = int(ip_range2.split(".")[-1]) + 1

    ip_list = [f"{basic_ip}.{i}" for i in range(start, end)]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(scan_ip, ip_list)

        
Scan()