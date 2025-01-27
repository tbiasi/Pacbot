#!/usr/bin/env python3

import robomodules
import os
from messages import MsgType

ADDRESS = os.environ.get("BIND_ADDRESS","192.168.0.100")
PORT = os.environ.get("BIND_PORT", 11297)

def main():
    server = robomodules.Server(ADDRESS, PORT, MsgType)
    server.run()

if __name__ == "__main__":
    main()
