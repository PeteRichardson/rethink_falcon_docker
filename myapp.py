import rethinkdb as r
import json

DB="myapp"
TABLE="weblog"

conn = r.connect(host="db")
try:
	r.db_create(DB).run(conn)
	r.db(DB).table_create(TABLE).run(conn)
except r.errors.ReqlOpFailedError:
	pass

def app(environ, start_response):
        data = { "message": "Hello, Pete!" }
        result = r.db(DB).table(TABLE).insert(data).run(conn)
        start_response("200 OK", [
            ("Content-Type", "text/json"),
            ("Content-Length", str(len(json.dumps(result))))
        ])
        return json.dumps(result)



