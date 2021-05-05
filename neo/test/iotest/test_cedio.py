import unittest

from neo.io import CedIO
from neo.test.iotest.common_io_test import BaseTestIO


class TestCedIO(BaseTestIO, unittest.TestCase, ):
    ioclass = CedIO
    entities_to_test = [
        'spike2/m365_1sec.smrx'
    ]
    entities_to_download = [
        'spike2/m365_1sec.smrx'
    ]


if __name__ == "__main__":
    unittest.main()
