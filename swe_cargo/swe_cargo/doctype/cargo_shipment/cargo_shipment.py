# Copyright (c) 2026, cargo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _


class CargoShipment(Document):

    def validate(self):
        """
        Runs before save.
        Good place for business rules.
        """
        self._validate_basic_rules()

    def before_insert(self):
        """
        Runs only when document is first created.
        Useful for defaults / auto values.
        """
        self._set_initial_status()

    # -------------------------
    # Internal Helpers
    # -------------------------

    def _set_initial_status(self):
        """
        Minimal defensive defaulting.
        """
        if not self.status:
            self.status = "Ready"

    def _validate_basic_rules(self):
        """
        Very light V1 validation.
        Extend later via agent turns.
        """

        if self.weight and self.weight < 0:
            frappe.throw(_("Weight cannot be negative."))

        if self.declared_value and self.declared_value < 0:
            frappe.throw(_("Declared value cannot be negative."))