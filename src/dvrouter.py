import os
import json
import sys
import socket
import time
import getopt
import heapq

host = '127.0.0.1'
AnyIP = '0.0.0.0'
uid = 4920
BUF_SIZE = 4096
# ONLINE = True
ONLINE = True
TIMER = 10
suffix = ".clic.cs.columbia.edu"
class Node:
    # Build a UDP socket, store your arguments
    # Initialize your routing table, etc.

    def __init__(self, port, args):
        self.neighbors = []
        # Build a lookup table
        self.route_table = dict()
        self.port = port
        self.addr = (AnyIP, self.port)
        print('Initialize an udp socket at' + str(self.addr))
        self.udpSerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udpSerSock.bind(self.addr)
        self.udpSerSock.settimeout(TIMER)
        self.hostname = socket.gethostname()
        self.parse_nodes(args)
        pass

    # Dump current routing table to a text file
    # This is going to be especially useful for debugging!
    def dump_routing_table(self):
        print('hostname: ' + self.hostname)
        for k, v in self.route_table.items():
            print('cost to ', k, ' is ', v)
        pass

    # Parse Arguments
    # Initialize list of neighbors and T = 0 of RIP Table
    # Only call this once
    def parse_nodes(self, nodes):
        self.route_table[self.hostname] = 0
        for node in nodes:
            k, v = node.split(':')
            self.route_table[k] = int(v)
            if self.route_table[k] > 0:
                self.neighbors.append(k)
        pass

    # Send all neighbors your current routing table
    def send_routing_table(self):
        try:
            if self.route_table:
                dataframe = json.dumps(self.route_table, indent=4).encode()
                for neighbor in self.neighbors:
                    neighbor_host = neighbor + suffix
                    print('sending routing table to ' + neighbor_host)
                    self.udpSerSock.sendto(dataframe, (neighbor_host, self.port))
        except Exception as e:
            print('send_routing_table error e = ', e)

        pass

    # Receive data from a neighbor of their routing table
    # Update our rating table as needed
    def inbound(self):
        try:
            route, addr = self.udpSerSock.recvfrom(BUF_SIZE)
            if route:
                print('Receiving data from host:' + str(addr) + ' with data:' + route.decode('utf-8'))
                print('starting update routing table')
                self.update_routing_table(json.loads(route.decode()))
                print('update routing table complete')
        except Exception as e:
            print('inbound error e = ', e)
        pass

    # Called from inbound. Update Routing Table given what neighbor told you
    # Bellman Ford
    def update_routing_table(self, routing):

        h = []
        for city, cost in routing.items():
            heapq.heappush(h, (cost, city))
        dummy_cost, v = heapq.heappop(h)
        while h:
            c, y = heapq.heappop(h)
            # Dx(y) = minv{cx,v + Dv(y)}, x: local, v: neighbor, y: v's neighbors
            if y not in self.route_table:
                self.route_table[y] = c + self.route_table[v]
            else:
                self.route_table[y] = min(self.route_table[y], c + self.route_table[v])
        pass


    def close(self):
        self.udpSerSock.close()


def main():
    # Turns: ["-p" "8000", "berlin:1", "Vienna:1"] to ("-p", "8000"), ["berlin:1", "Vienna:1"]
    # If no -p passed you get
    # ["berlin:1", "Vienna:1"] to (-p, None), ["berlin:1", "Vienna:1"]
    options, cities = getopt.getopt(sys.argv[1:], "p:")

    print(cities)   # ['rome:1', 'paris:7', 'vienna:3']
    try:
        port = int(options[0][1])
    except Exception as e:
        if ONLINE:
            port = 30000 + os.getuid()
        else:
            port = 30000 + uid
    node = Node(port, cities)
    node.dump_routing_table()
    print('start in 3 seconds')
    time.sleep(3)

    while True:
        try:
            # I'll leave this to you to implement
            # Should be obvious which order of functions to call in what order

            # It should converge super-fast without the timer!
            # But feel free to use sleep()
            # both for troubleshooting, and minimize risk of overloading CLIC
            # Although Please Remove any sleep in final submission!
            node.send_routing_table()
            node.inbound()
            print('new table is updated as follows')
            node.dump_routing_table()
            # time.sleep(2)
        # Use CTRL-C to exit
        # You do NOT need to worry of updating routing table
        # if a node drops!
        # Show final routing table for checking if RIP worked
        except KeyboardInterrupt:
            node.dump_routing_table()
            node.close()
            break


if __name__ == '__main__':
    main()
