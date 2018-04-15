import unittest
import html_render as hr


class HTMLRenderTest(unittest.TestCase):
    """tests html_render output"""

    def test_element(self):
        test = hr.Element(content=None)
        self.assertEqual(test.tag, '')
        self.assertEqual(test.indent, 0)