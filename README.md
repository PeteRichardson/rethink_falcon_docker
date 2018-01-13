# Running Rethink Falcon gunicorn in a Docker instance
This repo contains the files needed to build a docker container with RethinkDB, the Falcon python module for writing RESTful web services and a gunicorn WSGI server.

## Getting Started
1. Install Docker
2. Clone the repo
3. cd into the cloned directory
4. open a shell and type  
`docker-compose up`
5. open the rethinkdb admin web UI in a browser:
`http://localhost:9080`
6. open the sample app web UI in a browser:
 `http://localhost:9000` 

The source for the sample app is in myapp.py.

You can replace the web app code with your own Falcon app or api.