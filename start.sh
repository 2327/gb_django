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

# start app
# module nameis necessary!
# python -m django startapp mainapp

# filling default fields
# TODO: current state is not working
# python manage.py fill_db

python manage.py runserver

#python manage.py makemigrations
#python manage.py migrate

# python manage.py createsuperuser

#
# Import/Export database data
#
#./manage.py dumpdata --indent 2 > db.json
#./manage.py dumpdata mainapp --indent 2 > mainapp.json
#./manage.py dumpdata mainapp.product --indent 2 > mainapp_.json
# ./manage.py dumpdata --exclude auth.permission --indent 2 > db.json
#
# refresh database exclude fileds --exclude auth.permission
# ./manage.py loaddata db.json
#
