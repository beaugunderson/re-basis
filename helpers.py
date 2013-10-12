def chunks_from_file(filename, chunk_size=64):
    """A generator that yields each chunk_size-byte chunk of a binary file"""
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunk_size)

            if chunk:
                yield chunk
            else:
                break

def bytes_from_file(filename, chunk_size=8192):
    """A generator that yields each byte of a binary file"""
    for chunk in chunks_from_file(filename, chunk_size):
        for byte in chunk:
            yield byte
