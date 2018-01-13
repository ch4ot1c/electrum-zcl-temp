#!/usr/bin/env python3

# A simple script (python3) that connects to a server and displays block headers via socket

import json
import socket

def get_from_electrum(method, params=[]):
    params = ['1001']
    s = socket.create_connection(('35.224.186.7', 50001))  # or ssl 500002
    s.send(json.dumps({"id": "0", "method": method, "params": params}).encode() + b'\n')
    return json.loads(s.recv(99999)[:-1].decode())

h = get_from_electrum('blockchain.block.get_header')    
print(h)
