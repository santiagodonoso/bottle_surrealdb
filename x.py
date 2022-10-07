from bottle import request
import requests
from requests.auth import HTTPBasicAuth
import re

##############################
SURREALDB_URL           = "http://127.0.0.1:8000/sql"
SURREALDB_NAMESPACE     = "company"
SURREALDB_DATABASE_NAME = "company"
SURREALDB_USER_NAME     = "admin"
SURREALDB_USER_PASSWORD = "password"

ITEM_NAME_MIN         = 2
ITEM_NAME_MAX         = 20
ITEM_DESCRIPTION_MIN  = 10
ITEM_DESCRIPTION_MAX  = 200
ITEM_PRICE_REGEX      = "^[1-9][0-9]*,[0-9]{2}$"

##############################
def validate_item_name():
  error_message = f"'item_name' min {ITEM_NAME_MIN} max {ITEM_NAME_MAX} characters"
  request.form.item_name = request.form.item_name.strip()
  request.form.item_name = re.sub(' +', ' ', request.form.item_name)
  if len(request.form.item_name) < ITEM_NAME_MIN: raise Exception(error_message)
  return request.form.item_name

##############################
def validate_item_description():
  error_message = f"'item_description' min {ITEM_DESCRIPTION_MIN} max {ITEM_DESCRIPTION_MAX} characters"
  request.form.item_description = request.form.item_description.strip()
  request.form.item_description = re.sub(' +', ' ', request.form.item_description)
  if len(request.form.item_description) < ITEM_DESCRIPTION_MIN: raise Exception(error_message)
  return request.form.item_description

##############################
def validate_item_price():
  error = f"'item_price must be a whole number or contain 2 decimals divided by a comma"
  request.form.item_price = request.form.item_price.strip()
  if("." in request.form.item_price): request.form.item_price = request.form.item_price.replace(".", ",")
  if("," not in  request.form.item_price):  request.form.item_price = f"{request.form.item_price},00"
  if(not re.match(ITEM_PRICE_REGEX, request.form.item_price)): raise Exception(error)
  return request.form.item_price

##############################
def validate_page_number():
  error = f"'page' must be a positive number"
  try:
    request.query.page = int(request.query.page)
    if request.query.page < 1: raise Exception(error)
    return request.query.page
  except:
    raise Exception(error)    


##############################
def surrealdb(query):
  headers = { 'Content-Type': 'application/json', 
              'Accept':'application/json', 
              'ns': SURREALDB_NAMESPACE, 
              'db': SURREALDB_DATABASE_NAME}
  r = requests.post(  SURREALDB_URL, 
                      data=query, 
                      headers=headers, 
                      auth = HTTPBasicAuth(SURREALDB_USER_NAME, SURREALDB_USER_PASSWORD))
  if "code" in r.json(): raise Exception(r.json())
  return r.json()