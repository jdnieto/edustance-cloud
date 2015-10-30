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
	api.disconnect()

except Exception as ex:
	print "Unexpected error: %s" % ex
