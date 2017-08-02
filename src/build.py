# encoding=utf-8
from docker.client import DockerClient

import os
from docker.tls import TLSConfig
from docker.utils.utils import kwargs_from_env

IP = '115.29.146.79'
CERTS_DIR_PATH = '/home/zihua/Repository/violent_python/chapter10'

AUTH_CONFIG = (
    (
        os.path.join(CERTS_DIR_PATH, 'cert.pem'),
        os.path.join(CERTS_DIR_PATH, 'key.pem')
    ),
    os.path.join(CERTS_DIR_PATH, 'ca.pem')
)


def tls_config():
    from docker.tls import TLSConfig
    cert, _ = AUTH_CONFIG
    return TLSConfig(client_cert=cert, verify=False)


def docker_client(version='auto', base_url=None, tls=False, **kwargs):
    kwargs = kwargs_from_env(**kwargs)
    kwargs['version'] = version
    kwargs['base_url'] = base_url
    if tls:
        cert, _ = AUTH_CONFIG
        kwargs['tls'] = TLSConfig(client_cert=cert, verify=False)
    return DockerClient(**kwargs)


def build():
    client = docker_client(base_url='tcp://%s:2376' % IP, tls=True)
    client.images.pull("yzihua/system_ui")
    con = client.containers.run(image="yzihua/system_ui",
                                name="system_ui",
                                ports={'8991': 80},
                                detach=True)



if __name__ == '__main__':
    build()
