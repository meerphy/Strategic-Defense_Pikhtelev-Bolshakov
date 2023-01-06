from socket import *
import sqlite3
import json


class Server:
    def __init__(self, ip, port, basse_name):
        print(f"ip: {ip}, \nServerPort: {port}")
        self.base_n = basse_name
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((ip, port))
        self.server.listen(3)

    def sender(self, user, text):
        user.send(text.encode('utf-8'))

    def startserv(self):
        while 1:
            user, adres = self.server.accept()
            print('text')
            self.listen(user)

    def listen(self, user):
        self.sender(user, "text")
        iswork = 1
        while iswork:
            try:
                dat = user.recv(1024)
                self.sender(user, 'geted')
            except:
                dat = ''
                iswork = 0
        if len(dat) > 0:
            msg = dat.decode('utf-8')

            if msg == 'disconnect':
                self.sender(user, "u are disconnected")
                user.close()
                iswork = 0
            else:

                con = sqlite3.connect(self.base_n)
                cur = con.cursor()
                try:
                    answ = [x for x in cur.execute(msg)]
                    error = ''
                except Exception as h:
                    error = str(h)
                    answ = ''
                con.commit()
                cur.close()
                con.close()
                answer = json.dumps(
                    {
                        'answer': answ,
                        'error': error
                    }
                )
                self.sender(user, answer)
            dat = b''
            msg = ''
        else:
            print("disconnected")
            iswork = 0

    server = socket(
        AF_INET, SOCK_STREAM
    )


Server('192.168.1.3', 9999, 'data/databas.db').startserv()
