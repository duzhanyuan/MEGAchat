#!/usr/bin/python2

# Links chromium stuff onto the webrtc tree. Must be run in webrtc tree's src directory
import subprocess
import os
import glob

if os.path.exists('./.get-chromium-deps-ran'):
    print("Already linked to chromium deps, skipping")
    exit(0)

def makelink(path, linked):
    if path:
        path='/'+path;
    os.system('ln -sfv '+cwd+'/chromium/src'+path+'/'+linked+' '+cwd+path)
    return

print("============================================================")
print("Linking paths in chromium tree to webrtc tree...")
cwd=os.getcwd();
makelink('', 'build')
makelink('', 'buildtools')
makelink('tools', 'clang')
makelink('tools', 'generate_library_loader')
makelink('tools', 'generate_stubs')
makelink('tools', 'gn')
makelink('tools', 'gyp')
makelink('tools', 'isolate_driver.py')
makelink('tools', 'memory')
makelink('tools', 'protoc_wrapper')
makelink('tools', 'python')
makelink('tools', 'protoc_wrapper')
makelink('tools', 'win')
makelink('tools', 'xdisplaycheck')
makelink('tools', 'android')
for dir in os.listdir('./chromium/src/third_party/'):
    if not os.path.isdir('./chromium/src/third_party/'+dir):
         continue
    makelink('third_party', dir)

open('./.get-chromium-deps-ran', 'w+').close()

