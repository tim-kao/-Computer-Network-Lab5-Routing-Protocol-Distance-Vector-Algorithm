# -Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm

## Overview ##
Lab 5: Routing Algorithm Distance Vector \
Implement Bellman-Ford algorithm and run on four separate machines.

## Demo ##
Test Scenario
![image](https://github.com/tim-kao/-Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm/blob/main/demo/test_scenario.png)
Execution
![image](https://github.com/tim-kao/-Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm/blob/main/demo/execution.png)

[paris log](https://github.com/tim-kao/-Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm/blob/main/log/paris.log) \
[berlin log](https://github.com/tim-kao/-Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm/blob/main/log/berlin.log) \
[minsk log](https://github.com/tim-kao/-Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm/blob/main/log/minsk.log) \
[khartoum log](https://github.com/tim-kao/-Computer-Network-Lab5-Routing-Protocol-Distance-Vector-Algorithm/blob/main/log/khartoum.log)

## Feature ##
1. Initialization and Start
2. Send the routing table to a router's neighbors
3. Receive the routing table from neighbors
4. Update the routing table based on (3)
##  Usage Examples ##
paris.clic.cs.columbia.edu		python3 dvrouter.py paris:0 berlin:7 minsk:2
berlin.clic.cs.columbia.edu		python3 dvrouter.py paris:7 khartoum:1 berlin:0 minsk:3
minsk.clic.cs.columbia.edu		python3 dvrouter.py paris:2 khartoum:1 berlin:3 minsk:0
khartoum.clic.cs.columbia.edu 	dvrouter.py khartoum:0 berlin:1 minsk:1
   
## Contributor ##
#### [Tim Kao](https://github.com/tim-kao) (UNI: sk4920)
