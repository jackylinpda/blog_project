#!/usr/bin/python
# -*- coding: utf-8 -*-
# module name:fabfile
# author:linjiafa
# create time: 2018-3-15
# modify time: 2018-3-15

from fabric.api import env, run
#from fabric.operations import sudo

GIT_REPO = 'https://github.com/jackylinpda/blog_project.git'

env.user = 'root'
env.use_ssh_config = True
#env.key_filename = 'C:/putty/ssh_key/TENCENT_SSH_KEY'
#SSH主机名，在~/.ssh/config文件中指定
env.hosts = ['VM_0_3_centos']
#SSH端口号
#env.port = '22'


def deploy():
    source_folder = '/root/django/blog_project'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../bin/pip3.6 install -r requirements.txt &&
        ../bin/python3.6 manage.py collectstatic --noinput &&
        ../bin/python3.6 manage.py migrate
        """.format(source_folder))
    run('systemctl restart gunicorn')
    run('systemctl restart nginx')