# PRD: sgPhoneNumbers65

## Overview
A Python tool for Singapore phone number validation and generation. Two scripts: one generates all possible 8-prefix and 9-prefix mobile numbers, one checks a list of numbers and identifies their allocated telco (Singtel, StarHub, M1, etc.) based on official IMDA block assignments.

## Goals
- Generate all possible SG mobile numbers in 8xxx and 9xxx ranges
- Validate whether a given SG number is a real allocated number
- Identify which telco owns a number based on number block allocation

## Non-Goals
- Real-time IMDA number block API lookup
- VoIP or overseas number identification
- Porting history lookup

## User Stories
- As a developer, I want to validate user-entered phone numbers to ensure they're valid SG mobile numbers.
- As a researcher, I want to identify which telco owns a number without making a call.

## Tech Stack
- **Language**: Python 3.x
- **Libraries**: stdlib only

## Architecture
```
sgPhoneNumbers65/
├── generatephonenumbers.py  # Generates number ranges
├── checkphonenumbers.py     # Validates and telco-identifies numbers
└── results/                 # Output files
```

## Features

### Generate Numbers
- 8xxx range: 81,000,000 – 88,000,000
- 9xxx range: 90,000,000 – 98,000,000
- Writes to lists (in memory — see note on output)

### Check / Validate Numbers
- Reads input numbers from file or list
- Checks against IMDA number block assignments
- Identifies: Singtel, StarHub, M1, MVNOs, unallocated
- Writes results to `results/` folder

## Deployment / Run
```bash
python generatephonenumbers.py
python checkphonenumbers.py
```

## Constraints & Notes
- **Static block data**: telco block assignments are hardcoded; IMDA may reassign blocks over time
- **Legal**: for educational/validation purposes; do not use for unsolicited marketing (PDPA violation)
- **Prepaid**: same number may have been ported; block assignment indicates original allocating telco
