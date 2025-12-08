
import os
try:
    del os.environ['NVIDIA_API_KEY']
    print("Deleted key")
except KeyError:
    print("KeyError: NVIDIA_API_KEY not found")
