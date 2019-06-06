#!/bin/sh

docker-compose run \
  --rm pythicles_app /bin/sh \
  -c "python ./bin/connection_loader.py && python manage.py createsuperuser"

docker-compose stop pythicles_postgres
