from unittest import TestCase

from itsybitsy.TH.code_folding import get_number


class TestGet_number(TestCase):
    result = get_number()
    assert result == 10

