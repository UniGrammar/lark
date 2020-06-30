from __future__ import absolute_import, print_function

import unittest
import logging
from lark import LOGGER

from .test_trees import TestTrees
from .test_tools import TestStandalone
from .test_cache import TestCache
from .test_reconstructor import TestReconstructor

try:
    from .test_nearley.test_nearley import TestNearley
except ImportError:
    LOGGER.warning("Warning: Skipping tests for Nearley grammar imports (js2py required)")

# from .test_selectors import TestSelectors
# from .test_grammars import TestPythonG, TestConfigG

from .test_logger import TestLogger

from .test_parser import (
        TestLalrStandard,
        TestEarleyStandard,
        TestCykStandard,
        TestLalrContextual,
        TestEarleyDynamic,
        TestLalrCustom,

        # TestFullEarleyStandard,
        TestFullEarleyDynamic,
        TestFullEarleyDynamic_complete,

        TestParsers,
        )

LOGGER.setLevel(logging.INFO)

if __name__ == '__main__':
    unittest.main()
