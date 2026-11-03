# Lab 6 — Code and Branch Coverage Results

Run from the `LAB6` folder:

```bash
python -m pip install pytest coverage
python -m coverage run --branch -m pytest -q
python -m coverage report -m
```

Verified results:
- 23 tests passed.
- `house_painting_quote.py`: 37 statements, 0 missed; 24 branches, 0 partial; **100% statement and branch coverage**.
- The tests exercise pricing rules and boundaries, minimum quote, exterior surcharge, large-area discount, invalid jobs, paint surface coverage, rounding, wallpaper removal, and invalid painter counts.

The production module was not changed; only the tests and this report were added.
