from descriptors import Name, Body, Target, If_root


class Command:
    """Команды с хоста админа.
    Все аргументы - str!!!
    name - название действия,
    action - сам код действия,
    target - цель применения"""
    name = Name()
    body = Body()
    target = Target()
    if_root = If_root()

    def __init__(self, name: str, body: str, target: str, if_root: bool = False):
        self.name = name
        self.body = body
        self.target = target
        self.if_root = if_root

    def __str__(self):
        """При вызове для чтения"""
        return (f"Класс {Command} "
                f"Имя действия {self.name} "
                f"Тело действия {self.body} "
                f"Цель {self.target} "
                f"Права {self.if_root}")
