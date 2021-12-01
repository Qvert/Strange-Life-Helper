from cx_Freeze import setup, Executable


executables = [
    Executable("converter.py", targetName="converter-currency.exe", base="Win32GUI"),
    Executable("calc.py", targetName="calculator.exe", base="Win32GUI"),
    Executable("planirov.py", targetName="planirov.exe", base="Win32GUI"),
    Executable("prognos_pog.py", targetName="Wither forecast.exe", base="Win32GUI"),
    Executable("Translator.py", targetName="Translator.exe", base="Win32GUI"),
    Executable("Zapis.py", targetName="Notebook.exe", base="Win32GUI"),
    Executable(
        "Main.py", targetName="Strange Life.exe", base="Win32GUI", icon="unnamed.ico"
    ),
]

excludes = [
    "test",
    "tkinter",
    "lib2to3",
]

zip_include_packages = ["collections", "encodings", "importlib", "wx"]

include_files = [
    "database",
    "Icons",
    "Reserve",
    "Project.py",
    "BalsamiqSans-Italic.ttf",
    "DancingScript-Bold.ttf",
    "Gif",
    "Pixmap",
    "main_true_false.txt",
    "Notebook_base.txt",
    "planirov_sec.txt",
    "wither_prov.txt"
]

options = {
    "build_exe": {
        "include_msvcr": True,
        "excludes": excludes,
        "zip_include_packages": zip_include_packages,
        "build_exe": "build_windows",
        "include_files": include_files,
    }
}

setup(
    name="Converter",
    version="2.0.3",
    description="converter currency!",
    executables=executables,
    options=options,
)
