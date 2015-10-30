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
	print "Let's create classrooms in sequence"
	number1 = raw_input("First sequence classroom number (normally 1): ")
	number2 = raw_input("Second sequence classroom number: ")
	names = ['computea', 'computeb', 'cboot', 'control', 'bserver']
	for num in range(int(number1),int(number2)+1):
		for name in names:
			vm_name = name+str(num)+".onapp.labs"
			if (name == "computea") or (name == "computeb"):
				vm_template = api.templates.get("OnApp_compute")					
			elif name == "cboot":
				vm_template = api.templates.get("OnApp_cboot")
			elif name == "control":
				vm_template = api.templates.get("OnApp_control")
			else:
				vm_template = api.templates.get("OnApp_bserver")
				
			vm_cluster = api.clusters.get("Lille-Cluster")
			vm_params = params.VM(name=vm_name, cluster=vm_cluster, template=vm_template)
			try:
				api.vms.add(vm=vm_params)
				print "Virtual machine '%s' added." % vm_name
				
			except Exception as ex:
				print "Adding virtual machine '%s' failed %s" % (vm_name,ex)
				
			try:
				vm = api.vms.get(name=vm_name)
				if (name == "computea") or (name == "computeb"):
					nicnumber=0
					networks = ['ext', 'mgmt', 'storage', 'prov', 'app']
					for network in networks:
						nicnumber +=1
						nic_name = "nic"+str(nicnumber)
						nic_interface = "virtio"
						nic_network = vm_cluster.networks.get(name="class"+str(num)+"_"+network)
						nic_params = params.NIC(name=nic_name, interface=nic_interface, network=nic_network)
						vm.nics.add(nic_params)
					for disk in vm.disks.list():
						disk.set_alias(name+str(num)+".onapp.labs_Disk1")
						disk.update()					
				elif name == "cboot":
					nicnumber=0
					networks = ['ext', 'mgmt', 'storage', 'app']
					for network in networks:
						nicnumber +=1
						nic_name = "nic"+str(nicnumber)
						if nicnumber == 1:
							nic_interface = "virtio"
						else:
							nic_interface = "e1000"
						nic_network = vm_cluster.networks.get(name="class"+str(num)+"_"+network)
						nic_params = params.NIC(name=nic_name, interface=nic_interface, network=nic_network)
						vm.nics.add(nic_params)
			
					for disk in vm.disks.list():
						disk.set_alias(disk.get_name().replace("1",str(num),1))
						disk.update()
				elif name == "control":
					nicnumber=0
					networks = ['ext', 'mgmt']
					for network in networks:
						nicnumber +=1
						nic_name = "nic"+str(nicnumber)
						nic_interface = "virtio"
						nic_network = vm_cluster.networks.get(name="class"+str(num)+"_"+network)
						nic_params = params.NIC(name=nic_name, interface=nic_interface, network=nic_network)
						vm.nics.add(nic_params)
					for disk in vm.disks.list():
						disk.set_alias(name+str(num)+".onapp.labs_Disk1")
						disk.update()
				else:
					nicnumber=0
					networks = ['ext', 'mgmt', 'storage', 'prov']
					for network in networks:
						nicnumber +=1
						nic_name = "nic"+str(nicnumber)
						nic_interface = "virtio"
						nic_network = vm_cluster.networks.get(name="class"+str(num)+"_"+network)
						nic_params = params.NIC(name=nic_name, interface=nic_interface, network=nic_network)
						vm.nics.add(nic_params)
					for disk in vm.disks.list():
						disk.set_alias(name+str(num)+".onapp.labs_Disk1")
						disk.update()
			except Exception as ex:
				print "Adding network interface to '%s' failed: %s" % (vm.get_name(), ex)
			
	api.disconnect()

except Exception as ex:
	print "Unexpected error: %s" % ex
