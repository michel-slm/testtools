# Copyright (c) 2008 Jonathan M. Lange. See LICENSE for details.

"""Extensions to the standard Python unittest library."""

__all__ = [
    'clone_test_with_new_id',
    'iterate_tests',
    'MultiTestResult',
    'TestCase',
    'TestResult',
    'ThreadsafeForwardingResult',
    ]

from testtools.testcase import TestCase, clone_test_with_new_id
from testtools.testresult import (
    MultiTestResult,
    TestResult,
    ThreadsafeForwardingResult,
    )
from testtools.utils import iterate_tests
