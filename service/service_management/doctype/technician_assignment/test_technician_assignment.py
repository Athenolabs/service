# Copyright (c) 2013, www.ossph.com and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Technician Assignment')

class TestTechnicianAssignment(unittest.TestCase):
	pass
