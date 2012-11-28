from django.utils import unittest
import json
import sys

import mock

from .formatters import JSONFormatter


class JSONFormatterTests(unittest.TestCase):
    def test_out_is_valid_json(self):
        """JSONFormatter should output valid JSON."""
        formatter = JSONFormatter()
        output = formatter.format(self.FakeLogRecord())

        self.assertIsInstance(json.loads(output), dict)

    def test_basic_usage(self):
        """
        JSONFormatter should be able to handle a simple LogRecord and return JSON for it.
        """
        expected_output = {
            'extra': {'ip': '127.0.0.1', 'foo': 'asfd'},
            'process': {'process': 7821, 'processName': 'MainProcess', 'threadName': 'MainThread', 'thread': 140735211397504},
            'file': {'funcName': 'main', 'pathname': 'test.py', 'lineno': 116, 'module': 'test', 'filename': 'test.py'},
            'time': {'relativeCreated': 8.126974105834961, 'asctime': '2012-11-20T23:30:59.111096Z', 'created': 1353454259.111096},
            'logger': {'levelno': 10, 'name': 'main', 'levelname': 'DEBUG'},
            'message': {'msg': 'in main function %s', 'message': "in main function ['foo']", 'args': ['foo']}
        }

        formatter = JSONFormatter()
        output_json = formatter.format(self.FakeLogRecord())
        output = json.loads(output_json)

        self.assertEqual(output, expected_output)

    def test_custom_layout(self):
        """
        JSONFormatter should use a custom dictionary format if specified.
        """
        expected_output = {
            'file': {'funcName': 'main', 'lineno': 116, 'module': 'test'},
            'time': {'asctime': '2012-11-20T23:30:59.111096Z'},
            'logger': {'name': 'main', 'levelname': 'DEBUG'},
            'message': {'message': "in main function ['foo']"}
        }
        custom_layout = {
            'file': ['module', 'funcName', 'lineno'],
            'time': ['asctime'],
            'logger': ['name', 'levelname'],
            'message': ['message']
        }

        formatter = JSONFormatter(layout=custom_layout)
        output_json = formatter.format(self.FakeLogRecord())
        output = json.loads(output_json)

        self.assertEqual(output, expected_output)

    def test_proccess_extra(self):
        """
        JSONFormatter.process_extra should find all the `extra` parameters on a LogRecord and return them as a dictionary.
        """
        expected_output = {'ip': '127.0.0.1', 'foo': 'asfd'}

        formatter = JSONFormatter()
        output = formatter.process_extra(self.FakeLogRecord())

        self.assertEqual(output, expected_output)

    def test_custom_json_encoder(self):
        """
        JSONFormatter should use a custom JSON encoder if it is specified.
        """
        custom_layout = {'extra': ''}
        mocked_json_encoder = mock.MagicMock()
        formatter = JSONFormatter(
            layout=custom_layout,
            json_encoder=mocked_json_encoder
        )

        record = self.FakeLogRecord()

        formatter.format(record)
        self.assertTrue(mocked_json_encoder.called)

    def test_formatDate(self):
        """
        JSONFormatter.formatDate should return a ISO formatted UTC date string.
        """
        expected_output = '2012-11-20T23:30:59.111096Z'
        timestamp = 1353454259.111096

        formatter = JSONFormatter()
        output = formatter.formatDate(timestamp)

        self.assertEqual(output, expected_output)

    def test_proccess_exception(self):
        """
        JSONFormatter.process_exception should return a dictionary with exception info.
        """
        formatter = JSONFormatter()

        try:
            5 + 'boom!'
        except TypeError:
            exc_info = sys.exc_info()

        output = formatter.process_exception(exc_info)
        self.assertEqual(output['type'], "<type 'exceptions.TypeError'>")
        self.assertEqual(output['value'], "unsupported operand type(s) for +: 'int' and 'str'")
        self.assertEqual(output['traceback'][0]['function_name'], 'test_proccess_exception')

    class FakeLogRecord(object):
        """A fake log record for testing."""
        def __init__(self):
            self.args = ['foo']
            self.levelname = 'DEBUG'
            self.levelno = 10
            self.pathname = 'test.py'
            self.filename = 'test.py'
            self.process = 7821
            self.processName = 'MainProcess'
            self.threadName = 'MainThread'
            self.thread = 140735211397504
            self.funcName = 'main'
            self.lineno = 116
            self.module = 'test'
            self.relativeCreated = 8.126974105834961
            self.created = 1353454259.111096
            self.name = 'main'
            self.exc_info = None
            self.msg = 'in main function %s'
            self.ip = '127.0.0.1'
            self.foo = 'asfd'

        def getMessage(self):
            return self.msg % self.args
