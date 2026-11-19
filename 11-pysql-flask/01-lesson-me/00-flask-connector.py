# Flask test

try:
    from flask import Flask
except ImportError:
    print("Failed to import Flask!")
else:
    print("Flask is ready!")

