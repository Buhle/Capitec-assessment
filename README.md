# Capitec-assessment

## For local setup

Install pip3
Run `pip3 install requirement.py`

## Run test

`python manage.py test`

## To run a project 

`python manage.py runserver`


## APIs

### Submit a transaction
**url:** `/transaction`

**Method:** POST

**Body Payload:**

`{
    "amount": 20000,
    "user_id": "2",
    "reference": "gambling"
}`

**Response payload:**

`{
    "id": 6,
    "user_id": 20,
    "amount": "20000.00",
    "created_at": "2025-11-24T18:04:23.164569Z",
    "reference": "test"
}`

### List all fraud alerts
**url:** `/fraud/alerts`

**Method:** GET

**Response payload:** 

    [
        {
        "id": 1,
        "transaction_id": "4",
        "is_fraudulent": true,
        "alert_message": "Transaction exceeds maximum allowed amount.",
        "created_at": "2025-11-19T22:10:44.891552Z",
        "transaction": 4
    },
    {
        "id": 2,
        "transaction_id": "5",
        "is_fraudulent": true,
        "alert_message": "Transaction exceeds maximum allowed amount.",
        "created_at": "2025-11-19T22:21:03.831787Z",
        "transaction": 5
    }
]


### Retrieve 1 fraud alert
 **url:** `/fraud/2`

 **Method:** GET

 **Response payload:** 

    `{
        "id": 2,
        "transaction_id": "5",
        "is_fraudulent": true,
        "alert_message": "Transaction exceeds maximum allowed amount.",
        "created_at": "2025-11-19T22:21:03.831787Z",
        "transaction": 5
    }`
    
## To access admin

**Create super user**

`python manage.py createsuperuser`

**url** `admin`

**To build docker**

`docker build -t fraud .`
