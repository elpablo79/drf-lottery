# DRF Lottery


## Assumptions

The application uses random generation for the winnings.
The first assumption is that the requests for each day are `prize_per_day` squared. If you want to change that value simply edit the number returned from the function `n_requests_estimate` in `/api/functions.py`.


## Installation

Run the following commands:
1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python manage.py migrate`
5. `python manage.py db_seed`

The last command creates 2 contests and 2 users.
###
   - Users "user1", "user2", have the password "123456"
   - User admin has the password "admin"
###

   - C0001 is a standard contest.
   - C0002 is an expired contest.

6. `python manage.py runserver`

###

- To create a new user, you can use the Django admin interface available at http://127.0.0.1:8000/admin/ (username: admin, password: admin)

- To associate a user with a contest, you can create the association at http://127.0.0.1:8000/admin/api/usertocontest/


## Usage
To launch the contest the API call has to be done to the following endpoint:

`/play/?contest={code}`

The endpoint can be called with the GET method.

The `contest` parameter is mandatory.
