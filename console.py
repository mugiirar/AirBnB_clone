#!/usr/bin/python3
"""
a command line interpreter
"""
import models
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    custom command line interpreter
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """
        exit the program
        """
        return True

    def emptyline(self):
        """
        no excecution
        """
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_create(self, arg):
        """
        creating a new instance of BaseModel
        """
        if (len(arg) == 0):
            print ("** class name missing **")

        elif (arg != "BaseModel"):
            print ("** class doesn't exist **")

        else:
            try:
                n_inst = BaseModel()
                n_inst.save()
                print(n_inst.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
        string representation of an instance based on the class
        """
        args = line.split()
        if (len(line) == 0):
            print("** class name missing **")

        elif (args[0] != "BaseModel"):
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        else:
            class_name = args[0]
            instance_id = args[1]
            instance_key = "{}.{}".format(class_name, instance_id)
            all_objs = models.storage.all()

            if instance_key in all_objs:
                print(all_objs[instance_key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        delete an instance based on class name
        """
        args = line.split()
        if (len(args) == 0):
            print("** class name missing **")

        elif args[0] != "BaseModel":
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        else:
            n_inst = args[0] + '.' + args[1]
            all_inst = models.storage.all()
            if n_inst in all_inst:
                del models.storage.all()[n_inst]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
        str_all = []

        if len(arg) == 0:
            for inst in models.storage.all().values():
                str_all.append(str(new_instance))

        else:
            args = arg.split()
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
                return False
            else:
                for key, value in models.storage.all().items():
                    if value.__class__.__name__ == args[0]:
                        str_all.append(str(value))

        print(str_all)

    def do_update(self, arg):
        """Updates an instance based on the class name"
        """

        args = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")

        else:
            n_inst = args[0]+'.'+args[1]
            if n_inst in models.storage.all():
                setattr(models.storage.all()[n_inst],
                        args[2], args[3])
                models.storage.save()
            else:
                print("** no instance found **")


        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
