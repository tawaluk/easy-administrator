class Name:
    def __get__(self, obj, objtype=None):
        return self.name

    def __set__(self, obj, name):
        if str == type(name):
            self.name = name
        else:
            raise ValueError(f"name ожидает str, а получен {type(name)}")


class Body:
    def __get__(self, obj, objtype=None):
        return self.body

    def __set__(self, obj, body):
        if str == type(body):
            self.body = body
        else:
            raise ValueError(f"body ожидает str, а получен {type(body)}")


class Target:
    def __get__(self, obj, objtype=None):
        return self.target

    def __set__(self, obj, target):
        if str == type(target):
            self.target = target
        else:
            raise ValueError(f"target ожидает str, а получен {type(target)}")


class If_root:
    def __get__(self, obj, objtype=None):
        return self.if_root

    def __set__(self, obj, if_root):
        if bool == type(if_root):
            self.if_root = if_root
        else:
            raise ValueError(f"if_root ожидает bool, а получен {type(if_root)}")