from cx_Freeze import setup, Executable

setup(
    name="Tucil",
    version="1.0",
    description="Bruteforcing Cyberpunk 2077 Hacking minigame",
    executables=[Executable("Cyberpunk_BruteForce.py")]
)