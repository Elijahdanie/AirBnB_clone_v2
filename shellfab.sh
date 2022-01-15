#!/bin/bash
fab -f ./2-do_deploy_web_static.py do_deploy:archive_path=./versions/web_static_202211517939.tgz -i ./sshakey.pub -u ubuntu
