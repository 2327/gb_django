python manage.py makemigrations
echo "migrations_created"

python manage.py migrate
echo "migrations_done"

# python manage.py dumpdata -e contenttypes -o db.json
