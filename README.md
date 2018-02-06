# Example Database app
This is an example database app using PostgreSQL, Flask-SQLAlchemy and Flask-Migrate

To begin using this app you can do the following:

1. Clone the repository to your local machine or Cloud9.
2. Create a Python virtual environment e.g. `virtualenv venv`
3. Install the dependencies using Pip. e.g. `pip install -r requirements.txt`. Note: Ensure you have PostgreSQL already installed and a database created.
4. Edit the `app/__init__.py` file and enter your database credentials and database name.
5. Run the migrations by typing `python flask-migrate.py db upgrade`
6. Start the development server using `python run.py`.