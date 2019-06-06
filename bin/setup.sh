#!/bin/sh

docker-compose stop pythicles_app pythicles_postgres

docker-compose build

rm -rf postgres

docker-compose up -d pythicles_postgres

docker-compose run \
  --rm pythicles_app /bin/sh \
  -c "python ./bin/setup_db.py && python manage.py migrate"

docker-compose stop pythicles_postgres

echo "Setup completed"
