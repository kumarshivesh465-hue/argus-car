from mpu9250_jmc import MPU9250
import time

mpu = MPU9250()

print("Testing GY-91 (MPU9250 + AK8963 + BMP280)...")
print("Reading for 10 seconds. Move the board around to see values change.\n")

for i in range(10):
    accel = mpu.readAccel()
    gyro = mpu.readGyro()
    mag = mpu.readMagnet()

    print(f"Accel (g):  X={accel['x']:.2f}  Y={accel['y']:.2f}  Z={accel['z']:.2f}")
    print(f"Gyro (dps): X={gyro['x']:.2f}  Y={gyro['y']:.2f}  Z={gyro['z']:.2f}")
    print(f"Mag (uT):   X={mag['x']:.2f}  Y={mag['y']:.2f}  Z={mag['z']:.2f}")
    print("---")
    time.sleep(1)
