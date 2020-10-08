# -*- coding: utf-8 -*-

name = 'rapidjson'

version = '1.0.4-ta.1.1.0'

authors = [
    'benjamin.skinner',
    'tencent',
]

requires = [
    'python-3'
]

@early()
def private_build_requires():
    import sys
    if 'win' in str(sys.platform):
        return ['visual_studio']
    else:
        return ['gcc-7']

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10'],
    #['platform-linux', 'arch-x64'],
]

def commands():

     # Split and store version and package version
    split_versions = str(version).split('-')
    env.RAPIDJSON_VERSION.set(split_versions[0])
    env.RAPIDJSON_PACKAGE_VERSION.set(split_versions[1])

    env.RAPIDJSON_ROOT.set( "{root}" )
    env.RAPIDJSON_LIB_DIR.set( "{root}/lib" )
    env.RAPIDJSON_INCLUDE_DIR.set( "{root}/include" )

    env.PATH.append( "{root}/bin" )
