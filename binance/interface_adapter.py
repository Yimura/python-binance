import socket
import requests
from requests import adapters
from urllib3.poolmanager import PoolManager

class InterfaceAdapter(adapters.HTTPAdapter):
    def __init__(self, **kwargs):
        self.iface = kwargs.pop('iface', None)
        super(InterfaceAdapter, self).__init__(**kwargs)

    def _socket_options(self):
        if self.iface is None:
            return []
        else:
            return [(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, self.iface)]

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            socket_options=self._socket_options()
        )