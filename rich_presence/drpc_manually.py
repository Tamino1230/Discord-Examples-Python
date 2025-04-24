from pypresence import Presence
import time

CLIENT_ID = "your client id"

rpc = Presence(CLIENT_ID)
rpc.connect()

start = time.time()

rpc.update(
    details="Example for details",
    state="Example for state",
    start=start
)

print("drpc is active now")

try:
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    print("Exiting RPC...")
finally:
    rpc.close()
