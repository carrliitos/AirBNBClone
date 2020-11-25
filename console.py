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

nameOfClass = {
	"BaseModel": BaseModel,
	"User": User,
	"State": State,
	"City": City,
	"Amenity": Amenity,
	"Place": Place,
	"Review": Review,
}

class ABNBCommand(cmd.Cmd):
	'''Create an interpreter command in Python'''
	prompt = "(ConsoleBNB) "

	def do_EOF(self, line):
		'''Exit the program'''
		return True

	def do_quit(self, line):
		'''Quit command exit the program'''
		return True

	def emptyLine(self, args):
		'''Nothing is executed'''
		pass

	def do_create(self, args):
		'''Create a new instance of the class BaseModel'''
		args = shlex.split(args)
		if not args:
			print("**Class name missing**")
		elif not args[0] in nameOfClass:
			print("** Class doesn't exist **")
		else:
			newObj = eval(args[0])()
			newObj.save()
			print(newObj.id)

	def do_show(self, args):
		'''Prints the string representation of the instance'''
		args = shlex.split(args)
		dicti = storage.all()
		if not args:
			print("** class name missing **")
		elif not args[0] in nameOfClass:
			print("** class doesn't exist **")
		elif len(args) == 1:
			print("** instance id missing **")
		elif "{}.{}".format(args[0], args[1]) in dicti:
			print(dicti["{}.{}".format(args[0], args[1])])
		else:
			print("** no instance found **")

	def do_destroy(self, args):
		'''Deletes an instance base on the class name and id'''
		args = shlex.split(args)
		dicti = storage.all()
		if not args:
			print("** class name missing **")
		elif not args[0] in nameOfClass:
			print("** class doesn't exist **")
		elif len(args) == 1:
			print("** instance id missing **")
		elif "{}.{}".format(args[0], args[1]) in dicti:
			dicti.pop("{}.{}".format(args[0], args[1]))
			storage.save()
		else:
			print("** no instance found **")

	def do_all(self, args):
		'''Prints all strings representation of all instances'''
		args = shlex.split(args)
		dicti = storage.all()
		printall = []
		if not args:
			for i in dicti.values():
				printall.append(str(i))
			print(printall)
		elif args[0] in nameOfClass:
			for key, val in dicti.items():
				if val.__class__.__name__ == args[0]:
					printall.append(val.__str__())
			print(printall)
		else:
			print("** class doesn't exist **")

	def do_update(self, args):
		'''Updates an instance base on the class name and id'''
		args = shlex.split(args)
		dicti = storage.all()
		if not args:
			print("** class name missing **")
		elif not args[0] in nameOfClass:
			print("** class doesn't exist **")
		elif len(args) == 1:
			print("** instance id missing **")
		elif not "{}.{}".format(args[0], args[1]) in dicti:
			print("** no instance found **")
		elif len(args) == 2:
			print("** attribute name missing **")
		elif len(args) == 3:
			print("** value missing **")
		else:
			key = dicti["{}.{}".format(args[0], args[1])]
			setattr(key, args[2], args[3])
			key.save()

if __name__ == '__main__':
	ABNBCommand().cmdloop()