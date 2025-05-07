import platform
import subprocess
import os
import json
import psutil
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavfile
import getpass
import glob

def get_system_info():
    try:
        info = {
            "OS": platform.system(),
            "Node": platform.node(),
            "Release": platform.release(),
            "Version": platform.version(),
            "CPU": platform.processor(),
            "Memory": f"{psutil.virtual_memory().total / (1024**3):.2f} GB",
            "Disk": f"{psutil.disk_usage('/').total / (1024**3):.2f} GB",
            "Current User": getpass.getuser(),
            "Uptime": f"{psutil.boot_time() / 3600:.2f} hours",
            "Software": get_installed_software()
        }
        return json.dumps(info, indent=2)
    except Exception as e:
        return f"[!] Error getting system info: {e}"

def get_installed_software():
    try:
        if platform.system() == "Windows":
            result = subprocess.run("wmic product get name", shell=True, capture_output=True, text=True)
            return result.stdout.strip().split("\n")[1:]
        else:
            result = subprocess.run("pkg list-installed", shell=True, capture_output=True, text=True)
            return result.stdout.strip().split("\n")
    except:
        return ["[!] Unable to list software"]

def list_directory(path="."):
    try:
        files = os.listdir(path)
        return "\n".join(files)
    except Exception as e:
        return f"[!] Error listing directory: {e}"

def download_file(filename):
    try:
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                data = f.read()
            return f"[*] File {filename} downloaded (size: {len(data)} bytes)"
        else:
            return f"[!] File {filename} not found"
    except Exception as e:
        return f"[!] Error downloading file: {e}"

def upload_file(filename):
    try:
        with open(filename, "wb") as f:
            f.write(b"Sample uploaded data")
        return f"[*] File {filename} uploaded"
    except Exception as e:
        return f"[!] Error uploading file: {e}"

def delete_file(filename):
    try:
        if os.path.exists(filename):
            os.remove(filename)
            return f"[*] File {filename} deleted"
        else:
            return f"[!] File {filename} not found"
    except Exception as e:
        return f"[!] Error deleting file: {e}"

def search_files(pattern):
    try:
        matches = glob.glob(f"**/{pattern}", recursive=True)
        return "\n".join(matches) or "[!] No files found"
    except Exception as e:
        return f"[!] Error searching files: {e}"

def record_audio(seconds):
    try:
        fs = 44100
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        wavfile.write("recording.wav", fs, recording)
        return "[*] Audio recorded and saved as recording.wav"
    except Exception as e:
        return f"[!] Error recording audio: {e}"

def execute_shell_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return f"[!] Error executing shell command: {e}"

def list_processes():
    try:
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            processes.append(f"PID: {proc.info['pid']}, Name: {proc.info['name']}, CPU: {proc.info['cpu_percent']}%, Memory: {proc.info['memory_percent']:.2f}%")
        return "\n".join(processes)
    except Exception as e:
        return f"[!] Error listing processes: {e}"

def kill_process(pid):
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        return f"[*] Process {pid} terminated"
    except Exception as e:
        return f"[!] Error killing process: {e}"

def suspend_process(pid):
    try:
        proc = psutil.Process(pid)
        proc.suspend()
        return f"[*] Process {pid} suspended"
    except Exception as e:
        return f"[!] Error suspending process: {e}"