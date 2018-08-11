import unittest, random, time, datetime

from timestamps import Timestamp

# TODO: Implement __eq__ to not have to rely on private attributes

class InitializationTests(unittest.TestCase):
	def test_failure_1(self):
		with self.assertRaises(ValueError) as cm:
			Timestamp('x')

	def test_failure_2(self):
		with self.assertRaises(ValueError) as cm:
			Timestamp(1.0, _float=1)

	def test_float(self):
		# Initialize with float
		i = random.random()*time.time()
		j = Timestamp(i)
		k = Timestamp(_float=i)
		l = Timestamp.from_float(k._float)
		self.assertEqual(j._float, i)
		self.assertEqual(j._float, k._float)
		self.assertEqual(l._float, j._float)

		del i, j, k, l

	def test_datetime(self):
		# Initialize with datetime
		d = datetime.datetime.now()
		timestamp = d.timestamp()
		t1 = Timestamp(timestamp)
		t2 = Timestamp(_datetime=d)
		t3 = Timestamp.from_datetime(d)

		self.assertEqual(t1._float, t2._float)
		self.assertEqual(t3._float, timestamp)

		del d, timestamp, t1, t2, t3

	def test_hex(self):
		# Initialize with hex
		t1 = Timestamp('0xff')
		t2 = Timestamp.from_hex(' ff ')
		t3 = Timestamp(_hex='#FF ')
		t4 = Timestamp('00fF')

		self.assertEqual(t1._float, t2._float)
		self.assertEqual(t2._float, t3._float)
		self.assertEqual(t3._float, t4._float)
		self.assertEqual(t4._float, t1._float)

		del t1, t2, t3, t4

	def test_now(self):
		# now = Timestamp.now()
		pass
