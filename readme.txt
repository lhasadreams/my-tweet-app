Run de demo:
$ vi ./templates/index.html (and modify the text)

Clean up things:
$ docker stop 36569e2d6fad
$ docker rm 36569e2d6fad

$ cp Dockerfile.vuln Dockerfile
$ cp ./templates/index.html.ORG ./templates/index.html
 
