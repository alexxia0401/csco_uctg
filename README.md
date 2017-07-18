### Public network                                                                 
                                                                                   
IP: 10.74.128.87 ~ 10.74.128.89                                                    
netmask: 255.255.255.0                                                             
gateway: 10.74.128.254                                                             
VLAN: 70                                                                           
                                                                                   
| IP             | device          | type    |                                     
| ---            | ---             | ---     |                                     
| 10.74.128.87   | switch VLAN 70  | static  |                                     
| 10.74.128.88   | desktop PC      | static  |                                     
| 10.74.128.89   | CentOS 6.x      | static  |                                     
                                                                                   
### Lab network                                                                    
                                                                                   
IP: 100.101.0.128                                                                  
netmask: 255.255.255.224                                                           
gateway: 100.101.0.129                                                             
VLAN: 166                                                                          
                                                                                   
| IP             | device          | type    |                                     
| ---            | ---             | ---     |                                     
| 100.101.0.130  | switch VLAN 166 | static  |                                     
| 100.101.0.131  | CentOS 6.x      | static  |                                     
| 100.101.0.132  | TBD             | DHCP    |  
| 100.101.0.158  | TBD             | DHCP    |

### Full name of abbreviation
* 3PCC - 3rd-Party Call Control
* FCS - First Commercial Shipment
* DUT - Device Under Test
* RU
