from ovirtsdk.api import API
from ovirtsdk.xml import params
import getpass
import time

connection = raw_input("Url of engine (in format https://server): ")
user = raw_input("Username: ")
passwd = getpass.getpass("Password for " + user + ": ")

try:
    api = API (url=connection,
           username=user,
           password=passwd,
           ca_file="ca.crt")
    print "Connected to %s successfully!" % api.get_product_info().name
    vm_name = "classroom-eu.onapp.labs"
    vm_cluster = api.clusters.get(name="Lille-Cluster")
    vm_template = api.templates.get(name="OnApp_classroom")
    vm_params = params.VM(name=vm_name,cluster=vm_cluster,template=vm_template)
    try:
        api.vms.add(vm_params)
        
    except Exception as ex:
        print "Error creating VM: %s" % ex
    time.sleep(10)
    vm = api.vms.get(name=vm_name)
    try:
        print "Let's define classroom number of networks in sequence"
        number1 = raw_input("First sequence classroom number (normally 1): ")
        number2 = raw_input("Second sequence classroom number: ")
        networks = ['ext', 'storage']
        count = 0
        inc = 0
        number = 0
        for network in networks:
            if count == 1:
                inc = 10
            count=1             
            for number in range (int(number1), int(number2)+1):
                nic_name = "nic"+str(number+inc)
                nic_interface = "virtio"
                nic_network = vm_cluster.networks.get(name="class"+str(number)+"_"+network)
                nic_params = params.NIC(name=nic_name, interface=nic_interface, network=nic_network)
                vm.nics.add(nic_params)
        nic_name= "nic"+str(int(number2)*2+1)
        nic_interface = "virtio"
        nic_network = vm_cluster.networks.get(name="external")
        nic_params = params.NIC(name=nic_name, interface=nic_interface, network=nic_network)
        vm.nics.add(nic_params)
    except Exception as ex:
        print "Adding network machine '%s' failed %s" % (vm_name,ex)    
    try:
        vm.start(
                    action=params.Action(
                        vm=params.VM(
                            initialization=params.Initialization(
                                cloud_init=params.CloudInit(
                                    host=params.Host(address=vm_name),
                            network_configuration=params.NetworkConfiguration(
                                nics=params.Nics(
                                    nic=[params.NIC(
                                        name="eth0",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="192.168.1.1",
                                                netmask="255.255.255.0",
                                                gateway="192.168.0.1"
                                            )
                                        )
                                    ),
                                         params.NIC(
                                        name="eth1",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="192.168.2.1",
                                                netmask="255.255.255.0",
                                                gateway="192.168.0.1"
                                            )
                                        )
                                    ),
                                         params.NIC(
                                        name="eth2",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="192.168.3.1",
                                                netmask="255.255.255.0",
                                                gateway="192.168.0.1"
                                            )
                                        )
                                    ),
                                         params.NIC(
                                        name="eth3",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="192.168.4.1",
                                                netmask="255.255.255.0",
                                                gateway="192.168.0.1"
                                            )
                                        )
                                    ),
                                         params.NIC(
                                        name="eth4",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="192.168.5.1",
                                                netmask="255.255.255.0",
                                                gateway="192.168.0.1"
                                            )
                                        )
                                    ),
                                         params.NIC(
                                        name="eth5",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="192.168.6.1",
                                                netmask="255.255.255.0",
                                                gateway="192.168.0.1"
                                            )
                                        )
                                    ),
                                         params.NIC(
                                        name="eth6",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="192.168.7.1",
                                                netmask="255.255.255.0",
                                                gateway="192.168.0.1"
                                            )
                                        )
                                    ),
                                         params.NIC(
                                        name="eth7",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="192.168.8.1",
                                                netmask="255.255.255.0",
                                                gateway="192.168.0.1"
                                            )
                                        )
                                    ),
                                         params.NIC(
                                        name="eth8",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="192.168.9.1",
                                                netmask="255.255.255.0",
                                                gateway="192.168.0.1"
                                            )
                                        )
                                    ),
                                         params.NIC(
                                        name="eth9",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="192.168.10.1",
                                                netmask="255.255.255.0",
                                                gateway="192.168.0.1"
                                            )
                                        )
                                    ),
                                        params.NIC(
                                        name="eth10",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="172.25.1.1",
                                                netmask="255.255.255.0"
                                            )
                                        )
                                        ),                               
                                         params.NIC(
                                        name="eth11",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="172.25.2.1",
                                                netmask="255.255.255.0"
                                            )
                                        )
                                        ),
                                         params.NIC(
                                        name="eth12",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="172.25.3.1",
                                                netmask="255.255.255.0"
                                            )
                                        )
                                        ),
                                         params.NIC(
                                        name="eth13",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="172.25.4.1",
                                                netmask="255.255.255.0"
                                            )
                                        )
                                        ),
                                         params.NIC(
                                        name="eth14",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="172.25.5.1",
                                                netmask="255.255.255.0"
                                            )
                                        )
                                        ),
                                         params.NIC(
                                        name="eth15",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="172.25.6.1",
                                                netmask="255.255.255.0"
                                            )
                                        )
                                        ),
                                         params.NIC(
                                        name="eth16",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="172.25.7.1",
                                                netmask="255.255.255.0"
                                            )
                                        )
                                        ),
                                         params.NIC(
                                        name="eth17",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="172.25.8.1",
                                                netmask="255.255.255.0"
                                            )
                                        )
                                        ),
                                         params.NIC(
                                        name="eth18",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="172.25.9.1",
                                                netmask="255.255.255.0"
                                            )
                                        )
                                        ),
                                         params.NIC(
                                        name="eth19",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="172.25.10.1",
                                                netmask="255.255.255.0"
                                            )
                                        )
                                        ),
                                    ]
                                    )
                            )
                                )
                            )
                        )
                    )
                )
    except Exception as ex:
        print "Configuring virtual machine '%s' failed %s" % (vm_name,ex)   
except Exception as ex:
    print "Unexpected error: %s" % ex
