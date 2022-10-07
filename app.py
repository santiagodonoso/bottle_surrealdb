from bottle import default_app, response, run, get, static_file, view
import x

##############################
@get("/static/<file_name>")
def _(file_name):
  return static_file(file_name, root="./static")

##############################
@get("/")
@view("view_index.html")
def _():
  return


##############################
@get("/api-get-all-items")
def _():
  try:
    db_response = x.surrealdb("SELECT * FROM item")
    return db_response[0]['result']
  except Exception as ex:
    response.status = 400
    return {"info":str(ex)}

##############################


##############################
import api_create_item


##############################
try:
  import production
except:
  run(host="127.0.0.1", port=3333, debug=True, reloader=True)


