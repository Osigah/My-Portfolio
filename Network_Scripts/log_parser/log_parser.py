#!/usr/bin/env python3
import paramiko
import re
import getpass
import csv
import os

def fetch_cisco_logs(host, username, password):
    """Connects to a Cisco router via SSH and retrieves log output."""
    ssh = paramiko.SSHClient()  # create an SSH client object
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # auto-accept unknown SSH keys
    ssh.connect(host, username=username, password=password, look_for_keys=False)  # connect to router
    
    stdin, stdout, stderr = ssh.exec_command("show logging")  # run the Cisco command
    logs = stdout.read().decode('utf-8')  # read command output as text
    ssh.close()  # close connection
    return logs  # return log data as a string

def parse_logs(logs, keyword):
    """Searches Cisco log output for lines matching a keyword or pattern."""
    matches = []
    for line in logs.splitlines():  # go through each line of the log
        if re.search(keyword, line, re.IGNORECASE):  # case-insensitive match
            matches.append(line.strip())  # add matching line
    return matches

def save_to_csv(matches, filename='cisco_log_matches.csv'):
    """Saves matching log entries to a CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Matching Cisco Log Entries"])  # header row
        for line in matches:
            writer.writerow([line])  # one match per line

if __name__ == "__main__":
    print(" Welcome to Sigs Cisco Log Parser " )
    host = input("Enter Cisco device IP or hostname: ").strip()
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")  # safely hide password input
    keyword = input("Enter keyword or regex to search for: ").strip()

    print("\nConnecting to device and fetching logs... please wait.")
    try:
        logs = fetch_cisco_logs(host, username, password)
    except Exception as e:
        print(f" Connection failed: {e}")
        exit(1)

    print("Parsing logs for matches...")
    results = parse_logs(logs, keyword)

    output_file = os.path.join(os.getcwd(), 'cisco_log_matches.csv')
    save_to_csv(results, output_file)

    print(f"\n Found {len(results)} matching lines.")
    print(f" Results saved to: {output_file}")
