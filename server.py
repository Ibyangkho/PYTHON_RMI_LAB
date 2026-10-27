"""server.py - Equivalent of Server.java, ProductImpl.java and ServerImpl.java.

Requires the registry (Pyro5 name server) to be running on 127.0.0.1:9000:
    python -m Pyro5.nameserver -n 127.0.0.1 -p 9000
"""
import Pyro5.api
from product import Product


# ---- ProductImpl.java ----
@Pyro5.api.expose
class ProductImpl(Product):
    # Parametrized constructor
    def __init__(self, new_name, new_description, new_price):
        self.name = new_name
        self.description = new_description
        self.price = new_price

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price


# ---- ServerImpl.java: (empty in the Java version; hosts the daemon here) ----
class ServerImpl:
    def __init__(self, host="127.0.0.1"):
        # Like System.setProperty("java.rmi.server.hostname", "127.0.0.1")
        self.daemon = Pyro5.api.Daemon(host=host)

    def export_object(self, obj):
        # Like UnicastRemoteObject.exportObject(p, 0)
        return self.daemon.register(obj)

    def start(self):
        self.daemon.requestLoop()


# ---- Server.java (main) ----
def main():
    try:
        print("Server is booting....")
        server = ServerImpl("127.0.0.1")

        # Create the product objects
        p1 = ProductImpl("Laptop", "Lenovo laptop", 800000.0)
        p2 = ProductImpl("Mobile", "MI 9 mobile", 24000.0)
        p3 = ProductImpl("Bag", "Branded bag", 800.0)
        p4 = ProductImpl("Charger", "MI Charger", 230.0)

        # Export all objects before registering them
        stub1 = server.export_object(p1)
        stub2 = server.export_object(p2)
        stub3 = server.export_object(p3)
        stub4 = server.export_object(p4)

        # Get the registry (LocateRegistry.getRegistry("127.0.0.1", 9000))
        registry = Pyro5.api.locate_ns("127.0.0.1", 9000)

        # Bind the exported objects so clients can look them up
        registry.register("laptop", stub1)
        registry.register("ram", stub2)
        registry.register("bag", stub3)
        registry.register("charger", stub4)

        print("Objects bound: laptop, ram, bag, charger")
        server.start()
    except Exception as e:
        print("Server error", e)


if __name__ == "__main__":
    main()