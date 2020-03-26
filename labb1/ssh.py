import paramiko
import time
ip_address = "172.17.159.75"
username = "administrator"
password = "cisco123"
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)
remote_connection = ssh_client.invoke_shell()
print("You are now connected to: ", ip_address, "\n")
remote_connection.send("ip address show\n")
time.sleep(1)
output = remote_connection.recv(65535)
print(output)
ssh_client.close
