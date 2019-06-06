#!/bin/sh

docker-compose run \
  --rm pythicles_app /bin/sh \
  -c "python ./bin/connection_loader.py && python manage.py test"

docker-compose stop pythicles_postgres
