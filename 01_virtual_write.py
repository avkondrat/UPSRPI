import BlynkLib
import time

BLYNK_AUTH = 'bOp4kFHopWDCVz1rO6_EaOaL7lSCLEoV'
blynk = BlynkLib.Blynk(BLYNK_AUTH,
                       server='127.0.0.1',        # set server address
                       port=8080                       # set server port
)

tmr_start_time = time.time()
while True:
    blynk.run()

    t = time.time()
    if t - tmr_start_time > 1:
        print("1 sec elapsed, sending data to the server...")
        blynk.virtual_write(0, "time:" + str(t))
        tmr_start_time += 10

