import cx_Freeze

executables = [cx_Freeze.Executable("AutoTyper.py")]

cx_Freeze.setup(
    name="AutoTyper Application",
    version="1.0",
    description="Introduce errors with 20% probability (80% accuracy)",
    executables=executables
)