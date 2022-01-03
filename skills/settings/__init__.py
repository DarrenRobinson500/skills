from .common import *
from .production import *

try:
	from ._local import *
except:
    pass

# from ._local import *git add .
# git add .
# git commit -m “Heroku Push”
# git push
# git push heroku main

# heroku run python manage.py createsuperuser