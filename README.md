# Library Management System

Custom Frappe application developed as part of the ERPNext Developer Assessment.

## Features

* Book Catalog Management
* Library Member Management
* Book Issue & Return
* Automatic Due Date Calculation
* Fine Calculation
* Fine Payment Management
* Email Notifications for Overdue Books
* Accounting Integration using Journal Entries
* Reports and Dashboard
* Naming Series for all transactions

## Technology Stack

* Frappe Framework
* ERPNext
* Python
* MariaDB

## Installation

```bash
bench get-app https://github.com/PRIYANSHICHOUHAN/library_management.git

bench --site site1.local install-app library_management
```

## Workflow

Book → Issue Book → Return Book → Fine Calculation → Journal Entry Creation → Fine Payment

## Accounting Integration

When a Fine is created:

* Library Fine Receivable (Debit)
* Library Fine Income (Credit)

Journal Entry is automatically created.

## Reports

* Overdue Books Report
* Fine Collection Report
* Outstanding Fine Report

## Naming Series

* BOOK-.YYYY.-.#####
* MEM-.YYYY.-.#####
* ISSUE-.YYYY.-.#####
* FINE-.YYYY.-.#####
* PAY-.YYYY.-.#####

## Author

Priyanshi Chouhan

