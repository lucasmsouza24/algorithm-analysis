destination = "192.168.10.1"

def send_package(package, destination):
    print(f'Sent {package} packet to {destination}')

def xx():
    for i in range(1, 100_000):
        send_package(i, destination)

xx()