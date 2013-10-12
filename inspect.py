#!/usr/bin/env python2.7

import struct

from helpers import bytes_from_file

# steps, calories, skin temperature, perspiration, heart rate
# sleeping, awake, active, unknown

def print_contents():
    chunks = []
    current_chunk = ""

    markers = [0x29, 0x0c, 0x2b]
    names = ["0x29", "0x0c", "0x2b"]
    marker = 0

    for byte in bytes_from_file("packets/packet-reformatted.bin"):
        byte = ord(byte)

        if byte == 0x00 and \
                ord(current_chunk[-1]) in markers and \
                (ord(current_chunk[-1]) != markers[marker] or \
                    ord(current_chunk[-2]) == 0x00):
            chunks.append({
                "field_type": names[marker],
                "data": current_chunk[:-1]
            })

            # Keep track of which field we just saw
            marker = markers.index(ord(current_chunk[-1]))

            current_chunk = ""
        else:
            current_chunk += chr(byte)

    # Append the last chunk
    chunks.append({
        "field_type": "end",
        "data": current_chunk
    })

    print(len(chunks), "chunks found")
    #pprint([len(chunk["data"]) for chunk in chunks])

    # Strip 0x00 padding
    for i in xrange(len(chunks)):
        chunks[i]["data"] = chunks[i]["data"].rstrip(chr(0x00))

    #for chunk in chunks:
    #    (timestamp,) = struct.unpack_from("I", chunk["data"])

    #    if timestamp > 81469139:
    #        print "Weird timestamp:"
    #        print " ".join(["{:02x}".format(ord(byte)) for
    #            byte in chunk["data"]])

    def format_0x29(data):
        (timestamp,) = struct.unpack_from("I", data)

        extra = ""

        if len(data) > 4:
            extra = data[4:]

        extra = " ".join(["{:02X}".format(ord(byte)) for byte in extra])

        print "0x29: %d, extra: %s" % (timestamp, extra)

    def format_0x0c(data):
        (timestamp,) = struct.unpack_from("I", data)

        print "0x0c: %d" % (timestamp)

        data = data[4:]

        for i in xrange(0, len(data), 3):
            try:
                (field_type, value) = struct.unpack_from("<BH", data, offset=i)

                print "   type: %d (%02x), value: %d" % (field_type, field_type,
                        value)
            except:
                pass

    def format_0x2b(data):
        (timestamp,) = struct.unpack_from("I", data)

        print "0x2b: %d" % (timestamp)

    def format_end(data):
        print "end:", " ".join(["{:02X}".format(ord(byte)) for byte in data])

    formatters = {
        "0x29": format_0x29,
        "0x0c": format_0x0c,
        "0x2b": format_0x2b,
        "end": format_end
    }

    for chunk in chunks:
        formatters[chunk["field_type"]](chunk["data"])

print_contents()
