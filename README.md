# container-port-host
A very simple port host for a container - a flask container that will run on a specified port (defaults to 5000 or whatever the ENV variable PORT is).

```
docker run -e PORT=8080 purplepixie/container-port-host
```

For example would run on port 8080 and if connected would say ```Hello on 8080```.

