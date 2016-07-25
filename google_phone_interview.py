def add(a, b):
	#this_a_digit = int(a[-1:])
	#this_b_digit = b % 10
	a_idx = len(a) - 1
	result = ‘’
	carry = 0
	while a_idx >= 0 or b >= 1:
        if a_idx >= 0: this_a_digit = int(a[a_idx])
		else: this_a_digit = 0

        this_b_digit = b % 10

		new_digit = this_a_digit + this_b_digit + carry
		carry = int(new_digit / 10)
		result = str(new_digit % 10) + result

		a_idx -= 1
		b = int(b / 10)
	if carry:
		result = str(carry) + result
	return result


import unittest

class TestAdd(unittest.Testcase):

    def test(self):
    	self.assertEqual(add(“97”, 3), “100”)
    	self.assertEqual(add(“0”, 0), “0”)
    	self.assertEqual(add(“5”, 5), “10”)
    	self.assertEqual(add(“100”, 900), “1000”)
    	self.assertEqual(add(“555”, 555), “1110”)
    	self.assertEqual(add(“123”, 123), “246”)
    	self.assertEqual(add(“1”, 999), “1000”)
    	self.assertEqual(add(“11111111111110”, 1), “11111111111111”)
        self.assertEqual(add(“11111111111111111111110”, 1), “11111111111111111111111”)
