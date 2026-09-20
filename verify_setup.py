"""
verify_setup.py — Run this after installing requirements to confirm
everything needed for Phase 0 is importable.

Run it with:  .\\venv\\Scripts\\python verify_setup.py
"""

import sys

print(f"Python: {sys.version}")
print()

checks = [
    ("fastapi",           "FastAPI"),
    ("uvicorn",           "Uvicorn"),
    ("sqlalchemy",        "SQLAlchemy"),
    ("pymysql",           "PyMySQL"),
    ("pydantic",          "Pydantic"),
    ("pydantic_settings", "pydantic-settings"),
    ("dotenv",            "python-dotenv"),
    ("pandas",            "pandas"),
    ("numpy",             "numpy"),
    ("sklearn",           "scikit-learn"),
    ("xgboost",           "XGBoost"),
    ("joblib",            "joblib"),
    ("openpyxl",          "openpyxl"),
    ("matplotlib",        "matplotlib"),
    ("seaborn",           "seaborn"),
    ("pytest",            "pytest"),
    ("httpx",             "httpx"),
]

all_ok = True
for module, label in checks:
    try:
        mod = __import__(module)
        version = getattr(mod, "__version__", "n/a")
        print(f"  [OK]   {label:<22} {version}")
    except ImportError as exc:
        print(f"  [FAIL] {label:<22} MISSING - {exc}")
        all_ok = False

print()
if all_ok:
    print("All packages OK. Phase 0 is ready.")
else:
    print("Some packages are missing. Re-run:  pip install -r backend\\requirements.txt")
