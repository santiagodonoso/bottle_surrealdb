from bottle import default_app, request, response, run, get, post
import x

##############################
@get("/")
def _():
  pass


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
# api-create-item
import api_create_item


##############################
@get("/items")
def _():
  try:
    x.validate_page_number()
    return "x"
  except Exception as ex:
    response.status = 400
    return {"info":f"{str(ex)}"}


##############################
try:
  import production
except:
  run(host="127.0.0.1", port=3333, debug=True, reloader=True)


