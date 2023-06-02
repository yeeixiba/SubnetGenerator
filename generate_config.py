def create_configuration_file(subnet_details, filename, war_template=False):
    if war_template:
        template = """
set template DC_WAR_PA-5220 config  network interface aggregate-ethernet ae1 layer3 units ae1.{vlan_id} tag {vlan_id}
set template DC_WAR_PA-5220 config  network interface aggregate-ethernet ae1 layer3 units ae1.{vlan_id} ipv6 neighbor-discovery router-advertisement enable no
set template DC_WAR_PA-5220 config  network interface aggregate-ethernet ae1 layer3 units ae1.{vlan_id} ndp-proxy enabled no
set template DC_WAR_PA-5220 config  network interface aggregate-ethernet ae1 layer3 units ae1.{vlan_id} adjust-tcp-mss enable no
set template DC_WAR_PA-5220 config  network interface aggregate-ethernet ae1 layer3 units ae1.{vlan_id} ip {default_gateway_cidr}
set template DC_WAR_PA-5220 config  network interface aggregate-ethernet ae1 layer3 units ae1.{vlan_id} interface-management-profile "Ping Only"
set template DC_WAR_PA-5220 config  network interface aggregate-ethernet ae1 layer3 units ae1.{vlan_id} comment {subnet_name}

set template DC_WAR_PA-5220 config  network virtual-router default interface ae1.{vlan_id}
set template DC_WAR_PA-5220 config  vsys vsys1 import network interface ae1.{vlan_id}

set template DC_WAR_PA-5220 config  vsys vsys1 zone {zone_name} network enable-packet-buffer-protection yes
set template DC_WAR_PA-5220 config  vsys vsys1 zone {zone_name} network layer3 ae1.{vlan_id}

set device-group WAR_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO AD" from {zone_name}
set device-group WAR_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO AD-1" from {zone_name}
set device-group WAR_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO ZABBIX" from {zone_name}
set device-group WAR_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS ZABBIX TO SERVERS" to {zone_name}
set device-group WAR_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO SNOW" from {zone_name}
set device-group WAR_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO LOGSYSTEM" from {zone_name}
set device-group WAR_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO WSUS" from {zone_name}
set device-group WAR_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO TSM" from {zone_name}
set device-group WAR_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO SCCM" from {zone_name}
set device-group WAR_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS SCCM TO SERVERS" to {zone_name}
set device-group WAR_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO PKI" from {zone_name}
set device-group WAR_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO SEPM" from {zone_name}
set device-group WAR_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO EDR" from {zone_name}
set device-group WAR_DC_PA-5220_vsys1 pre-rulebase security rules "DENY FROM" from {zone_name}
set device-group WAR_DC_PA-5220_vsys1 pre-rulebase security rules "DENY TO" to {zone_name}

##### CONFIG ON msz16sw03s 04s #####
sys
vlan {vlan_id}
 description {zone_name}
 name {zone_name}
 q
 
interface Eth-Trunk40
 port trunk allow-pass vlan {vlan_id}
 
interface Eth-Trunk41
 port trunk allow-pass vlan {vlan_id}

commit
q
save
y
 
##### CONFIG ON msz16sw05s 06s #####
sys
vlan {vlan_id}
 description {zone_name}
 name {zone_name}
 q

commit
q
save
y

"""
    else:
        template = """
##### CONFIG ON PANORAMA #####
set template DC_WRO_PA-5220 config  network interface aggregate-ethernet ae1 layer3 units ae1.{vlan_id} tag {vlan_id}
set template DC_WRO_PA-5220 config  network interface aggregate-ethernet ae1 layer3 units ae1.{vlan_id} ipv6 neighbor-discovery router-advertisement enable no
set template DC_WRO_PA-5220 config  network interface aggregate-ethernet ae1 layer3 units ae1.{vlan_id} ndp-proxy enabled no
set template DC_WRO_PA-5220 config  network interface aggregate-ethernet ae1 layer3 units ae1.{vlan_id} adjust-tcp-mss enable no
set template DC_WRO_PA-5220 config  network interface aggregate-ethernet ae1 layer3 units ae1.{vlan_id} ip {default_gateway_cidr}
set template DC_WRO_PA-5220 config  network interface aggregate-ethernet ae1 layer3 units ae1.{vlan_id} interface-management-profile "Ping Only"
set template DC_WRO_PA-5220 config  network interface aggregate-ethernet ae1 layer3 units ae1.{vlan_id} comment {subnet_name}

set template DC_WRO_PA-5220 config  network virtual-router default interface ae1.{vlan_id}
set template DC_WRO_PA-5220 config vsys vsys1 import network interface ae1.{vlan_id}

set template DC_WRO_PA-5220 config  vsys vsys1 zone {zone_name} network enable-packet-buffer-protection yes
set template DC_WRO_PA-5220 config  vsys vsys1 zone {zone_name} network layer3 ae1.{vlan_id}

set device-group WRO_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO AD" from {zone_name}
set device-group WRO_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO AD-1" from {zone_name}
set device-group WRO_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO ZABBIX" from {zone_name}
set device-group WRO_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS ZABBIX TO SERVERS" to {zone_name}
set device-group WRO_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO SNOW" from {zone_name}
set device-group WRO_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO LOGSYSTEM" from {zone_name}
set device-group WRO_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO WSUS" from {zone_name}
set device-group WRO_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO TSM" from {zone_name}
set device-group WRO_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO SCCM" from {zone_name}
set device-group WRO_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS SCCM TO SERVERS" to {zone_name}
set device-group WRO_DC_PA-5220_vsys1 pre-rulebase security rules "ACCESS TO PKI" from {zone_name}
set device-group WRO_DC_PA-5220_vsys1 pre-rulebase security rules "DENY FROM" from {zone_name}
set device-group WRO_DC_PA-5220_vsys1 pre-rulebase security rules "DENY TO" to {zone_name}

##### CONFIG ON wro30sw03s 04s #####
sys
vlan {vlan_id}
 description {zone_name}
 name {zone_name}
 q
 
interface Eth-Trunk40
 port trunk allow-pass vlan {vlan_id}
 
interface Eth-Trunk41
 port trunk allow-pass vlan {vlan_id}

commit
q
save
y
 
##### CONFIG ON wro30sw05s 06s #####
sys
vlan {vlan_id}
 description {zone_name}
 name {zone_name}
 q

commit
q
save
y

"""

    config_text = template.format(**subnet_details)
    with open(filename, "w") as file:
        file.write(config_text)
