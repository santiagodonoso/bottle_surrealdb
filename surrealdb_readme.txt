SURREALDB

// Download the single executable file

iwr https://windows.surrealdb.com -useb | iex

// This will download a file called surreal.exe

Start the server in memory
surreal start --log trace --user admin --pass password

Start the server and store data in a file
surreal start --log trace --user admin --pass password file:data.db

Start the client
surreal sql --conn http://localhost:8000 --user admin --pass password --ns company --db company --pretty

SQL
NoSQL
Kay Values
GRAPH

Create an user
CREATE user:1 SET name='A', email='@a', age=1
CREATE user:2 SET name='Ub', email='@b', age=2

Show users
SELECT * FROM user

Show user with id 1
SELECT * FROM user:1

Create items
CREATE item:1 SET name='Item One', price=10
CREATE item:2 SET name='Item Two', price=20

Show items
SELECT * FROM item

Show item with id 1
SELECT * FROM item:1

Set user 1 to buy item 1 for a price of 8
RELATE user:1->bought->item:1 SET price=8, created_at = time::now()

RELATE user:2->bought->item:1 CONTENT {
	source: 'Store',
	tags: ['notes', 'markdown'],
	time: {
		written: time::now(),
	},
} RETURN AFTER;


Show items bought by user:1
SELECT id, ->bought->item AS bought FROM user:1
SELECT *, ->bought->item.* AS bought FROM user:1 

SELECT *, ->(bought AS bought)->item.* AS items FROM user:1 FETCH bought;

 SELECT ->(bought AS bought_items)->item AS items FROM user:1 FETCH bought_items, items

LET 


bought
[
  {
    "result": [
      {
        "id": "bought:znuuzakar0y48u7wbhdn",
        "in": "user:1",
        "out": "item:1",
        "price": 8
      }
    ],
    "status": "OK",
    "time": "3.1309ms"
  }
]



 SELECT *, ->bought AS bought FROM user:1 FETCH bought, bought.out.item
 [
  {
    "result": [
      {
        "bought": [
          {
            "id": "bought:3xoc93b95e8c2otxnxnx",
            "in": "user:1",
            "out": "item:2",
            "price": 9
          },
          {
            "id": "bought:znuuzakar0y48u7wbhdn",
            "in": "user:1",
            "out": "item:1",
            "price": 8
          }
        ],
        "id": "user:1",
        "name": "A"
      }
    ],
    "status": "OK",
    "time": "17.1366ms"
  }
]



> SELECT *, ->bought AS bought, math::sum(->bought.*.price) AS total FROM user:1 FETCH bought, bought.out.item
[
  {
    "result": [
      {
        "bought": [
          {
            "id": "bought:3xoc93b95e8c2otxnxnx",
            "in": "user:1",
            "out": "item:2",
            "price": 9
          },
          {
            "id": "bought:znuuzakar0y48u7wbhdn",
            "in": "user:1",
            "out": "item:1",
            "price": 8
          }
        ],
        "id": "user:1",
        "name": "A",
        "total": 17
      }
    ],
    "status": "OK",
    "time": "20.9706ms"
  }
]


SELECT * FROM person WHERE name CONTAINS "something"; -- contains
SELECT * FROM person WHERE name = /something/; -- matches regex
SELECT * FROM person WHERE email = /gmail.com$/; -- ends with gmail.com
SELECT * FROM person WHERE email ~ "GMail"; -- fuzzy matches
SELECT * FROM person WHERE emails.*.value ?= /gmail.com$/; -- any email value ends with gmail.com
SELECT * FROM person WHERE emails.*.value ?~ "GMail"; -- any email value fuzzy matches
SELECT * FROM person WHERE emails.*.value *= /gmail.com$/; -- all email values end with gmail.com
SELECT * FROM person WHERE emails.*.value *~ "GMail"; -- all email values fuzzy match




##############################
##############################
##############################

surreal sql --conn http://localhost:8000 --user admin --pass password --ns company --db company --pretty

CREATE user:1 SET name='A', email='@a', age=1
CREATE item:1 SET name='Item One', price=10
CREATE item:2 SET name='Item Two', price=20

RELATE user:1->bought->item:1 SET price=5, created_at = time::now()
RELATE user:1->bought->item:2 SET price=10, created_at = time::now()

SELECT *, ->bought AS bought, math::sum(->bought.*.price) AS total FROM user:1 FETCH bought, bought.out.item
SELECT *, ->bought AS bought, math::sum(->bought.*.price) AS total, ->bought.*.out.* AS items FROM user:1 FETCH bought
