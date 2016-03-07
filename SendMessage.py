#导入我们需要用到的包和类并且起别名
import sys
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi

# Connect device
device = mr.waitForConnection(1.0,'M3LDU15430022319')  # waitForConnection(Interval,'device_id')
if not device:
    print >>sys.stderr, 'fail'
    sys.exit(1)

# define Start Activity
componentName = 'com.android.mms/.ui.BootActivity'
# Define specified activity
device.startActivity(component=componentName)
# Set Interval between operations
mr.sleep(1.0)

# new a message
device.touch(57, 747, 'DOWN_AND_UP')
mr.sleep(1.0)
# Enter recipient
device.type('18007928637')

# Count of message
for i in range(0,.1):
    device.touch(187, 402, 'DOWN_AND_UP')
    device.type('Hi Auntie, How are you today? Are you Okay? I hope so. Are you happy? I hope so')
    mr.sleep(1.0)

    # Send the message
    device.touch(432, 380, 'DOWN_AND_UP')
    mr.sleep(1.0)
    device.touch(51, 752, 'DOWN_AND_UP')
    mr.sleep(1.0)

# Take Snapshot
mr.sleep(1.0)
result = device.takeSnapshot()

#  save to file
result.writrToFile('D:\\MessageResult.png', 'png');



