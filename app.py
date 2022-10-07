from bottle import default_app, request, response, run, get, static_file, view
import x

##############################
@get("/static/<file_name>")
def _(file_name):
  return static_file(file_name, root="./static")

##############################
@get("/")
@view("view_index.html")
def _(): 
  is_spa = True if request.headers.get('HTTP_SPA') else False
  return dict(title="Home", is_spa=is_spa)

##############################
@get("/create-item")
@view("view_create_item.html")
def _():
  print('HTTP_SPA', request.headers.get('HTTP_SPA'))
  is_spa = True if request.headers.get('HTTP_SPA') else False
  return dict(title="Create item", is_spa=is_spa)  

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


