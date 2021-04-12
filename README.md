# Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm

## Overview ##
Lab 5: Routing Algorithm Distance Vector \
Implement the Bellman-Ford algorithm and run it on four separate machines.


## Demo ##
## Test Scenario ## 
![image](https://github.com/tim-kao/-Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm/blob/main/demo/test_scenario.png)

## Execution ##
![image](https://github.com/tim-kao/-Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm/blob/main/demo/execution.png)

[Paris log](https://github.com/tim-kao/-Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm/blob/main/log/Paris.log) \
[Berlin log](https://github.com/tim-kao/-Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm/blob/main/log/berlin.log) \
[Vienna log](https://github.com/tim-kao/-Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm/blob/main/log/Vienna.log) \
[Rome log](https://github.com/tim-kao/-Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm/blob/main/log/rome.log)

## Feature ##
1. Initialization and Start
2. Send the routing table to a router's neighbors
3. Receive the routing table from neighbors
4. Update the routing table based on (3)
##  Usage Examples ##
On Berlin (Node 0) run: python3 dvrouter.py rome:1 paris:7 vienna:3 \
On Rome (Node 1) run: python3 dvrouter.py berlin:1 vienna:1 \
On Vienna(Node 2) run: python3 dvrouter.py berlin:3 rome:1 paris:2 \
On Paris (Node 3) run: python3 dvrouter.py berlin:7 vienna:2 \
   
## Contributor ##
#### [Tim Kao](https://github.com/tim-kao) (UNI: sk4920)
