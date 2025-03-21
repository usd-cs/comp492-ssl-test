## Example Application with SSL

This is an example application using SSL certificates with nginx and a flask web server.

## Setup

Edit the nginx.conf file replacing GROUP.dedyn.io with your group's domain name.

To deploy, use Docker compose.

```
docker compose up -d
```

Check that everything is working by running the compose ps command.

```
docker compose ps
```

This should give you something similar to the following, the important parts being the STATUS as "Up" for both containers.

```
NAME               IMAGE                  COMMAND                  SERVICE   CREATED          STATUS          PORTS
ssl-test-proxy-1   nginx:latest           "/docker-entrypoint.…"   proxy     35 seconds ago   Up 34 seconds   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp, 80/tcp, 0.0.0.0:8080->8080/tcp, [::]:8080->8080/tcp
ssl-test-web-1     ssl-test-web           "python3 app.py"         web       35 seconds ago   Up 34 seconds
```

After the application starts, navigate to `https://GROUP.dedyn.io:8080` in your web browser, which should display a webpage
that reads, "Hello SECURE World!".

Going to `http://GROUP.dedyn.io:8000` should redirect you to the HTTPS version on port 8080.


Stop and remove the containers as follows.

```
docker compose down
```
