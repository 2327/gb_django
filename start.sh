#!/bin/bash - 
#===============================================================================
#
#          FILE: start.sh
# 
#         USAGE: ./start.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 01/24/2019 11:32
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

python manage.py runserver

#python manage.py makemigrations
#python manage.py migrate

# python manage.py createsuperuser

#
# Импорт/Экспорт базона
#
#./manage.py dumpdata --indent 2 > db.json
#./manage.py dumpdata mainapp --indent 2 > mainapp.json
#./manage.py dumpdata mainapp.product --indent 2 > mainapp_.json
# ./manage.py dumpdata --exclude auth.permission --indent 2 > db.json
#
# можно обавлять, исключая --exclude auth.permission
# ./manage.py loaddata db.json
#
