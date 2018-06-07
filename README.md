# CTFBoard Alpha

Written by @nsychev at 5 AM

Design advices by @vanyaklimenko

## License

[GLWTPL?](https://github.com/me-shaon/GLWTPL/blob/master/LICENSE) :)

## How to use

It's easy Django application.

### Debug mode

For debug purposes just run `python3 app/manage.py runserver`.

**Warning:** in this case scoreboards and static task files are not served correctly.

To use scoreboards, just change their directory to `app/tasks/static/boards` and they will be served to `/static/boards/`, not just `/boards/`.

Static task files cannot be served in this mode, please don't use `attachments` field and everything will be OK.

### Production mode

In production, I created docker-compose configuration.

```
touch db.sqlite3
python3 app/manage.py collectstatic
docker-compose up --build -d
```

Why do we need first line? Otherwise, docker will think that `db.sqlite3` is name of shared directory, not file.

In `nginx-platform.conf` there is example config of my webserver **on host machine** from Ugra CTF 2018. Also you can create docker container which will manage port 443 (or any other you want), but I don't prefer it because I serve many applications on the same server.

Nginx server handles TLS certificate, static files from `app/static/` and task static files from `${TASKS_DIR}/${TASK_NAME}/public/`.

### Configuration

All platform configuration is in `app/ctfboard/config.py`. You can find many useful (or not?) options there.

### Migrations

You won't find any tables in fresh database. So please run migrations:

```
python3 app/manage.py migrate
```

### Admin

To add teams and see flags there's Django default admin panel. Run this command to create admin account:

```
python3 app/manage.py createsuperuser
```

Then sign in to `https://url.com/admin/`.

### Tasks

Task layout description is [here](TASKS.md)

## Questions?

Feel free to ask me any questions about platform here: https://t.me/nsychev
