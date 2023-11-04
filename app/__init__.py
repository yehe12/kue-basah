from flask import Flask

app = Flask(__name__)

from app.config.db import *

from app.controllers import *

from app.controllers.Auth import *

from app.controllers.Boss import *

from app.controllers.Admin import *