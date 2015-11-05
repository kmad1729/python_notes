import socket

#create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# now connect to the web server on port 80 - the normal http port

python_org_addr = ("www.python.org", 80)

print("python_org_addr -->", python_org_addr)
s.connect(python_org_addr)


print("local addr -->", s.getsockname())

