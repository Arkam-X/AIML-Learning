import sys
print("Python executable:", sys.executable)
print("Python path:")
for p in sys.path:
    print("  ", p)

print("\n" + "="*50)

try:
    import PyPDF2
    print("✓ PyPDF2 imported successfully")
except ImportError as e:
    print("✗ PyPDF2 failed:", e)

try:
    import pypdf
    print("✓ pypdf imported successfully") 
except ImportError as e:
    print("✗ pypdf failed:", e)

try:
    import google.generativeai as genai
    print("✓ google.generativeai imported successfully")
except ImportError as e:
    print("✗ google.generativeai failed:", e)

try:
    import streamlit as st
    print("✓ streamlit imported successfully")
except ImportError as e:
    print("✗ streamlit failed:", e)