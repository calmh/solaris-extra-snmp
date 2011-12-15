This is a small script to add additional useful variables for SNMP monitoring
under Solaris. It's known to be compatible with Solaris 11 Express and Solaris 11.
When deployed, it provides the following additional information:

    SNMPv2-SMI::enterprises.25359.1.1.1.0 = STRING: "Temp"
    SNMPv2-SMI::enterprises.25359.1.1.2.0 = Gauge32: 30
    SNMPv2-SMI::enterprises.25359.1.1.3.0 = STRING: "Degrees C"
    SNMPv2-SMI::enterprises.25359.1.2.1.0 = STRING: "ZFS ARC size"
    SNMPv2-SMI::enterprises.25359.1.2.2.0 = Gauge32: 2630303
    SNMPv2-SMI::enterprises.25359.1.2.3.0 = STRING: "KB"
    SNMPv2-SMI::enterprises.25359.1.3.1.0 = STRING: "ZFS ARC hits"
    SNMPv2-SMI::enterprises.25359.1.3.2.0 = Counter32: 908276151
    SNMPv2-SMI::enterprises.25359.1.3.3.0 = STRING: "number"
    SNMPv2-SMI::enterprises.25359.1.4.1.0 = STRING: "ZFS ARC misses"
    SNMPv2-SMI::enterprises.25359.1.4.2.0 = Counter32: 83416492
    SNMPv2-SMI::enterprises.25359.1.4.3.0 = STRING: "number"
    SNMPv2-SMI::enterprises.25359.1.5.1.0 = STRING: "ZFS read bytes"
    SNMPv2-SMI::enterprises.25359.1.5.2.0 = Counter32: 1359411320
    SNMPv2-SMI::enterprises.25359.1.5.3.0 = STRING: "KB"
    SNMPv2-SMI::enterprises.25359.1.6.1.0 = STRING: "ZFS readdir bytes"
    SNMPv2-SMI::enterprises.25359.1.6.2.0 = Counter32: 22022593
    SNMPv2-SMI::enterprises.25359.1.6.3.0 = STRING: "KB"
    SNMPv2-SMI::enterprises.25359.1.7.1.0 = STRING: "ZFS write bytes"
    SNMPv2-SMI::enterprises.25359.1.7.2.0 = Counter32: 4293706169
    SNMPv2-SMI::enterprises.25359.1.7.3.0 = STRING: "KB"

With this information, you can graph system temperature, ZFS ARC cache hit rate
and ZFS IO rate. To use, drop the script in for example /usr/local/bin, add the
following to /etc/net-snmp/snmp/snmpd.conf:

    pass .1.3.6.1.4.1.25359.1 /usr/local/bin/solaris-extra-snmp

and restart the net-snmp service. If you don't already use the net-snmp service
you will need to enable it and set community etc.

