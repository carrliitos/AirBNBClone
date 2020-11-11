#!/usr/bin/python3

'''Console module'''

import cmd
import shlex
from models import storage
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.baseModel import BaseModel
from models.engine.fileStorage import FileStorage