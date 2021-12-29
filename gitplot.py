import docker
import os
from os import walk

# Try to copy file from the container to the host using docker.

# Get the container name: https://stackoverflow.com/a/52988227
container_id = open("/proc/1/cpuset", "r").read().removeprefix("/docker/").strip()

print('container_id : ' + container_id)

client = docker.from_env()

container = client.containers.get(container_id)

print(container)

f = open("test.txt", "a")
f.write("Come from container")
f.close()

print(os.getcwd())

filenames = next(walk(os.getcwd()), (None, None, []))[2]  # [] if no file

print(filenames)

# docker cp ${container_id}:/opt/project/test.txt /home/test/gitplot/test.txt
# https://stackoverflow.com/questions/46390309/how-to-copy-a-file-from-host-to-container-using-docker-py-docker-sdk

# Fail because the method get_archive provided by the docker SDK: https://docker-py.readthedocs.io/en/stable/containers.html#docker.models.containers.Container.get_archive
# retrieve a file in the docker container and there is no way to put the file in the host machine.
