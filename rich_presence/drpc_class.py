from pypresence import Presence
import time

class RPC:
    def __init__(self, client_id: int):
        """
        ### Example to activate DRPC:
        ```
        rpc_class = RPC("client id here")
        rpc_class.set_update("details", "state")
        rpc_class.connect()
        rpc_class.update_rpc()

        while True:
            try:
                print("sleep 15s")
                time.sleep(15)
            except Exception as e:
                print("Exited")
        ```
        """
        self.rpc = Presence(client_id)
        self.client_id = client_id
        self.start_time = time.time()
        self.details = None
        self.state = None
        self.connected = False

    def set_update(self, details: str, state: str):
        """
        Sets the following variables:
        - details
        - state
        """
        self.details = details
        self.state = state

    def connect(self):
        """
        Connects you to the Discord RPC Server
        """
        if self.connect == True:
            print("You are already connected to the RPC Server")
        try:
            self.rpc.connect()
            self.connected = True
        except Exception as e:
            print("Error accured while connecting to the RPC:", e)
            

    def update_rpc(self, new_start_time: bool = False):
        """
        Updates the set rpc with `set_update(details, state)` and updates it on discord
        """
        if self.connected != True:
            print("You are not connected to the RPC Server!")
            return
        if self.details != None and self.state != None:
            if new_start_time == True:
                #* renew the time
                self.start_time = time.time()
                self.rpc.update(
                    details=self.details,
                    state=self.state,
                    start=self.start_time
                )
                return
               
            self.rpc.update(
                details=self.details,
                state=self.state
            )
            return
        print("Details and State cannot be None!")

    def clear_rpc(self):
        """
        Clears the currently displayed RPC on Discord (If connected)
        """
        if self.connect != True:
            print("You are not connected to the RPC Server!")
            return
        self.rpc.clear()
    
    def disconnect(self):
        """
        Disconnects yourself from the rpc server (If connected)
        """
        if self.connect != True:
            print("You are not connected to the RPC Server!")
            return
        self.rpc.close()


if __name__ == "__main__":
    rpc_class = RPC("client id here")
    rpc_class.set_update("details", "state")
    rpc_class.connect()
    rpc_class.update_rpc()

    print("went through all commands.")
    while True:
        try:
            print("staying alive (15s)")
            time.sleep(15)
        except Exception as e:
            print("Exited drpc")