import hashlib

class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.calculate_hash()

  def calculate_hash(self):
    return hashlib.sha256(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).hexdigest()
