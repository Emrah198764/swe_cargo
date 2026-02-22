# swe_cargo

A custom Frappe / ERPNext application designed to model a realistic cargo and shipment management workflow.

The application focuses on shipment requests, operational processing, tracking visibility, and status-driven logistics flows.

---

## Project Overview

`swe_cargo` simulates a structured cargo lifecycle inside ERPNext.

The system models the following core business flow:

Shipment Request → Operational Review → Shipment Creation → Tracking Events → Delivery Lifecycle

Primary objectives:

- Manage shipment requests
- Control shipment lifecycle via statuses
- Track cargo movements through events
- Enforce operational validations
- Provide a clean, extensible logistics model

This project is intentionally designed for iterative development and progressive feature expansion.

---

## Functional Scope (V1)

Current functional areas include:

- Shipment Request management
- Shipment lifecycle tracking
- Status-driven workflow logic
- Tracking / milestone events
- Server-side validations
- Operational state transitions

Planned enhancements:

- Advanced workflow rules
- Pricing / quotation logic
- Carrier assignment model
- SLA & exception handling
- Reporting & dashboards

---

## Technical Context

Built as a **Frappe custom app**.

Design principles:

- Workflow-centric architecture
- Clear DocType responsibility separation
- Server-side business logic enforcement
- Maintainable controller structure
- Extensible event / tracking model
- No external service dependencies

---

## Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app swe_cargo