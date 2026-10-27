"""client.py - Equivalent of Client.java."""
import Pyro5.api


def main():
    try:
        # LocateRegistry.getRegistry("127.0.0.1", 9000)
        registry = Pyro5.api.locate_ns("127.0.0.1", 9000)
        # registry.lookup("laptop")
        laptop = Pyro5.api.Proxy(registry.lookup("laptop"))

        laptop_name = laptop.get_name()
        laptop_description = laptop.get_description()
        price = laptop.get_price()
        print("Name:" + laptop_name)
        print("Description: " + laptop_description)
        print("Price: " + str(price))
    except Exception as e:
        print("Exception in client side", e)


if __name__ == "__main__":
    main()