class Deque:
  def __init__(self) -> None:
    self.items = []
  
  def is_empty(self):
    return self.items == []

  def first(self):
    return self.items[0]

  def last(self):
    return self.items[-1]

  def add_first(self, item):
    self.items.insert(0, item)

  def add_last(self, item):
    self.items.append(item)

  def delete_first(self):
    assert not self.is_empty()
    return self.items.pop(0)

  def delete_last(self):
    assert not self.is_empty()
    return self.items.pop()
  
  def print_queue(self):
    return self.items
  
  def size(self):
    return len(self.items)
