import bjoern
from main.wsgi import application
import os

bjoern.run(application, "0.0.0.0", int(os.getenv("PORT", 8000)), reuse_port=True)
