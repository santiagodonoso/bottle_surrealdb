from bottle import request, response, post
import x

##############################
@post("/api-create-item")
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



