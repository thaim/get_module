#!/usr/bin/env python

import os
import sys
import requests
import yaml
import git
import zipfile

def get_modules(yml_file, dest):
    for data in yaml.load(file(yml_file)):
        if (not dest.endswith('/')):
            dest = dest + '/'
        download_module(data['url'], dest, data['name'], data['type'], data['version'])

def download_module(src, dest, name, type, version):
    if type == 'git':
        download_git(src, dest + name, version)
    elif type == 'zip':
        download_zip(src, dest, name)

def download_git(src, dest, version):
    git.Repo.clone_from(src, dest)

def download_zip(src, dest, name):
    filename = download_file(src, dest)
    zfile = zipfile.ZipFile(filename, "r")
    zfile.extractall(dest)
    os.rename(dest+zfile.namelist()[0].split("/")[0], dest+name)
    os.remove(filename)

def download_file(url, destdir):
    filename = destdir + url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        return filename

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        print 'Usage: python %s <modules.yml> <dest_dir>' % args[0]
        sys.exit(1)
    get_modules(args[1], args[2])
