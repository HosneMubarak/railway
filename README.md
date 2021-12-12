## Railway ticket booking

## Coding problem solution in rood directory problem.py

In the project directory, you can run:

### `pip install -r requirements.txt`
### `python manage.py makemigration`
### `python manage.py migrate`
### `python manage.py runserver 8000`

##End point:

##getting all train schedule
### `http://127.0.0.1:8000/all_train_scedule/`

## Booking ticket by user using POST method and it will decrese seat count and if seat count == 0 user can't make booking 
### `http://127.0.0.1:8000/user_ticket/`
`body={
{
    "user":1,
    "ticket":1
}
}`

### GET geting specific user booking ticket data

`http://127.0.0.1:8000/user_ticket/`

