# run on open network at a certain port
# py manage.py runserver 0.0.0.0:8082
rung:
	set BUILD_MAP=FALSE&&gunicorn -w 4 config:gunicorn:dev
run:
	set BUILD_MAP=FALSE&&py manage.py runserver

runb:
	set BUILD_MAP=TRUE&&py manage.py runserver

# linux version
# python3 -m venv venv
migrations_linux:
	pipenv run python3 manage.py makemigrations --skip-checks
	pipenv run python3 manage.py migrate --skip-checks

# python3 -m venv venv
migrations:
	pipenv run py manage.py makemigrations --skip-checks
	pipenv run py manage.py migrate --skip-checks

# Make migrations and implement them for all installed apps
makemigrations:
	pipenv run py manage.py makemigrations --skip-checks

migrate:
	pipenv run py manage.py migrate --skip-checks
	pipenv run py manage.py migrate --database="Ivory Coast" --skip-checks
	pipenv run py manage.py migrate --database="Benin" --skip-checks

# Check SQL commands to be run by a certain migration script
# sql:
# 	pipenv run py manage.py sqlmigrate polls 0001

# Checks for any problems in your project without making migrations or touching the database.
check:
	pipenv run py manage.py check

# Hops into the interactive Python shell and play around with the free API Django gives you. To invoke the Python shell, use this command:
shell:
	pipenv run py manage.py shell

# create superuser
suser:
	pipenv run py manage.py createsuperuser

# create a message file for translation
makem:
	python manage.py makemessages -l fr

# compile messages that have been created
compilem:
	python manage.py compilemessages


format:
	djhtml .

# Gathering static files in a single directory so you can serve them easily.
preparestatics:
	python manage.py collectstatic


test:
	py manage.py test

# python ./scripts/data_import_scripts/import_plantations_new.py "Ivory Coast"


celery:
	celery -A cajulab_remote_sensing_dashboard worker --loglevel=info

clear_celery:
	celery -A cajulab_remote_sensing_dashboard purge


# 
# Compute commands
compute:
	pipenv run python ./scripts/data_compute_scripts/build_satellite_prediction_computed_data.py "$(country)"

# TODO Ename this
compute_spacing_nursery:
	pipenv run python ./scripts/data_compute_scripts/tree_spacing_recommandations.py "$(country)"


db_backup:
	chmod +x ./config/backup/db_backup.sh
	sudo ./config/backup/db_backup.sh backup
	
setup:
	pipenv run python ./scripts/setup_scripts/add_countries.py
	pipenv run python ./scripts/setup_scripts/add_contries_datasets.py
	pipenv run python ./scripts/setup_scripts/add_organization_and_role.py

cache:
	pipenv run python manage.py createcachetable --database="default"
	pipenv run python manage.py createcachetable --database="Ivory Coast"
	pipenv run python manage.py createcachetable --database="Benin"
# Update cron tab to run the job daily
# crontab -e
# 0 2 * * * sudo ./~/project_dir/Caju-Dashboard-v2/config/backup/db_backup.sh backup
# 0 2 * * * sudo ./~/project_dir/Caju-Dashboard-v2/config/backup/db_backup.sh backup
#  python3 ./scripts/separate_countries.py