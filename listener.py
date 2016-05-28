import YailListener


class Value(object):
    def __init__(self, val_type, value):
        self.type = val_type
        self.value = value


class Listener(YailListener.YailListener):     
    def __init__(self):
        super(YailListener.YailListener, self).__init__()
        self.variables = {}
        self.values_stack = []

    def exitDeclare(self, ctx):
        var_type = ctx.TYPE().getText()
        var_name = ctx.ID().getText()

        if var_name in self.variables:
            raise Exception('Variable %s already declared' % var_name)
        else:
            self.variables[var_name] = self.values_stack.pop()

    def exitAssign(self, ctx):
        var_name = ctx.ID().getText()

        if var_name not in self.variables:
            raise Exception('Variable %s not declared' % var_name)
        else:
            var_type = self.variables[var_name].type
            var_value = self.variables[var_name].value
            value_from_stack = self.values_stack.pop()
            if var_type != value_from_stack.type:
                raise Exception('''Variable %s is type of %s
                                   but given values is type of %s
                                '''% (var_name, var_type, value_from_stack.type))
            else:
                self.variables[var_name].value = value_from_stack.value

    def exitInt(self, ctx):
        val_type = 'int'
        value = ctx.INT().getText()
        self.values_stack.append(Value(val_type, value))

    def exitDouble(self, ctx):
        val_type = 'double'
        value = ctx.DOUBLE().getText()
        self.values_stack.append(Value(val_type, value))

    def exitId(self, ctx):
        var_name = ctx.ID().getText()
        
        if var_name not in self.variables:
            raise Exception('Variable %s not declared' % var_name)
        else:
            self.values_stack.append(self.variables[var_name])

    def exitWrite(self, ctx):
        var_name = ctx.ID().getText()
        if var_name in self.variables:
            print(self.variables[var_name].value)
        else:
            raise Exception('Variable %s not declared' % var_name)

    def exitRead(self, ctx):
        var_name = ctx.ID().getText()
        if var_name in self.variables:
            x = input()
            self.variables[var_name].value = x
        else:
            raise Exception('Variable %s not declared' % var_name)
