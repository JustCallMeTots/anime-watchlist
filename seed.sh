rm -rf animapi/migrations
rm db.sqlite3
python manage.py migrate
python manage.py makemigrations animapi
python manage.py migrate animapi
python manage.py loaddata genre
python manage.py loaddata watcher
python manage.py loaddata watchlist
python manage.py loaddata anime

# Run chmod +x seed.sh in the terminal.
# run ./seed.sh in the terminal to run the commands
