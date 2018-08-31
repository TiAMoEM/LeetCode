# Read from the file file.txt and output all valid phone numbers to stdout.
grep -p '^(\d{3}-|\(\d{3}\))\d{3}-\d{4}$' file.txt