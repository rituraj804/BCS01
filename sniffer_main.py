import socket
import struct
# import textwrap


HOST = socket.gethostbyname(socket.gethostname())
# the public network interface
# socket() -- create a new socket object
# gethostbyname() -- map a hostname to its IP number
# gethostname() -- return the current hostname


def main():

    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    conn.bind((HOST, 0))
    # create a raw socket and bind it to the public interface
    # AF_INET, AF_UNIX -- socket domains (first argument to socket() call)
    # SOCK_STREAM, SOCK_DGRAM, SOCK_RAW -- socket types (second argument)

    conn.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    # SEt SOCKet OPTions true (1) to INCL HDR for IP PROTOcol level

    conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    #  "receive all(RCVALL)" Control-Code packets set option "RCVALL_ON" i.e. Promiscous mode

    while True:

        raw_data, addr = conn.recvfrom(65536)
        # Receive everything from socket 65536(input) and returning "the data" into raw_data and "the address" into addr

        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        # run ethernet_frame function to extract dest_mac, src_mac, eth_proto and data from raw_data recd from socket

        print('\nEthernet Frame:')
        print('Destination : {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, eth_proto))


# unpack ethernet frame
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    # unpack function to unpack from "data[:14]" according to format string "! 6s 6s H"
    # single 6 byte string, another 6 byte string and then unsigned short
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]


# return properly formatted MAC address
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()


main()
