import unittest
from LCA import LCA

class TestLCA(unittest.TestCase):

	# Testing constructor with file as input
	# also tests the building of the tree
    def test_contstructor1(self):
        lca = LCA("inputs.txt")
        self.assertEqual(lca.bst.printTreeOneLine(
        ), "((((()1())3(()4()))5((()6())7(()8())))10((()15(()17()))20((()22())25(()27())))")

	# Testing contructor with array as input	
	# also tests the building of the tree	
    def test_constructor2(self):
        lca = LCA([10,5,20,3,7,15,25,1,4,6,8,12,17,22,27])
        self.assertEqual(lca.bst.printTreeOneLine(
        ), "((((()1())3(()4()))5((()6())7(()8())))10((()15(()17()))20((()22())25(()27())))")

	# Tests the LCA algorithm itself, which calls the other functions being used
    def test_LCA(self):
        lca = LCA("inputs.txt")
        self.assertEqual(lca.findLCA(6, 8), 7,"Find LCA of 6 and 8 (expect 7)")
        self.assertEqual(lca.findLCA(27, 1), 10,"Find LCA of 27 and 1 (expect 10)")
        self.assertEqual(lca.findLCA(1, 8), 5,"Find LCA of 1 and 8 (expect 5)")
        self.assertEqual(lca.findLCA(2121, 8), None,"Find LCA of 2121 and 8 (expect None)")
        self.assertEqual(lca.findLCA(None, None), None,"Find LCA of None and None (expect None)")


if __name__ == '__main__':
    unittest.main()
