import os
from pathlib import Path
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer
from cocotb_tools.runner import get_runner

# ==============================================================================
# PART 1: Helper Functions & Model
# ==============================================================================

def parse_line(line):
    """
    Parses a line like "L 50" or "R 20".
    Returns the 32-bit integer packet expected by the hardware.
    L (Subtract) -> Bit 31 = 0
    R (Add)      -> Bit 31 = 1
    """
    parts = line.strip().split()
    if not parts:
        return None
        
    direction_char = parts[0]
    value = int(parts[1])
    
    # 31-bit value mask to ensure safety
    value = value & 0x7FFFFFFF
    
    if direction_char == 'L':
        # L means subtract (0 at MSB). Just the value.
        packet = value
    elif direction_char == 'R':
        # R means add (1 at MSB).
        packet = (1 << 31) | value
    else:
        raise ValueError(f"Unknown direction: {direction_char}")
        
    return packet

def python_model_step(current_counter, packet):
    """
    Simulates the hardware logic in Python to verify the result.
    """
    # Extract direction and value from packet
    direction = (packet >> 31) & 1
    value = packet & 0x7FFFFFFF
    
    if direction == 0:
        new_counter = current_counter - value
    else:
        new_counter = current_counter + value
        
    return new_counter

# ==============================================================================
# PART 2: Cocotb Test Bench
# ==============================================================================

@cocotb.test()
async def test_processor_logic(dut):
    """
    Tests the processor module against a Python model.
    """
    
    # 1. Start the Clock (Period = 10ns)
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    # 2. Initialize Inputs
    dut.i_dataValid.value = 0
    dut.i_packet.value = 0
    dut.rst.value = 1

    # 3. Reset Routine
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    dut.rst.value = 0
    await RisingEdge(dut.clk)

    # 4. Define Test Data
    # You can replace this list with file reading logic if "day1.txt" exists
    # test_lines = [
    #     "L 50",   # 50 - 50 = 0      (Hit! Count = 1)
    #     "R 100",  # 0 + 100 = 100    (Hit! Count = 2)
    #     "L 5",    # 100 - 5 = 95     (No Hit)
    #     "R 5",    # 95 + 5 = 100     (Hit! Count = 3)
    #     "L 200",  # 100 - 200 = -100 (Hit! Count = 4)
    #     "R 300",  # -100 + 300 = 200 (Hit! Count = 5)
    # ]

    test_lines = open(r"C:\Users\Ayushman\Desktop\DesktopClean\CODES\Advent_of_FPGAs_2025\puzzle_inputs\day1.txt", "r").read().splitlines()
    # Initialize Python Model state
    model_counter = 50 # Matches p_initSum
    model_answer = 0

    dut._log.info("Starting Driver Loop...")

    # 5. Driver & Monitor Loop
    for line in test_lines:
        packet = parse_line(line)
        
        # Drive the interface
        dut.i_packet.value = packet
        dut.i_dataValid.value = 1
        
        # Wait for clock edge to register input
        await RisingEdge(dut.clk)
        
        # Calculate Expected Result
        # Note: The hardware updates 'o_answer' on the SAME edge 'ir_counter' becomes divisible
        # or the NEXT? Let's check logic:
        # Hardware: if (ir_newCounter % 100 == 0) o_answer <= o_answer + 1;
        # Since 'ir_newCounter' is combinational, o_answer updates on the clock edge.
        
        model_counter = python_model_step(model_counter, packet)
        
        if model_counter % 100 == 0:
            model_answer += 1
            dut._log.info(f"Input: {line} -> Counter: {model_counter} -> HIT! Expected Answer: {model_answer}")
        else:
            dut._log.info(f"Input: {line} -> Counter: {model_counter}")

        # The DUT updates signals on the clock edge. 
        # We need to wait a tiny bit (ReadOnly phase) or check on next edge to see the result.
        # Since we just passed RisingEdge, the values *just* updated.
        
        # Allow signals to settle (delta cycle)
        await Timer(1, units='ns') 
        
        # Check Results
        actual_answer = dut.o_answer.value.integer
        assert actual_answer == model_answer, \
            f"Mismatch! Line: {line}, Expected: {model_answer}, Got: {actual_answer}"

    # Cleanup
    dut.i_dataValid.value = 0
    await RisingEdge(dut.clk)
    dut._log.info("Test Passed!")


# ==============================================================================
# PART 3: Python Runner (Pytest Interface)
# ==============================================================================

def test_processor_runner():
    """
    Configuration for the simulator.
    """
    sim = os.getenv("SIM", "icarus")
    
    # Get the directory of this python file
    proj_path = Path(__file__).resolve().parent
    
    # Assuming Verilog file is in the same directory and named 'processor.sv'
    # Change "processor.sv" below if your file is named differently
    sources = [proj_path / "processor.v"]

    runner = get_runner(sim)
    
    runner.build(
        sources=sources,
        hdl_toplevel="processor", # Must match the module name in Verilog
        always=True,
        timescale=("1ns", "1ps")
    )

    runner.test(
        hdl_toplevel="processor",
        test_module=Path(__file__).stem, # Points back to this file
    )

if __name__ == "__main__":
    test_processor_runner()