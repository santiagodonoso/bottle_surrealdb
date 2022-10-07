from bottle import default_app, request, response, run, get, post
import requests
from requests.auth import HTTPBasicAuth
import json
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
@post("/items")
def _():
  try:
    x.validate_item_name()
    x.validate_item_description()
    x.validate_item_price()
  except Exception as ex:
    response.status = 400
    return {"info":str(ex)}
    
  try:
    db_response = x.surrealdb(f"""
      LET $name='{request.form.item_name}';
      LET $price='{request.form.item_price}';
      CREATE item SET name=$name, price=$price;
    """)
    return db_response[-1]['result'][0]
  except Exception as ex:
    response.status = 400
    return {"info":f"{str(ex)}"}


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


