# Pythicles

A Python 3-based blog app built on Django.

## Installation

Please, use [Docker](https://docs.docker.com/) to install this app.

Run the below setup command to build the containers, create a new database and run the migrations.
Please note, the command drops any existing database.
```
$ ./bin/setup.sh
```

Create a superuser account:
```
$ ./bin/create_superuser.sh
```

Start the app in development mode:
```
$ ./bin/start.sh
```

Finally, load [http://localhost](http://localhost) in your browser.
The admin panel is available at [http://localhost/admin](http://localhost/admin)


## Running the tests

```
$ ./bin/test.sh
```
