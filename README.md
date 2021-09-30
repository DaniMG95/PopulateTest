# PopulateTest

Item level review system, in which the system architecture is built in Flask for the Backend and FrontEnd.
in Angular [repositorio](https://github.com/DaniMG95/populateFront).  
For the deployment of the application we have hosted the FrontEnd compiled from angular together with the Backend that has been generated in 
Flask to facilitate the development of the application.  

To launch the application it is necessary to have python3 installed and launch the following steps.

```
pip install -r requirements
export path="path/test.db"
export key="keyFlask"
python3 server.py
```
 - path :  is the path to test.db
 - keyFlask : is the key to Flask

The BackEnd is assembled with Flask, the Flask-restfull library and the database model is assembled with SQLAlchemy-Flask.


## Modelo de datos

We have two database tables, one is an item and the other is a review and we have a one to many relationship, which allows an item to have several reviews.
so we allow that an item can have several reviews and the insertion to the database is done through the endpoints.



## EndPoints

These are the endpoints that are available in the API 

### GET /items/
This endpoints returns the items with their respective reviews.


#### Output
```
{
    "items": [
        {
            "name": "The Minimalist Entrepreneur",
            "rating": 3.2,
            "reviews": [
                {
                    "review": "sadasddsaasddas",
                    "rating": 2,
                    "item_id": 1
                },
            ]
         }
}
```

### GET /item/[id: integer]
This endpoints returns the item that corresponds to the id with its respective reviews.

#### Output
```
{
    "name": "The Minimalist Entrepreneur",
    "rating": 3.2,
    "reviews": [
        {
            "review": "sadasddsaasddas",
            "rating": 2,
            "item_id": 1
        },
    ]
}
        
```

### PUT /item/[id: integer]
This endpoint takes all the reviews of the item id and updates its rating by the average of the ratings of all the reviews.
all the reviews

#### Output
```
{
    "name": "The Minimalist Entrepreneur",
    "rating": 3.2,
    "reviews": [
        {
            "review": "sadasddsaasddas",
            "rating": 2,
            "item_id": 1
        },
    ]
}
```


### POST /item
This endpoint is in charge of creating the item with the description passed in the input.

#### Input
```
{
    "name": "The Minimalist Entrepreneur"
}
```

#### Output
```
{
    "msg": "item created"
}
```


### POST /review/[id: integer]
This endpoint is responsible for inserting a review to the item id with the respective entry.

#### Input
```
{
    "review":"sadasddsaasddas",
    "rating": 2
}
```

#### Output
```
{
    "review": "sadasddsaasddas",
    "rating": 2,
    "item_id": 1
}
```