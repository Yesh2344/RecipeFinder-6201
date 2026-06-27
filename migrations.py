from flask import Flask
from database import init_db, create_tables

# rewrote this part
app = Flask(__name__)
init_db(app)
create_tables(app)