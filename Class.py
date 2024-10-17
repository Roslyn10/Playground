#!/usr/bin/python3

class Cmd:
    def __init__(self):
        self.prompt = '> '

    def cmdloop(self):
        """Repeatedly issue a prompt, accept input, parse an initial prefix off
        the received input, and dispatch to action methods, passing them the
        remainder of the line as argument."""
        self.preloop()
        while True:
            try:
                line = input(self.prompt)
            except EOFError:
                line = 'EOF'
            if not line:
                line = 'empty line'
            if line == 'EOF':
                break
            self.onecmd(line)
        self.postloop()

    def preloop(self):
        """Hook method executed once when the cmdloop() method is called."""
        pass

    def postloop(self):
        """Hook method executed once when the cmdloop() method is about to return."""
        pass

    def onecmd(self, line):
        """Interpret the command."""
        cmd, arg, line = self.parseline(line)
        if not cmd:
            return self.default(line)
        method = 'do_' + cmd
        if hasattr(self, method):
            return getattr(self, method)(arg)
        return self.default(line)

    def parseline(self, line):
        """Parse the command line into a command and arguments."""
        line = line.strip()
        if not line:
            return None, None, line
        parts = line.split(maxsplit=1)
        cmd = parts[0]
        arg = parts[1] if len(parts) > 1 else ''
        return cmd, arg, line

    def default(self, line):
        """Called on an input line when the command prefix is not recognized."""
        print('*** Unknown command: %s' % line)

    def emptyline(self):
        """Called when an empty line is entered."""
        pass
