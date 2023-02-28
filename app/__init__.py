from flask import Flask

app = Flask(__name__)


# import routes always at bottom of page
from app import routes
