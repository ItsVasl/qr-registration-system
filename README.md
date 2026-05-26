# QR Attendance Verification System

A QR-based registration and verification system built for an NGO to automate attendee management.

## Overview
This system processes registration data from an Excel file, generates unique QR codes for each participant, and sends them via email. At the event, these QR codes can be scanned to verify registration status instantly.

## Features
- Reads and processes registration data from Excel (pandas)
- Generates unique QR codes for each participant
- Sends automated emails with QR codes attached
- Handles multiple registration states (e.g. confirmed, partially paid)
- Reduces manual verification effort during events

## Workflow
1. Load participant data from Excel
2. Generate QR code containing participant details
3. Send QR code via email to each registered user
4. Use QR scanning at entry for real-time verification

## Tech Stack
- Python
- pandas (data handling)
- qrcode (QR generation)
- smtplib (email automation)

## Context
Built for real-world use in an NGO event(Gurukul ELP) to streamline registration and entry verification.

## Notes
This project was designed with simplicity and reliability in mind, focusing on automating repetitive manual tasks.
