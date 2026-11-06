"""Test aktualnych trzech poziomów i obu gałęzi."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name("sprawdz_poziomy.py")),run_name="__main__")
