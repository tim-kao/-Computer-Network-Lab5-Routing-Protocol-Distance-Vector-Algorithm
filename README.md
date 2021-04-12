# Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm

## Overview ##
Lab 5: Routing Algorithm Distance Vector \
Implement the Bellman-Ford algorithm and run it on four separate machines.


## Demo ##
## Test Scenario ## 
![image](https://github.com/tim-kao/-Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm/blob/main/demo/test_scenario.png)

## Execution ##
![image](https://github.com/tim-kao/-Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm/blob/main/demo/execution.png)

[paris log](https://github.com/tim-kao/-Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm/blob/main/log/paris.log) \
[berlin log](https://github.com/tim-kao/-Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm/blob/main/log/berlin.log) \
[Vienna log](https://github.com/tim-kao/-Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm/blob/main/log/Vienna.log) \
[rome log](https://github.com/tim-kao/-Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm/blob/main/log/rome.log)

## Feature ##
1. Initialization and Start
2. Send the routing table to a router's neighbors
3. Receive the routing table from neighbors
4. Update the routing table based on (3)
##  Usage Examples ##
On Berlin run:
python3 dvrouter.py rome:1 paris:7 vienna:3

On Rome run:
python3 dvrouter.py berlin:1 vienna:1

On Vienna run:
python3 dvrouter.py berlin:3 rome:1 paris:2

On Paris run:
python3 dvrouter.py berlin:7 vienna:2
   
## Contributor ##
#### [Tim Kao](https://github.com/tim-kao) (UNI: sk4920)
