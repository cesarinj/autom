from ncclient import manager
import json
# create a variable object that represents the NETCONF session
m = manager.connect(
         host="192.168.1.28",
         port=830,
         username="cisco",
         password="cisco123!",
         hostkey_verify=False
         )

# one connected to the remote device using NETCONF
# display the device capabilities (supported YANG models)
print("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
    print(capability)
    
    with open('capabilities.json', 'a') as file:
        json.dump(capability, file, indent=4)

