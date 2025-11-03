import subprocess
import optparse
parse_object = optparse.OptionParser()
parse_object.add_option("-i","--interface",dest ="interface",help = "You can select your interface with -i <interface> or -interface <interface>")
parse_object.add_option("-m","--mac",dest="mac_adress",help="You can select the MAC address with -m <mac address> or -mac <mac address>")

(user_inputs,arguments) = parse_object.parse_args()

user_interface = user_inputs.interface
user_mac_adress = user_inputs.mac_adress

def mac_changer():
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_adress])
    subprocess.call(["ifconfig",user_interface,"up"])
