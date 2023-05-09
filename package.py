name = 'rapidjson'

version = '1.1.0.sse.1.0.0'

authors = [
    'RapidJson',
]

description = '''Json parser for C++'''

with scope('config') as c:
    import os
    c.release_packages_path = os.environ['SSE_REZ_REPO_RELEASE_EXT']

requires = [
]

private_build_requires = [
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-centos-7'],
]

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.REZ_RAPIDJSON_ROOT = '{root}'

uuid = 'repository.rapidjson'

