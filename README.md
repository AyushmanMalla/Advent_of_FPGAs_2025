# Advent of FPGA 2025

This repository contains solutions and experiments for the [Jane Street Advent of FPGA Challenge 2025](https://blog.janestreet.com/advent-of-fpga-challenge-2025/).

## Project Structure

*   **`algo_prototypes/`**: Python scripts for prototyping algorithms and pseudocode to understand the puzzles before hardware implementation.
*   **`hw_lib/`**: Reusable hardware modules implementing standard software data structures and algorithms (e.g., sorting networks, hash maps) for plug-and-play use in solutions.
*   **`tb/`**: Testbenches written in Python using [cocotb](https://www.cocotb.org/) for verification.
*   **`solutions/`**: The actual RTL modules written to solve the problem. primarily written using verilog.
*   **`python_solutions/`**: Python solns written to be used for testbench modeling and for better understanding the puzzle :)
*   **`puzzle_inputs/`**: Python solns written to be used for testbench modeling and for better understanding the puzzle :)

## Setup

To get started, clone the repository and run the setup script for your operating system. This will install Python dependencies (like `cocotb`) and the Icarus Verilog simulator.

### Windows
Run the PowerShell script:
```powershell
.\setup_env.ps1
```

### Linux / macOS
Run the shell script:
```bash
bash setup_env.sh
```
Or:
```bash
chmod +x setup_env.sh
./setup_env.sh
```

## Running Tests
Once setup is complete, you can run tests using `cocotb` (usually via `pytest` or a Makefile, depending on the specific folder).