This is a small script to add additional useful variables for SNMP monitoring
under Solaris. It's known to be compatible with Solaris 11 Express and Solaris 11.
When deployed, it provides the following additional information:

    SNMPv2-SMI::enterprises.25359.1.2.1.0 = STRING: "ZFS ARC size"
    SNMPv2-SMI::enterprises.25359.1.2.2.0 = Gauge32: 3855140
    SNMPv2-SMI::enterprises.25359.1.2.3.0 = STRING: "KB"
    SNMPv2-SMI::enterprises.25359.1.3.1.0 = STRING: "ZFS ARC hits"
    SNMPv2-SMI::enterprises.25359.1.3.2.0 = Counter32: 525804554
    SNMPv2-SMI::enterprises.25359.1.3.3.0 = STRING: "number"
    SNMPv2-SMI::enterprises.25359.1.4.1.0 = STRING: "ZFS ARC misses"
    SNMPv2-SMI::enterprises.25359.1.4.2.0 = Counter32: 16839622
    SNMPv2-SMI::enterprises.25359.1.4.3.0 = STRING: "number"
    SNMPv2-SMI::enterprises.25359.1.5.1.0 = STRING: "ZFS read bytes"
    SNMPv2-SMI::enterprises.25359.1.5.2.0 = Counter32: 717075497
    SNMPv2-SMI::enterprises.25359.1.5.3.0 = STRING: "KB"
    SNMPv2-SMI::enterprises.25359.1.6.1.0 = STRING: "ZFS readdir bytes"
    SNMPv2-SMI::enterprises.25359.1.6.2.0 = Counter32: 5622970
    SNMPv2-SMI::enterprises.25359.1.6.3.0 = STRING: "KB"
    SNMPv2-SMI::enterprises.25359.1.7.1.0 = STRING: "ZFS write bytes"
    SNMPv2-SMI::enterprises.25359.1.7.2.0 = Counter32: 540218951
    SNMPv2-SMI::enterprises.25359.1.7.3.0 = STRING: "KB"
    SNMPv2-SMI::enterprises.25359.1.8.1.0 = STRING: "ZFS L2ARC hits"
    SNMPv2-SMI::enterprises.25359.1.8.2.0 = Counter32: 0
    SNMPv2-SMI::enterprises.25359.1.8.3.0 = STRING: "number"
    SNMPv2-SMI::enterprises.25359.1.9.1.0 = STRING: "ZFS L2ARC misses"
    SNMPv2-SMI::enterprises.25359.1.9.2.0 = Counter32: 16839622
    SNMPv2-SMI::enterprises.25359.1.9.3.0 = STRING: "number"
    SNMPv2-SMI::enterprises.25359.1.10.1.0 = STRING: "ZFS L2ARC read bytes"
    SNMPv2-SMI::enterprises.25359.1.10.2.0 = Counter32: 0
    SNMPv2-SMI::enterprises.25359.1.10.3.0 = STRING: "KB"
    SNMPv2-SMI::enterprises.25359.1.11.1.0 = STRING: "ZFS L2ARC write bytes"
    SNMPv2-SMI::enterprises.25359.1.11.2.0 = Counter32: 0
    SNMPv2-SMI::enterprises.25359.1.11.3.0 = STRING: "KB"

With this information, you can graph ZFS ARC size and hit rate, ZFS IO rate and
ZFS L2ARC hit rate and IO rate. To use, drop the scripts in for example
/usr/local/bin, add the following to /etc/net-snmp/snmp/snmpd.conf:

    pass .1.3.6.1.4.1.25359.1 /usr/local/bin/zfs-snmp

and restart the net-snmp service. If you don't already use the net-snmp service
you will need to enable it and set community etc.

