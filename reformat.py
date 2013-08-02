#!/usr/bin/env python2.7

def chunks_from_file(filename, chunk_size=64):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunk_size)

            if chunk:
                yield chunk
            else:
                break

# Strip off the first two bytes of every 64-byte chunk
with open("packets/packet-reformatted.bin", "wb") as f:
    for message in chunks_from_file("packets/packet.bin"):
        f.write(message[2:])
