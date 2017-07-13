### Public network

ip: 10.74.128.87 ~ 10.74.128.89  
netmask: 255.255.255.0  
gateway: 10.74.128.254  
VLAN: 70

| ip             | name            | type    |
| ---            | ---             | ---     |
| 10.74.128.87   | switch          | static  |
| 10.74.128.88   | desktop PC      | static  |
| 10.74.128.89   | CentOS          | static  |

### Lab network

ip: 100.101.0.128  
netmask: 255.255.255.224  
gateway: 100.101.0.129  
VLAN: 166

| ip             | name            | type    |
| ---            | ---             | ---     |
| 100.101.0.130  | CentOS          | static  |
| 10.74.128.131  | TBD             | DHCP    |
| 10.74.128.158  | TBD             | DHCP    |