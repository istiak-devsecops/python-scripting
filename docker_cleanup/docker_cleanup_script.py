# install docker SDK for python first

# pip install docker

import docker #importing docker SDK

class DockerCleaner:
    def __init__(self):
        self.client = docker.from_env()
        print("Docker cleaner initialized...")

    def clean_containers(self):
        print(f"cleaning stopped containers...")
        containers = self.client.containers.list(all=True, filters={"status":"exited"})
        for container in containers:
            try:
                print(f"Removing container: {container.name}")
                container.remove()
            except Exception as e:
                print(f"Failed to remove {container.name}: {e}")
    
    def clean_images(self):
        print("Removing images...")
        images = self.client.images.list(filters={"dangling": True})
        for image in images:
            try:
                print(f"Removing image: {image.short_id}")
                self.client.images.remove(image.id)
            except Exception as e:
                print(f"Failed to remove {image.short_id}:{e}")

    def clean_networks(self):
        print("clearning unused network...")
        networks = self.client.networks.list()
        for network in networks:
            if network.name not in ["bridge","host","none"]:
                try:
                    print(f"Removing network: {network.name}")
                    network.remvoe()
                except Exception as e:
                    print(f"Failed to remvoe {network.name}: {e}")

    def clean_volumes(self):
        print("cleaning unused volumes...")
        volumes = self.client.volumes.list(filter={"dangling": True})
        for volume in volumes:
            try:
                print(f"Removing volume: {volume.name}")
                volume.remove()
            except Exception as e:
                print(f"Failed to remove {volume.name}: {e}")

    
    def main(self):
        print("starting docker cleanup...")
        self.clean_containers()
        self.clean_images()
        self.clean_networks()
        self.clean_volumes()
        print("cleanup complete...")


if __name__ == "__main__":
    cleaner = DockerCleaner()
    cleaner.main()