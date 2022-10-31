import bjoern
from main.wsgi import application


bjoern.run(application, "0.0.0.0", 8000, reuse_port=True)
