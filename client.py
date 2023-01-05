from socket import *
import json


class Client:
    def __init__(self, ip, port):
        self.cli = socket(AF_INET, SOCK_STREAM)
        self.cli.connect((ip, port))

    def connect(self):
        try:
            msg = self.cli.recv(1024).decode('utf-8')
        except Exception as e:
            print(e)
            exit()
        if msg == 'text':
            self.listen()
        else:
            exit()

    def sender(self, text):
        self.cli.send(text.encode('utf-8'))
        while self.cli.recv(1024).decode('utf-8') == 'getted':
            self.cli.send(text.encode('utf-8'))

    def listen(self):
        iswork = 1
        while iswork:
            req = input('Type SQL request: ')
            if req != '':
                if req == 'disconnect':
                    self.sender(req)
                    print(self.cli.recv(1024).decode('utf-8'))
                else:
                    self.sender(req)
                    dat = json.loads(self.cli.recv(1024).decode('utf-8'))

                    if dat['answer']:
                        print(f'serv_answ:{dat["answer"]}')
                    else:
                        print(f'serv_err:{dat["error"]}')



Client(input('type server ip: '), 9999).connect()

