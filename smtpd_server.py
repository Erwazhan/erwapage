from aiosmtpd.controller import Controller
from aiosmtpd.handlers import Debugging

if __name__ == '__main__':
    controller = Controller(Debugging, hostname='localhost', port=1025)
    controller.start()
    print('SMTP server running on localhost:1025')
