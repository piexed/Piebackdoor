import socket
import netifaces
import psutil
import scapy.all as scapy
import time
import random
import subprocess

def get_network_info():
    try:
        interfaces = netifaces.interfaces()
        info = []
        for iface in interfaces:
            addrs = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in addrs:
                for addr in addrs[netifaces.AF_INET]:
                    info.append(f"Interface: {iface}, IP: {addr['addr']}")
        connections = psutil.net_connections()
        for conn in connections:
            info.append(f"Connection: {conn.laddr} -> {conn.raddr if conn.raddr else 'N/A'} (Status: {conn.status})")
        result = subprocess.run("route print" if platform.system() == "Windows" else "ip route", shell=True, capture_output=True, text=True)
        info.append("Routing Table:\n" + result.stdout)
        return "\n".join(info)
    except Exception as e:
        return f"[!] Error getting network info: {e}"

def port_scan(ip, port_range):
    try:
        start_port, end_port = map(int, port_range.split("-"))
        open_ports = []
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
            time.sleep(0.05)
        return f"[*] Open ports: {open_ports}" if open_ports else "[!] No open ports found"
    except Exception as e:
        return f"[!] Error scanning ports: {e}"

def spoof_packet(target_ip, packet_count):
    try:
        for _ in range(packet_count):
            packet = scapy.IP(dst=target_ip)/scapy.TCP(sport=random.randint(1024, 65535), dport=80, flags="S")
            scapy.send(packet, verbose=False)
            time.sleep(0.1)
        return f"[*] Sent {packet_count} spoofed packets to {target_ip}"
    except Exception as e:
        return f"[!] Error spoofing packets: {e}"