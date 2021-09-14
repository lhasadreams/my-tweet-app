Run de demo:
$ vi ./templates/index.html (and modify the text)
$ docker build -t mytweetapp:0.2 .
$ docker run -it -p 5000:5000 -d mytweetapp:0.2

Open a browser and go to http://localhost:5000 (and refresh the page)

$ docker images
$ lw-scanner evaluate mytweetapp 0.2 --save --scan-library-packages --html


Clean up things:
$ docker rm -f $(docker ps -q)

$ cp Dockerfile.vuln Dockerfile
$ cp ./templates/index.html.ORG ./templates/index.html
 
