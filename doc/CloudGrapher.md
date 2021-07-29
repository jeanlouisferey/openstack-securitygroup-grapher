| Security group | Direction | IP type | Protocol | Port | Remote partner | 
| -------------- | --------- | ------- | -------- | ---- | -------------- | 
| default | egress | IPv4 | any | any | 0.0.0.0/0 |
| default | egress | IPv6 | any | any | 0.0.0.0/0 |
| default | ingress | IPv4 | any | any | default |
| default | ingress | IPv6 | any | any | default |
| PRIVATE_SG_BASTION_WAL | ingress | IPv4 | tcp | 2242 | 0.0.0.0/0 |
| PRIVATE_SG_BASTION_WAL | egress | IPv6 | any | any | 0.0.0.0/0 |
| PRIVATE_SG_BASTION_WAL | ingress | IPv4 | tcp | 22 | 0.0.0.0/0 |
| PRIVATE_SG_BASTION_WAL | ingress | IPv4 | tcp | 443 | 0.0.0.0/0 |
| PRIVATE_SG_BASTION_WAL | egress | IPv4 | any | any | 0.0.0.0/0 |
| PRIVATE_SG_BASTION_RP_PNB | egress | IPv4 | any | any | 0.0.0.0/0 |
| PRIVATE_SG_BASTION_RP_PNB | ingress | IPv4 | tcp | 443 | 0.0.0.0/0 |
| PRIVATE_SG_BASTION_RP_PNB | egress | IPv6 | any | any | 0.0.0.0/0 |
| PRIVATE_SG_BASTION_RP_PNB | ingress | IPv4 | 112 | any | 0.0.0.0/0 |
| PRIVATE_SG_BASTION_RP_PNB | ingress | IPv4 | tcp | 22 | 0.0.0.0/0 |