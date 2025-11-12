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

    