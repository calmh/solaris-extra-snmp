This is a small script to add additional useful variables for SNMP monitoring
under Solaris. It's known to be compatible with Solaris 11 Express and Solaris 11.
When deployed, it provides the following additional information:

    NYMNETWORKS-MIB::zfsFilesystemName.1 = STRING: "ext"
    NYMNETWORKS-MIB::zfsFilesystemName.2 = STRING: "rpool"
    NYMNETWORKS-MIB::zfsFilesystemAvailableKB.1 = Gauge32: 1177910825
    NYMNETWORKS-MIB::zfsFilesystemAvailableKB.2 = Gauge32: 22363549
    NYMNETWORKS-MIB::zfsFilesystemUsedKB.1 = Gauge32: 737837527
    NYMNETWORKS-MIB::zfsFilesystemUsedKB.2 = Gauge32: 15827554
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
    NYMNETWORKS-MIB::tempSensorName.0 = STRING: "System Temp"
    NYMNETWORKS-MIB::tempSensorValue.0 = Gauge32: 20

With this information, you can graph ZFS ARC size and hit rate, ZFS IO rate and
ZFS L2ARC hit rate and IO rate. To use, drop the scripts in for example
/usr/local/bin, add the following to /etc/net-snmp/snmp/snmpd.conf:

    pass .1.3.6.1.4.1.25359.1 /usr/local/bin/zfs-snmp

and restart the net-snmp service. If you don't already use the net-snmp service
you will need to enable it and set community etc.

