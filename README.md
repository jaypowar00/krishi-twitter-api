# krishi-twitter-api
This repository is for showcasing Krishi Network's Internship task  
[![wakatime](https://wakatime.com/badge/user/7293504b-e51f-41db-ba94-4c0911fe9e63/project/e7633a46-d9cb-4051-b8d3-2462b6b55bf3.svg)](https://wakatime.com/badge/user/7293504b-e51f-41db-ba94-4c0911fe9e63/project/e7633a46-d9cb-4051-b8d3-2462b6b55bf3)

___

## This flask app makes use of following ENV Variables:
- `DATABASE_URI` : for SQLAlchemy database connection also will be used for models to create/define tables
- `K_HOST` : for psycopg2 to connect to our database and execute manual queries in controller.py
- `K_DATABASE` : for psycopg2 to connect to our database and execute manual queries in controller.py
- `K_USER` : for psycopg2 to connect to our database and execute manual queries in controller.py
- `K_PORT` : for psycopg2 to connect to our database and execute manual queries in controller.py
- `K_PASSWORD` : for psycopg2 to connect to our database and execute manual queries in controller.py
- `WEATHER_API_KEY` : API KEY generated from your [openweathermap's](https://openweathermap.org/current) free account
___
## Routes provided by this API:
1. `/posts/`:
    - This route takes either query params or json data with `GET` request
    - for query parameters following fields are needed:
        1. `x`: value of latitude attribute of location
        2. `y`: value of longitude attribute of location
        3. `page`: defines which page to retrive. Each page contains 10 tweets
    - for json body data following fields are required:
        1. `location`: defines the location, it has 2 sub keys `x` & `y` for lat & long values respectively.
        2. `page`: for defining page number to retrive data from.
    - #### demo json data for this request:
      ```
      {
          "location": {
              "x": "16.70086500122643",
              "y": "74.216502097104"
          },
          "page": 1
      }
      ```

2. `/posts/create/`:
    - This route creates new tweets for given location with provided message.
    - This route requires `POST` request.
    - for json body data following attributes are required:
        1. `message`: defines what message should be given in the new tweet
        2. `location`: defines the location of the user who tweeted the tweet. It has 2 sub keys as `x` & `y` for lat & long resp.
    - #### demo json data for this request:
      ```
      {
          "message": "waiting at shivaji bridge for my friends to arrive",
          "location": {
              "x": "16.70702834506061",
              "y": "74.21791251709445"
          }
      }
      ```

3. `/weather/`:
    - This route returns current weather information using [openweathermap's free weather API](https://openweathermap.org/current).
    - This route takes either query params or json data with `GET` request
    - for query parameters following fields are needed:
        1. `x`: value of latitude attribute of location
        2. `y`: value of longitude attribute of location
    - for json body data following attributes are required:
        2. `location`: defines the location of the user who wants to get weather infomation. It has 2 sub keys as `x` & `y` for lat & long resp.
    - #### demo json data for this request:
      ```
      {
          "location": {
              "x": "16.70702834506061",
              "y": "74.21791251709445"
          }
      }
      ```
___

#### Extras:
- Checkout [openweathermap](https://openweathermap.org/current) for their free Weather API
- Check out PostgreSQL [POINT data type](https://www.postgresql.org/docs/current/datatype-geometric.html#idm46428712347808)
- Check out [PostGIS](https://postgis.net/) extension which enables use of sptial objects (in simle words: for enabling point data types)
- Checkout [SQLAlchemy](https://www.tutorialspoint.com/sqlalchemy/index.htm) & [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- Checkout [Blueprints in Flask](https://hackersandslackers.com/flask-blueprints/)
- Checkout [MVC in Flask](https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/)
___
