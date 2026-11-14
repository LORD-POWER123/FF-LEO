# Leo's Free Fire Top-Up Simulator

A safe, offline Python GUI for learning how a top-up checkout flow might look.

## Safety
- This is a simulation only.
- It does not connect to Garena, Free Fire, banks, card networks, UPI, or payment gateways.
- It never requests or stores card numbers, CVVs, OTPs, or real payment credentials.
- No real money is charged and no diamonds are delivered.

## Run from Python
1. Install Python 3 on Windows and enable "Add Python to PATH".
2. Open this folder in File Explorer.
3. Double-click `leos_topup_simulator.py`, or run:
   `python leos_topup_simulator.py`

Tkinter is included with most standard Windows Python installations.

## Build a Windows EXE
1. On a Windows PC, double-click `build_windows.bat`.
2. Wait for PyInstaller to finish.
3. Find `LeosTopUpSimulator.exe` inside the generated `dist` folder.

The EXE must be built on Windows for a normal Windows build. The batch file installs PyInstaller automatically.


## Build the EXE in GitHub (cloud Windows builder)
1. Create a new GitHub repository.
2. Upload the contents of this folder to the repository (including the hidden `.github` folder).
3. Open the repository's **Actions** tab and select **Build Windows EXE**.
4. Click **Run workflow** (or push to the `main` branch).
5. When the workflow finishes, open its run and download the `LeosTopUpSimulator-Windows` artifact.
6. Extract the downloaded artifact to get `LeosTopUpSimulator.exe`.

GitHub Actions runs this build on a Windows runner. No card information is collected; this remains an offline payment-flow simulator.
