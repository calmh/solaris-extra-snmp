# This project is not actively maintained

Issues and pull requests on this repository may not be acted on in a timely
manner, or at all.  You are of course welcome to use it anyway. You are even
more welcome to fork it and maintain the results.

![Unmaintained](https://nym.se/img/unmaintained.jpg)

This is a small script to add additional useful variables for SNMP monitoring
under Solaris. It's known to be compatible with Solaris 11 Express and Solaris 11.
When deployed, it provides the following additional information:

    NYMNETWORKS-MIB::zfsFilesystemName.1 = STRING: "ext"
    NYMNETWORKS-MIB::zfsFilesystemName.2 = STRING: "rpool"
    NYMNETWORKS-MIB::zfsFilesystemAvailableKB.1 = Gauge32: 1177910825
    NYMNETWORKS-MIB::zfsFilesystemAvailableKB.2 = Gauge32: 22363549
    NYMNETWORKS-MIB::zfsFilesystemUsedKB.1 = Gauge32: 737837527
    NYMNETWORKS-MIB::zfsFilesystemUsedKB.2 = Gauge32: 15827554
    NYMNETWORKS-MIB::zfsPoolHealth.1 = INTEGER: online(1)
    NYMNETWORKS-MIB::zfsPoolHealth.2 = INTEGER: online(1)
    NYMNETWORKS-MIB::zfsFilesystemAvailableMB.1 = Gauge32: 1150303
    NYMNETWORKS-MIB::zfsFilesystemAvailableMB.2 = Gauge32: 21839
    NYMNETWORKS-MIB::zfsFilesystemUsedMB.1 = Gauge32: 720544
    NYMNETWORKS-MIB::zfsFilesystemUsedMB.2 = Gauge32: 15456
    NYMNETWORKS-MIB::zfsARCSizeKB.0 = Gauge32: 4598931
    NYMNETWORKS-MIB::zfsARCMetadataSizeKB.0 = Gauge32: 191033
    NYMNETWORKS-MIB::zfsARCDataSizeKB.0 = Gauge32: 4407899
    NYMNETWORKS-MIB::zfsARCHits.0 = Counter32: 564613730
    NYMNETWORKS-MIB::zfsARCMisses.0 = Counter32: 18646010
    NYMNETWORKS-MIB::zfsL2ARCHits.0 = Counter32: 0
    NYMNETWORKS-MIB::zfsL2ARCMisses.0 = Counter32: 18646013
    NYMNETWORKS-MIB::zfsL2ARCReads.0 = Counter32: 0
    NYMNETWORKS-MIB::zfsL2ARCWrites.0 = Counter32: 0
    NYMNETWORKS-MIB::zfsReadKB.0 = Counter32: 765171103
    NYMNETWORKS-MIB::zfsReaddirKB.0 = Counter32: 6260406
    NYMNETWORKS-MIB::zfsWriteKB.0 = Counter32: 577324153

With this information, you can graph ZFS ARC size and hit rate, ZFS IO rate and
ZFS L2ARC hit rate and IO rate. Have a look in the MIB or in the source for
more detailed descriptions of the individual variables. If you add the `ipmi-snmp`
script, you'll get a basic temperature reading:

    NYMNETWORKS-MIB::tempSensorName.0 = STRING: "System Temp"
    NYMNETWORKS-MIB::tempSensorValue.0 = Gauge32: 20

If you have a NUT installation and add the `nut-snmp` script, youll get some
basic UPS stats:

    NYMNETWORKS-MIB::upsId.1 = STRING: "smartups"
    NYMNETWORKS-MIB::upsModel.1 = STRING: "Smart-UPS 750"
    NYMNETWORKS-MIB::upsManufacturer.1 = STRING: "American Power Conversion"
    NYMNETWORKS-MIB::upsSerial.1 = STRING: "AS1141221798"
    NYMNETWORKS-MIB::upsBatteryChargePercent.1 = Gauge32: 100
    NYMNETWORKS-MIB::upsBatteryRuntimeSec.1 = Gauge32: 2340
    NYMNETWORKS-MIB::upsBatteryVoltagedV.1 = Gauge32: 275
    NYMNETWORKS-MIB::upsBatteryNominalVoltagedV.1 = Gauge32: 240
    NYMNETWORKS-MIB::upsBatteryType.1 = STRING: "PbAc"
    NYMNETWORKS-MIB::upsStatus.1 = STRING: "OL"

To use, drop the scripts

    snmpresponse.py
    zfs-snmp
    ipmi-snmp
    nut-snmp

in for example `/usr/local/bin`, add the following to
`/etc/net-snmp/snmp/snmpd.conf`:

    pass .1.3.6.1.4.1.25359.1 /usr/local/bin/zfs-snmp
    pass .1.3.6.1.4.1.25359.2 /usr/local/bin/ipmi-snmp # Optional, for IPMI
    pass .1.3.6.1.4.1.25359.3 /usr/local/bin/nut-snmp # Optional, for NUT/UPS

and `svcadm restart net-snmp`. If you don't already use the net-snmp service
you will need to set community etc at the top of the file and `svcadm enable net-snmp`.

License
-------

2-Clause BSD

