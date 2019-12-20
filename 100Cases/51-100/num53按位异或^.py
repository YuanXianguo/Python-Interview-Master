"""程序分析：0^0=0; 0^1=1; 1^0=1; 1^1=0"""
a = 0o77
a_d = 63
a_b = 0b111111

b = 3
b_b = 0b11

num = a ^ b
num_b = 0b111100
print(num_b,num)

d = 7
d_b = 0b111

num_ = num ^ d
num_b_ = 0b111011
print(num_b_,num_)
