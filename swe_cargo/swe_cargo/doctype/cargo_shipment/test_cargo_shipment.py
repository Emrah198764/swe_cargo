import frappe
from frappe.tests.utils import FrappeTestCase


class TestCargoShipment(FrappeTestCase):

    def test_shipment_creation(self):
        doc = frappe.get_doc({
            "doctype": "Cargo Shipment",
            "shipment_title": "Test Shipment"
        })
        doc.insert()

        self.assertIsNotNone(doc.name)

    def test_negative_weight_validation(self):
        doc = frappe.get_doc({
            "doctype": "Cargo Shipment",
            "shipment_title": "Invalid Shipment",
            "weight": -5
        })

        with self.assertRaises(frappe.ValidationError):
            doc.insert()