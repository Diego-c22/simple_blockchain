import random
import sys
import json
from block import Block
from datetime import datetime
import hashlib



class Blockchain:
    def __init__(self):
        self.chain = []
        self.state = {}
        self.chain.append(self.create_genesis_block())
        self.previous_block = self.chain[0]

    def create_genesis_block(self):
        return Block(0, datetime.now(), "Genesis Block", "0")

    def next_block(self):
        this_index = self.previous_block.index + 1
        this_timestamp = datetime.now()
        this_data = "Hey! I'm block " + str(this_index)
        this_hash = self.previous_block.hash
        return Block(this_index, this_timestamp, this_data, this_hash)

    def create_hash(self, msg=""):
        if type(msg) != str:
            msg = json.dumps(msg, sort_keys=True)
        if sys.version_info.major == 2:
            return unicode(hashlib.sha256(msg).hexdigest(), "utf-8")
        else:
            return hashlib.sha256(str(msg).encode("utf-8")).hexdigest()
        
    def execute_transaction(self, max_value=3):
        sign = int(random.getrandbits(1)) * 2 - 1
        amount = random.randint(1, max_value)
        deposit = sign * amount
        withdraw = -deposit
        return deposit, withdraw

    def updateState(self, transaction):
        state = self.state.copy()
        for key in transaction:
            if key in state.keys():
                state[key] += transaction[key]
            else:
                state[key] = transaction[key]

    def validate_transaction(self, transaction):
        if sum(transaction.values()) is not 0:
            return False
        for key in transaction.keys():
            if key in self.state.keys():
                account_balance = self.state[key]
            else:
                account_balance = 0
            if account_balance + transaction[key] < 0:
                return False
        return True