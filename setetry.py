from socket import *
import time
m_socket = socket(AF_INET, SOCK_STREAM)
m_socket.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
m_socket.bind(("localhost", 9999))
m_socket.setblocking(0)
m_socket.listen(3)
players = []
while 1:
    dat = ''
    try:
        n_s, ip = m_socket.accept()
        print(f"your ip is {ip}")
        n_s.setblocking(0)
        players.append(n_s)
        print(len(players))
        if len(players) == 2:
            try:
                players[0].send("Start".encode())
                players[1].send("Start".encode())
            except:
                pass
    except:
        pass
    for s in players:
        try:
            if dat == '':
                dat = s.recv(1024)
                dat = dat.decode()
            else:
                k = s.recv(1024)
                dat += k.decode()
        except:
            pass

    for s in players:
        try:
            if dat != "":
                print(f"{dat}")
            s.send(dat.encode())
        except:
            players.remove(s)
            s.close()
            print("Player Disconnected")
    time.sleep(0.02)
