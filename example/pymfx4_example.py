import pymfx4
from pymfx4.mfx4device import mfx4Cut
from pymfx4.mffullindex import FullIndex
from pymfx4.mfconnection import mfx_endpoints, mfx_close_endpoints

import time

# connect to a MFX_4 EDI (Node=0). This function 
# will return a tuple of devices.
cutDevice = 0
for device in mfx_endpoints("192.168.3.117:4003", [0]):
    if isinstance(device, mfx4Cut):
        cutDevice = device

# print device info
print(cutDevice.SoftwareVersion.Value)
print(cutDevice.SoftwareDate.Value)
print(cutDevice.SoftwareTime.Value)

uploadSize = FullIndex(0, 0x200B, 0x0B) # Upload-Size-In-Bytes


def MyNotificationFunction(FI, Value):
    print(f"{FI} => {Value}")

cutDevice.SetNotification(uploadSize, 500, MyNotificationFunction)

for i in range(10):
    cutDevice.Set(uploadSize, f"{i*2}")
    time.sleep(1)

cutDevice.RemoveNotification(uploadSize)
mfx_close_endpoints()