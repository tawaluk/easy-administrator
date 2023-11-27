import unittest


from src.actions.master_to_host_commands import Command
from src.actions import descriptors


class TestCommand(unittest.TestCase):
    def test_create_command(self):
        xx = Command(name='name', body='print', target='google', if_root=True)
        print(xx)
        yy = 'adad'
        print(yy)
        self.assertEquals(xx, yy)


unittest.main()