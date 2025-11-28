# sgPhoneNumbers65

A Python tool to generate and validate Singapore phone numbers (+65)

## Description

This project provides utilities to generate valid Singapore mobile phone numbers and validate them to identify their country of origin and telco carrier. It leverages the `phonenumbers` library to parse and extract metadata from phone numbers, making it useful for understanding Singapore's phone number allocation system.

## Features

- Generate Singapore mobile phone numbers in the 8xxx-xxxx and 9xxx-xxxx ranges
- Validate phone numbers and identify their country of origin
- Identify the telecommunications carrier (telco) for each phone number
- Export results to text files for further analysis

## Technologies Used

- Python
- phonenumbers library (for phone number parsing and validation)

## Installation

```bash
# Clone the repository
git clone https://github.com/bryanseah234/sgPhoneNumbers65.git

# Navigate to project directory
cd sgPhoneNumbers65

# Install dependencies
pip install phonenumbers
```

## Usage

```bash
# Step 1: Generate Singapore phone numbers
python generatephonenumbers.py

# Step 2: Create a 'numbers.txt' file with phone numbers to validate
# (one phone number per line, e.g., +6581234567)

# Step 3: Validate the phone numbers and identify carriers
python checkphonenumbers.py
```

**Note:** The `numbers.txt` file should contain phone numbers in international format (e.g., `+6581234567`), with one number per line. The results will be saved to `checkednumbers.txt` with format: `number | country | telco`

## Disclaimer

1. FOR EDUCATIONAL PURPOSES ONLY
2. USE AT YOUR OWN DISCRETION
3. INFORMATION MAY NOT BE ACCURATE

## License

MIT License

---

**Author:** <a href="https://github.com/bryanseah234">bryanseah234</a>
