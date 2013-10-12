#!/usr/bin/env python2.7

from helpers import chunks_from_file

# Strip off the first two bytes of every 64-byte chunk
with open("packets/packet-reformatted.bin", "wb") as f:
    for message in chunks_from_file("packets/packet.bin"):
        f.write(message[2:])
