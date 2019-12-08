import socket

hotsname = "localhost"
pesan = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname,50002))
print "Menghitung luas jajargenjang"
while pesan.lower() != "keluar":
    pesan = raw_input("pesan:")
    s.send(pesan)
    if pesan.lower() == "keluar":
        response = s.recv(1024)
        s.close()
        break
    elif pesan.lower() != "keluar":
        response = s.recv(1024)
        print "Response:", response
s.close()
