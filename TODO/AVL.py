class Tree:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

  def print_node(self):
    string = ''
    string += str(self.left) if self.left else ' '
    string += "->"
    string += str(self.data) 
    string += "->"
    string += str(self.right) if self.right else ' '
    print string
    # print self.left if self.left else None
    # print self.right if self.right else None

  def __str__(self):
    return str(self.data)

def left_rotate(node):
  """
  10
    11
      12
  """
  top_ele = node
  right_ele = node.right
  bottom_ele = node.right.right

  right_ele.right = bottom_ele
  right_ele.left = top_ele
  return right_ele

def right_rotate(node):
  """
      10
    11
  12
  """
  top_ele = node
  left_ele = node.left
  bottom_ele = node.left.left

  left_ele.left = top_ele
  left_ele.right = bottom_ele
  return left_ele

def left_right_rotate(node):
  """
    12
  10
    11
  """
  top_ele = node
  left_ele = node.left
  bottom_ele = node.left.right

  left_ele.left = bottom_ele
  left_ele.right = top_ele
  return left_ele

def right_left_rotate(node):
  """
  10
    12
  11
  """
  top_ele = node
  right_ele = node.right
  bottom_ele = right_ele.left

  bottom_ele.left = top_ele
  bottom_ele.right = right_ele
  return bottom_ele

def test_left_rotate():
  # Test left_rotate
  test2 = Tree(11,left=None, right=12)
  test1 = Tree(10, left=None, right=test2)
  test1.print_node()
  test2.print_node()
  test = left_rotate(test1)
  test.print_node()


def test_right_rotate():
  # Test right_rotate
  test2 = Tree(11,left=12, right=None)
  test1 = Tree(10, left=test2, right=None)
  test1.print_node()
  test2.print_node()
  test = right_rotate(test1)
  test.print_node()

def test_left_right_rotate():
  # Test left_right_rotate
  test2 = Tree(10,left=None, right=11)
  test1 = Tree(12, left=test2, right=None)
  test1.print_node()
  test2.print_node()
  test = left_right_rotate(test1)
  test.print_node()

def test_right_left_rotate():
  # Test right_left_rotate
  test2 = Tree(12,left=11, right=None)
  test1 = Tree(10, left=None, right=test2)
  test1.print_node()
  test2.print_node()
  test = right_left_rotate(test1)
  test.print_node()

if __name__ == "__main__":
  print "Calling test_left_rotate"
  test_left_rotate()
  print "Calling test_right_rotate"
  test_right_rotate()
  print "Calling test_left_right_rotate"
  test_left_right_rotate()
  print "calling test_right_left_rotate"
  test_right_left_rotate()
  