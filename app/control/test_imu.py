import time
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250

mpu = MPU9250(
    address_ak=AK8963_ADDRESS,
    address_mpu_master=MPU9050_ADDRESS_68,
    address_mpu_slave=None,
    bus=1,
    gfs=GFS_1000,
    afs=AFS_8G,
    mfs=AK8963_BIT_16,
    mode=AK8963_MODE_C100HZ
)
mpu.configure()

print("Testing GY-91 (MPU9250 + AK8963)...")
print("Reading for 10 seconds. Move the board around to see values change.\n")

for i in range(10):
    accel = mpu.readAccelerometerMaster()
    gyro = mpu.readGyroscopeMaster()
    mag = mpu.readMagnetometerMaster()
    temp = mpu.readTemperatureMaster()

    print(f"Accel: {accel}")
    print(f"Gyro:  {gyro}")
    print(f"Mag:   {mag}")
    print(f"Temp:  {temp}")
    print("---")
    time.sleep(1)
