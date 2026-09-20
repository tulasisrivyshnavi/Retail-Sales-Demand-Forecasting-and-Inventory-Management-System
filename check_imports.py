import sys
print("Python:", sys.version[:10])
libs = [
    ("fastapi", "FastAPI"),
    ("uvicorn", "Uvicorn"),
    ("sqlalchemy", "SQLAlchemy"),
    ("pymysql", "PyMySQL"),
    ("pydantic", "Pydantic"),
    ("pydantic_settings", "pydantic-settings"),
    ("dotenv", "python-dotenv"),
    ("pandas", "pandas"),
    ("numpy", "numpy"),
    ("sklearn", "scikit-learn"),
    ("xgboost", "XGBoost"),
    ("joblib", "joblib"),
    ("openpyxl", "openpyxl"),
    ("matplotlib", "matplotlib"),
    ("seaborn", "seaborn"),
    ("pytest", "pytest"),
    ("httpx", "httpx"),
]
all_ok = True
for mod, label in libs:
    try:
        m = __import__(mod)
        v = getattr(m, "__version__", "n/a")
        print(f"  [OK]   {label:<22} {v}")
    except ImportError as e:
        print(f"  [FAIL] {label:<22} {e}")
        all_ok = False
print()
print("All packages OK. Phase 0 ready." if all_ok else "Some packages MISSING - re-run pip install.")
