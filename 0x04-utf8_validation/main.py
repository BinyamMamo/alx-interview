#!/usr/bin/python3
"""
Main for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [467, 133, 108]
print(*[bin(d) for d in data])
print(validUTF8(data))