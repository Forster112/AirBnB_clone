"""class HBNBCommand"""
import cmd


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """exit the program"""
        return True

    def do_Eof(self, arg):
        """exit the program"""
        return True

    def emptyline(self):
        """does nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
