import socket

hostname = "localhost"
pesan = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname,50001))
print "Program komunikasi tentang diri sendiri"

while pesan.lower() != "q":
    pesan = raw_input("perintah")
    s.send(pesan)
    if pesan.lower() == "keluar":
        response = s.recv(1024)
        print "Jawab: ", respinse
        s.close()
        break
    else pesan.lower() != "keluar":
        response = s.recv(1024)
        print "Jawab: ", response
s.close()
            
