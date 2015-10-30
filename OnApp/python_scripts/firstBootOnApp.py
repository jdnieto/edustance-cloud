from ovirtsdk.api import API
from ovirtsdk.xml import params
import getpass

connection = raw_input("Url of engine (in format https://server): ")
user = raw_input("Username: ")
passwd = getpass.getpass("Password for " + user + ": ")

try:
    api = API (url=connection,
           username=user,
           password=passwd,
           ca_file="ca.crt")
    
    print "Connected to %s successfully!" % api.get_product_info().name
except Exception as ex:
        print "Failed to connect to API: %s" % ex
print "Let's firstboot classrooms in sequence"
number1 = raw_input("First sequence classroom number (normally 1): ")
number2 = raw_input("Second sequence classroom number: ")
names = ['computea', 'computeb', 'control', 'bserver']    
for name in names:
    for num in range(int(number1),int(number2)+1):
        nic1 = int(num)
        nic2 = int(num) + 100
        nic3 = int(num) + 200
        nic4 = int(num) + 210
        try:
            vmachine = api.vms.get(name=name+str(num)+".onapp.labs")
            print vmachine.get_name()
        except Exception as ex:
            print "Failed to retrieve VM: %s" % ex
        try:
            if (name == 'control'):
                vmachine.start(
                    action=params.Action(
                        vm=params.VM(
                            initialization=params.Initialization(
                                cloud_init=params.CloudInit(
                                    host=params.Host(address=name+str(num)+".onapp.labs"),
                            network_configuration=params.NetworkConfiguration(
                                nics=params.Nics(
                                    nic=[params.NIC(
                                        name="eth0",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="192.168."+str(nic1)+".12",
                                                netmask="255.255.255.0",
                                                gateway="192.168."+str(nic1)+".1"
                                            )
                                        )
                                    ),
                                        params.NIC(
                                        name="eth1",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="172.25."+str(nic2)+".12",
                                                netmask="255.255.255.0"
                                            )
                                        )
                                        )
                                    ]
                                    )
                            )
                                )
                            )
                        )
                    )
                )
            else:
                if name == "computea":
                    end = "10"
                elif name == "computeb":
                    end = "11"
                else:
                    end = "13"
                vmachine.start(
                    action=params.Action(
                        vm=params.VM(
                            initialization=params.Initialization(
                                cloud_init=params.CloudInit(
                                    host=params.Host(address=name+str(num)+".onapp.labs"),
                            network_configuration=params.NetworkConfiguration(
                                nics=params.Nics(
                                    nic=[params.NIC(
                                        name="eth0",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="192.168."+str(nic1)+"."+end,
                                                netmask="255.255.255.0",
                                                gateway="192.168."+str(nic1)+".1"
                                            )
                                        )
                                    ),
                                        params.NIC(
                                        name="eth1",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="172.25."+str(nic2)+"."+end,
                                                netmask="255.255.255.0"
                                            )
                                        )
                                        ),
                                        params.NIC(
                                        name="eth2",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="172.25."+str(nic3)+"."+end,
                                                netmask="255.255.255.0"
                                            )
                                        )
                                        ),
                                        params.NIC(
                                        name="eth3",
                                        boot_protocol="static",
                                        on_boot=True,
                                        network=params.Network(
                                            ip=params.IP(
                                                address="172.25."+str(nic4)+"."+end,
                                                netmask="255.255.255.0"
                                            )
                                        )
                                        )
                                         
                                    ]
                                    )
                            )
                                )
                            )
                        )
                    )
                )
        except Exception as ex:
            print "Failed to start VM: %s" % ex
