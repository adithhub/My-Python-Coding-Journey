from datetime import datetime, timedelta
import sys

today = datetime.now()
tomorrow = today + timedelta(days=1)
print(f"Tomorrow will be {tomorrow.strftime('%Y-%m-%d')}")

print(sys.version)  # Output: Python version information
