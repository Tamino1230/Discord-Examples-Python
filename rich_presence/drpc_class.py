from pypresence import Presence
import time

class RPC:
    def __init__(self, client_id: int):
        """
        ### Example to activate DRPC:
        ```
        rpc = RPC("client id here")
        rpc.set_update("details", "state")
        rpc.connect()
        rpc.update_rpc()

        while True:
            try:
                print("sleep 15s")
                time.sleep(15)
            except Exception as e:
                print("Exited")
        ```
        """
        self.client_id = client_id
        self.rpc = Presence(self.client_id)
        self.start_time = time.time()
        self.details = None
        self.state = None
        self.party_size = None
        self.party_max = None
        self.buttons = []
        self.connected = False
        self.__author__ = "github.com/Tamino1230"


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
                    start=self.start_time,
                    buttons=self.buttons
                )
                return
               
            self.rpc.update(
                details=self.details,
                state=self.state,
                buttons=self.buttons
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

    def add_button(self, label: str, url: str) -> None:
        """
        Adds a button to the RPC (limit: 2).
        """
        if len(self.buttons) >= 2:
            print("You cannot add more than 2 buttons.")
            return

        if not url.startswith("https://") and not url.startswith("http://"):
            print(f'Your link "{url}" must start with "https://" or "http://"')
            return

        self.buttons.append({
            "label": label,
            "url": url
        })


if __name__ == "__main__":
    rpc = RPC("your client id")
    rpc.add_button("Button 1", "https://github.com/Tamino1230")
    rpc.add_button("Button 2", "https://github.com/Tamino1230")
    rpc.set_update("details", "state")
    rpc.connect()
    rpc.update_rpc()
    print(rpc.buttons)
    while True:
        try:
            print("staying alive (15s)")
            time.sleep(15)
        except KeyboardInterrupt:
            rpc.disconnect()
            print("Disconnected from RPC Server")
            break
        except Exception as e:
            rpc.disconnect()
            print("Disconnected from RPC Server")
            break