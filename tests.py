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

	def test_failure_3(self):
		with self.assertRaises(ValueError):
			Timestamp(-1)

	def test_failure_3(self):
		with self.assertRaises(ValueError):
			Timestamp('-0x1')


	def test_float(self):
		# Initialize with float
		i = random.random()*time.time()
		j = Timestamp(i)
		k = Timestamp(_float=i)
		l = Timestamp.from_float(k._float)
		self.assertEqual(float(j), i)
		self.assertEqual(float(j), k._float)
		self.assertEqual(float(l), float(j))

		del i, j, k, l

	def test_datetime(self):
		# Initialize with datetime
		d = datetime.datetime.now()
		timestamp = d.timestamp()
		t1 = Timestamp(timestamp)
		t2 = Timestamp(_datetime=d)
		t3 = Timestamp.from_datetime(d)

		self.assertEqual(float(t1), float(t2))
		self.assertEqual(float(t3), timestamp)

		del d, timestamp, t1, t2, t3

	def test_hex(self):
		# Initialize with hex
		t1 = Timestamp('0xff')
		t2 = Timestamp.from_hex(' ff ')
		t3 = Timestamp(_hex='#FF ')
		t4 = Timestamp('00fF')

		self.assertEqual(float(t1), float(t2))
		self.assertEqual(float(t2), float(t3))
		self.assertEqual(float(t3), float(t4))
		self.assertEqual(float(t4), float(t1))

		del t1, t2, t3, t4

	def test_now(self):
		now = Timestamp.now()

class CompareTests(unittest.TestCase):
	def test_now(self):
		for a, b in (
			(Timestamp.now(), Timestamp.now()),
			(Timestamp(' 0xff'), Timestamp.now()),
			(0.0, Timestamp('ff')),
			(Timestamp.now(), time.time()),
			(Timestamp(Timestamp.now()), time.time())
		):

			self.assertGreater(b, a)
			self.assertLess(a, b)

			self.assertGreaterEqual(b, a)
			self.assertLessEqual(a, b)

			self.assertEqual(a, a)
			self.assertEqual(b, b)

			self.assertNotEqual(a, b)

class OperatorTests(unittest.TestCase):
	def test_pos(self):
		t = Timestamp.now()
		assert t is +t

		t = Timestamp('0x01')
		assert t is +t
