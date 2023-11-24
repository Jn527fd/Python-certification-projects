class Rectangle:

  def __init__(self, width=-1, height=-1):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width**2 + self.height**2)**0.5)

  def get_picture(self):
    str = ''
    if self.height > 50 or self.width > 50:
      return 'Too big for picture.'
    else:
      for i in range(self.height):
        str += '*' * self.width + '\n'
      return str

  def get_amount_inside(self, shape):
    width_ratio = self.width // shape.width
    height_ratio = self.height // shape.height
    return width_ratio * height_ratio

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):

  def __init__(self, length):
    super().set_height(length)
    super().set_width(length)

  def set_side(self, length):
    super().set_height(length)
    super().set_width(length)

  def __str__(self):
    return f"Square(side={self.width})"
