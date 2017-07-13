import docker
import json

client = docker.from_env()
print client.containers.run('alpine', ['echo', 'hello word!'])

contain = client.containers.run('bfirsh/reticulate-splines', detach=True)
print contain.id
info = client.info()

print info
jso = json.dumps(info)
print jso

for c in client.containers.list():
    print c.logs()
    id = c.id

print id

c = client.containers.get(id)
print c.logs()

for img in client.images.list():
    print img.id

# image = client.images.pull('nginx')

print 'pull success !'
# print image.id



