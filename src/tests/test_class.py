import unittest
import sys

sys.path.append('src/actions')


from master_to_host_commands import Command
import descriptors


class TestCommand(unittest.TestCase):
    def test_create_command(self):
        xx = Command(name='name', body='print', target='google', if_root=True)
        print(xx)
        yy = 'adad'
        print(yy)
        self.assertEqual(xx, yy)
        print("!!!!!!!!")


unittest.main()