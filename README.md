# Example Database app
This is an example database app using PostgreSQL, Flask-SQLAlchemy and Flask-Migrate

To begin using this app you can do the following:

1. Clone the repository to your local machine or Cloud9.
2. Create a Python virtual environment e.g. `python -m venv venv` (You may need to use `python3` instead or `python3.5` on Cloud9)
3. Enter the virtual environment using `source venv/bin/activate` (or `.\venv\Scripts\activate` on Windows)
4. Install the dependencies using Pip. e.g. `pip install -r requirements.txt`. Note: Ensure you have PostgreSQL already installed and a database created.
5. Edit the `app/__init__.py` file and enter your database credentials and database name.
6. Run the migrations by typing `python flask-migrate.py db upgrade`
7. Start the development server using `python run.py`.