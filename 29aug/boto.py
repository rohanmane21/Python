import paramiko
ip_i="13.127.151.243"
usr= "ec2-user"
p_path="bunny.pem"
try:
    client = paramiko.SSHClient()
    print("a")
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("b")
    pk=paramiko.RSAKey.from_private_key_file(p_path)
    print("c")
    client.connect(ip_i,username=usr,pkey=pk)
    print("d")
    stdin,stdout,stder=client.exec_command("df -h")

    print(stdout.read().decode('utf -8'))
except Exception as e:
    print("Exception is ",str(e))
