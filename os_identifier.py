__author__ = 'Roland'
import os
import socket
import platform


class OsIdentifier():

    def __init__(self):
        self.plataform = platform.platform()

    def get_os_type(self):
        if 'Linux' in self.plataform:
            return 'linux'
        elif 'Windows' in self.plataform:
            return 'windows'
        else:
            return 'mac'