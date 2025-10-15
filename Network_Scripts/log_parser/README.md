# Cisco Log Parser (SSH-based Network Log Analyzer)

This project is a Python-based log parser designed to connect to Cisco routers via SSH, retrieve their system logs, and analyze them for key patterns such as **interface down** events or **EIGRP-related** messages.

---

##  Features

- SSH connection to Cisco routers using `paramiko`
- Automatic retrieval of system logs (`show logging`)
- Regex-based filtering for:
  - **Interface down/up events**
  - **EIGRP adjacency or route updates**
- Interactive search: user can specify any custom keyword or error pattern
- Cleanly formatted output for easy reading and export

---

##  Lab Setup

The project was tested in a **Packet Network Emulator (pnet)** lab environment with **three Cisco routers** configured with **EIGRP** for route exchange.

Each router was configured to generate logs for testing:
```bash
router eigrp 100
 network 10.0.0.0
!
interface g0/0
 ip address 10.0.0.1 255.255.255.0
 no shut
```

## How It Works

1. The script connects to the router(s) via SSH after requesting user to input the host ip, username and password.
2. It retrives logs using the cisco CLI command 'show logging'.
3. It asks the user what to seacrh for - e.g. down, EIGRP, neighbor, BGP, etc.
4. The regex engine matches the pattern and prints matching log lines.
5. Results are then saved to a .csv file in the same directory.

## Requirements

1. Python 3.8+
2. paramiko module for SSH
3. Access to cisco router(s) via SSH
4. Router logging enabled

Install dependencies
```bash
pip install paramiko
```

## Usage
1. Clone this repo:
```bash
git clone https://github.com/<your-username>/cisco-log-parser.git
cd cisco-log-parser
```
2. Run the script:
```bash
python3 cisco_log_parser.py
```
3. Enter credentials when prompted.
4. Enter a keyword ( e.g down. EIGRP) to filter logs.

```yaml
Enter router IP: 10.0.0.1
Enter username: admin
Enter password:
What log pattern do you want to search for? down
```

## Future Imporovements
- Support for multiple routers in parallel
- Timestamp filters
- Linux syslog parser companion
- Visualisation

## Author
Osigah Precious Ogedegbe

Network Security Engineer | Automation | SRE | Cloud 