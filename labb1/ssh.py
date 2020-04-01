import paramiko
import time

ip = input("Enter host IP address or hostname: ")
username = input("Enter username: ")
password = input("Enter password: ")

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, port=22, username=username,
                        password=password,
                        look_for_keys=False, allow_agent=False)

remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(65535)
print(output)

remote_conn.send("conf t\n")
time.sleep(1)
output = remote_conn.recv(65535)
print(output)

remote_conn.send("int loopback 1\n")
time.sleep(1)
output = remote_conn.recv(65535)
print(output)

remote_conn.send("ip address 8.8.8.8 255.255.255.0\n")
time.sleep(1)
output = remote_conn.recv(65535)
print(output)
