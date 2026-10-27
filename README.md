\# Python RMI Lab (Pyro5)



Python translation of a Java RMI project using \*\*Pyro5\*\* (Python Remote Objects).



| Java RMI                               | Python / Pyro5                              |

|----------------------------------------|---------------------------------------------|

| `Product.java`                         | `product.py`                                |

| `ProductImpl.java`                     | `ProductImpl` in `server.py`                |

| `ServerImpl.java`                      | `ServerImpl` in `server.py`                 |

| `Server.java`                          | `main()` in `server.py`                     |

| `Client.java`                          | `client.py`                                 |

| `rmiregistry` on port 9000             | `python -m Pyro5.nameserver -p 9000`        |

| `UnicastRemoteObject.exportObject`     | `daemon.register(obj)`                      |

| `registry.bind(name, stub)`            | `registry.register(name, uri)`              |

| `registry.lookup(name)`                | `registry.lookup(name)` + `Pyro5.api.Proxy` |



Objects bound by the server: `laptop`, `ram`, `bag`, `charger`.



\## Setup

```

pip install Pyro5

```



\## Run (three terminals, in this order)

1\. Registry:

```

python -m Pyro5.nameserver -n 127.0.0.1 -p 9000

```

2\. Server:

```

python server.py

```

3\. Client:

```

python client.py

```

Expected client output:

```

Name:Laptop

Description: Lenovo laptop

Price: 800000.0

```

