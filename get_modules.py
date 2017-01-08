#!/usr/bin/env python3

import os
import sys
import requests
import yaml
import git
import svn.remote
import zipfile
import argparse

def get_modules(yml_file, dest):
    f = open(yml_file)
    for data in yaml.load(f):
        if (not dest.endswith('/')):
            dest = dest + '/'
        if not 'version' in data:
            version = None
        else:
            version = data['version']
        download_module(data['url'], dest, data['name'], data['type'], version)
    f.close()

def download_module(src, dest, name, type, version):
    if os.path.exists(dest + name):
        return
    if type == 'git':
        download_git(src, dest + name, version)
    elif type == 'svn':
        download_svn(src, dest + name, version)
    elif type == 'zip':
        download_zip(src, dest, name)

def download_git(src, dest, version):
    if version is None:
        git.Repo.clone_from(src, dest)
    else:
        git.Repo.clone_from(src, dest, branch=version)

def download_svn(src, dest, version):
    r = svn.remote.RemoteClient(src)
    r.checkout(dest)

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

def create_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('modules',
                        help='list of modules to download')
    parser.add_argument('dest_dir',
                        help='dest directory to save modules')

    return parser

if __name__ == '__main__':
    args = create_argparser().parse_args()
    get_modules(args.modules, args.dest_dir)
