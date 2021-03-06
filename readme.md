***Cowrywise Application.*** 
The application contained in this repo was made to satisfy the following prompt
  
> Build a simple API that will return a key-value pair of randomly
> generated UUID. Key will be a timestamp and value will UUID. While the
> server is running, whenever the API is called, it should return all
> the previous UUIDs ever generated by the API alongside a new UUID.
>
The application is built using Django and the Django rest framework. It utilizes a basic authentication strategy to secure the endpoint. It is powered by the sqlite database.
The endpoints for viewing and creating the key value pair are outlined below.

GET | http://127.0.0.1:8000/keys/
SAMPLE CURL

    curl --location --request GET 'http://127.0.0.1:8000/keys/' \
    
    --header 'Accept: application/json; indent=4' \
    
    --header 'Authorization: Basic dWdvOnBhc3N3b3Jk'

Retrieves all keys and the corresponding values from the database. The results are sorted in descending order on the key column
**Sample Output**

    [
    	{
    		"2022-01-19 20:43:50.924033": "89fe186f-2086-47e2-abe5-860c389bf46a"
    	},
    	{
	    	"2022-01-19 20:43:47.872208": "29582fb8-3cf5-4e95-a687-983955571412"
    	},
    	{
	    	"2022-01-19 20:43:35.507993": "30bf361f-2334-4202-a2ac-4f6f2fbd38bb"
    	},
    	{
	    	"2022-01-19 20:43:19.272323": "952484a2-08d8-40a8-8159-297708ed7869"
    	}
    ]
POST | http://127.0.0.1:8000/keys/
sample curl 

    curl --location --request POST 'http://127.0.0.1:8000/keys/' \
    
    --header 'Accept: application/json; indent=4' \
    
    --header 'Authorization: Basic dWdvOnBhc3N3b3Jk'

When called this endpoint uses the current time to create a new key value pair and commits the result to the database

    {
	    "2022-01-19 21:58:18.003336":  "8c47f9c2-6ee4-47bc-af10-dbe2fc4052a1"    
    }
**Instructions to run**

1 install pipenv on you system using the command pip install --user pipenv

2) clone this repo

3) cd to the repo directory

4) run "pipenv install" to install the needed project files

5) run pipenv shell to enter your environment

6) python manage.py migrate to run migrations

7) python manage.py createsuperuser to create a user for authentication requirement

8) visit any of the end points above

YOU MAY USE THE SQLITE DB CONTAINED IN THE REPO IF YOU DONT WANT TO RUN MIGRATONS SIMPLE RENAME THE FILE TO db.sqlite3

Created By 
Nwokorobia Ugochukwu