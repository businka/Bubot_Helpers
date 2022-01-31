import unittest

from Bubot.Helpers.Action import Action
from Bubot.Helpers.ExtException import ExtException
from Bubot.Helpers.Helper import Helper


class TestExtException(unittest.TestCase):
    def test_raise_from_other_ext_exception(self):
        try:
            try:
                err1 = ExtException(message='msg1', action='action1')
                raise err1
            except ExtException as err:
                err2 = ExtException(message='msg2', action='action2', parent=err)
                raise err2
        except ExtException as err:
            err3 = ExtException(action='action3', parent=err)
        self.assertEqual(2, len(err3.stack))
        self.assertEqual('msg1', err3.stack[0]['message'])
        self.assertEqual('msg2', err3.message)
        print(err3)

    def test_raise_from_with_action(self):
        res = Action('action1')
        res2 = Action('action2')
        res2.add_stat(Action('action3').set_end())

        try:
            try:
                err1 = ExtException(message='msg1', action=res2)
                raise err1
            except ExtException as err:
                err2 = ExtException(message='msg2', action=res, parent=err)
                raise err2
        except ExtException as err:
            err3 = ExtException(action='action3', parent=err)
        self.assertEqual(2, len(err3.stack))
        self.assertEqual('msg1', err3.stack[0]['message'])
        self.assertEqual('msg2', err3.message)
        print(err3)

    def test_loads_exception(self):
        res = Helper.loads_exception(
            '{"__module__": "Bubot.Helpers.ExtException", "__name__":"ExtTimeoutError", "message":"test"}')
        self.assertIsInstance(res, ExtException)
        pass
