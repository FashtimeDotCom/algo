# coding:utf-8

from math import log

class BitMap(object):

    def __init__(self, max_num=0):
        self.bit_mask=1
        self.bucket_mask=0x40
        self.right = int(log(self.bucket_mask, 2))
        self.int_numbers = int(max_num/self.bucket_mask)+1
        self.bit_map = [0 for _ in range(self.int_numbers)]
        self.bit_init()

    def bit_init(self):
        for bucket in range(self.int_numbers):
            self.bit_map[bucket] &= 0x0
        
    def check_bit(self,number):
        return self.bit_map[number>>self.right] & self.bit_mask<<(number%self.bucket_mask)

    def set_bit(self, number):
        self.bit_map[number>>self.right] |= self.bit_mask<<(number%self.bucket_mask)
