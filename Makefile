all: output.txt

.PHONY: all

packets/packet.bin:
	@cat packets/packet-1.bin \
		packets/packet-2.bin \
		packets/packet-3.bin \
		packets/packet-4.bin \
		packets/packet-5.bin \
		packets/packet-6.bin \
		packets/packet-7.bin \
		packets/packet-8.bin \
		packets/packet-9.bin \
		packets/packet-10.bin \
		packets/packet-11.bin \
		packets/packet-12.bin \
		packets/packet-13.bin \
		packets/packet-14.bin \
		packets/packet-15.bin \
		packets/packet-16.bin > packets/packet.bin

packets/packet-reformatted.bin: packets/packet.bin
	@./reformat.py

output.txt: inspect.py
	@./inspect.py > output.txt
