# create user and db in psql:
    CREATE USER ignored_user WITH PASSWORD '5F4DCC3B5AA765D61D8327DEB882CF99' CREATEDB;

    CREATE DATABASE ignored_db WITH OWNER ignored_user;


# in root directory, run this in terminal:
    pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt


# create a .env file and add this:
    FLASK_APP=app
    FLASK_ENV=development
    SECRET_KEY=77D28DC99A3474920AFDF2FAC094D298
    DATABASE_URL=postgresql://ignored_user:5F4DCC3B5AA765D61D8327DEB882CF99@localhost/ignored_db


# Get into your pipenv shell, migrate your database, seed your database, and run your flask app

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```


# cd into react-app folder and run:
    npm install
    npm start


- You should be able to see login prompt at localhost:3000 now (npm start should take you there automatically)

