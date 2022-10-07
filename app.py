from bottle import default_app, error, redirect,request, response, run, get, static_file, view
import x

##############################
@get("/static/<file_name>")
def _(file_name):
  return static_file(file_name, root="./static")

##############################
@get("/")
@view("view_index.html")
def _(): 
  is_spa = True if request.headers.get('SPA') else False
  return dict(title="Home", is_spa=is_spa, home_link_active='class="active"')


##############################
@get("/items")
@view("view_items")
def _():
  items = [{"id":1, "name":"A", "price":10},{"id":2, "name":"B", "price":20}]
  is_spa = True if request.headers.get('SPA') else False
  return dict(title="Items", is_spa=is_spa, items_link_active='class="active"', items=items)  

##############################
@get("/item/<item_id>")
@view("view_item")
def _(item_id):
  item = {"id":item_id, "name":"A", "price":10}
  is_spa = True if request.headers.get('SPA') else False
  return dict(title=f"Item {item_id}", is_spa=is_spa, items_link_active='class="active"', item=item)  



##############################
@get("/create-item")
@view("view_create_item.html")
def _():
  print('HTTP_SPA', request.headers.get('SPA'))
  is_spa = True if request.headers.get('SPA') else False
  return dict(title="Create item", is_spa=is_spa, create_item_link_active='class="active"')  


##############################
@error(404)
@view("view_404")
def _(error):
  is_spa = True if request.headers.get('SPA') else False
  response.status= 200
  return dict(title="Ups", is_spa=is_spa)  


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


