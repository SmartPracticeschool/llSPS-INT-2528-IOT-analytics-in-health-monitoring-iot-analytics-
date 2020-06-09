import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
#Provide your IBM Watson Device Credentials
organization = "924c70"
deviceType = "Healthmonitor"
deviceId = "987654"
authMethod = "token"
authToken = "987654321"
def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)#Commands
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()
# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()
while True:
        ag=random.randint(15,60)
        pul=random.randint(40, 60)
        #print(hum)
        temp =random.randint(30, 80)
        #Send Temperature & Humidity to IBM Watson
        bpsys=random.randint(90,120)
        bpdia=random.randint(80,89)
        data = { 'Age': ag,'Temperature' : temp, 'Systolic': bpsys ,'Diastolic': bpdia, 'Pulse': pul}
        #print (data)
        def myOnPublishCallback():
            print ("Published  Age= %s years" % ag,"Temperature = %s F" % temp, "Pulse = %s ppm" % pul, "BP = %s"% bpsys,"/%s" % bpdia,"to IBM Watson")
        success = deviceCli.publishEvent("Weather", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(2)
        deviceCli.commandCallback = myCommandCallback
# Disconnect the device and application from the cloud
deviceCli.disconnect()
