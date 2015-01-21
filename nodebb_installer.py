# coding: utf-8
from __future__ import unicode_literals

import subprocess
import sys
import os
import urllib2
import json


def clone_repo(url, target_path, name):
    if os.path.exists(target_path):
        print '"%s" parece estar instalado ya' % name
        return

    args = ['git', 'clone', url, target_path]
    print 'Ejecutando:', ' '.join(args)
    subprocess.call(args)

def npm_install():
    sp = subprocess.Popen(['npm', 'install'], cwd=NODEBB_DIR)
    sp.communicate()


def should_install(repo):
    return repo['name'].startswith(('nodebb-plugin', 'nodebb-theme-exodo'))

NODEBB_DIR = '/vagrant/nodebb'
clone_repo('git://github.com/designcreateplay/NodeBB.git', NODEBB_DIR, 'nodebb')


repos_json = urllib2.urlopen('https://api.github.com/users/exo-do/repos').read()
repos = filter(should_install, json.loads(repos_json))

for repo in repos:
    path = os.path.join(NODEBB_DIR, 'node_modules', repo['name'])
    clone_repo(url=repo['git_url'], target_path=path, name=repo['name'])

npm_install()
print '\n\nFin de la historia. Dale duro al desarrollo shur!'
