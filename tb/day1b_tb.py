import os 
from pathlib import Path
import cocotb
from cocotb.triggers import Timer, FallingEdge, RisingEdge
from cocotb_tools.runner import get_runner
from cocotb.clock import Clock

ROOT_DIR = Path(__file__).resolve().parent.parent
MODULE_DIR = os.path.join(ROOT_DIR, "solutions")
SOURCES = [os.path.join(MODULE_DIR, "day1b.v")]
TOP_LEVEL = "processor"
PUZZLE_PATH = os.path.join(ROOT_DIR, "puzzle_inputs/day1.txt")

def parse_line(puzzleLine):
    """
    Parse a given line of the form "R 32".
    Return a 32-bit value(the packet) of this input line

    L (Subtract) -> Bit 31 = 0
    R (Add)      -> Bit 31 = 1
    """

    direction_char = puzzleLine.split()[0]
    val = int(puzzleLine.split()[1])

    val = val & 0x7FFFFFFF #bitwise and to get the first 31 bits of the number
    if direction_char == 'L':
        packet = val
    else:
        packet = (1 << 31) | val #push 1 to the 32nd bit of the val
    
    return packet

def python_model(currentCounter, puzzleLine):
    """
    Python Solution to the problem to compare against for the testbench after each line
    in the puzzle input is processed
    """

    direction_char = puzzleLine.split()[0]
    val = int(puzzleLine.split()[1])

    if direction_char == 'L':
        newCounter = currentCounter - val
        zerosInstep = ((currentCounter - 1)// 100) - ((newCounter - 1)// 100)
    else:
        newCounter = currentCounter + val
        zerosInstep = (newCounter // 100) - (currentCounter // 100)
    return zerosInstep, newCounter

@cocotb.test()
async def test_processor(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    dut.i_dataValid.value = 0
    dut.i_packet.value = 0
    dut.rst.value = 1

    await RisingEdge(dut.clk)
    dut.rst.value = 0
    await RisingEdge(dut.clk)

    test_lines = open(PUZZLE_PATH, 'r').read().splitlines()

    model_counter = 50
    model_answer = 0

    dut._log.info("Starting Driver Loop...")

    for line in test_lines:
        packet = parse_line(line)
        
        dut.i_dataValid.value = 1
        dut.i_packet.value = packet

        await RisingEdge(dut.clk)

        model_zerosInStep, model_counter = python_model(model_counter, line)

        if model_zerosInStep > 0:
            model_answer += model_zerosInStep
            dut._log.info(f"Input: {line} -> Counter: {model_counter} -> HIT! current answer: {model_answer}")
        else:
            dut._log.info(f"Input: {line} -> Counter: {model_counter}")
        
        await Timer (1, unit="ns")
        actual_answer = dut.o_answer.value.integer

        assert actual_answer == model_answer, \
            f"Mismatch! Line: {line}, Expected: {model_answer}, Receieved: {actual_answer}"
        

    dut.i_dataValid.value = 0
    dut._log.info("Test Passed!")

def test_my_design_runner():
    sim = os.getenv("SIM", "icarus")
    runner = get_runner(sim)
    runner.build(
        sources=SOURCES,
        hdl_toplevel=TOP_LEVEL,
        timescale=("1ns", "1ps"),
        always=True
    )
    runner.test(hdl_toplevel=TOP_LEVEL, test_module=Path(__file__).stem)


async def generate_clock(dut):
    """Generate clock pulses."""

    for _ in range(10):
        dut.clk.value = 0
        await Timer(1, unit="ns")
        dut.clk.value = 1
        await Timer(1, unit="ns")

if __name__ == "__main__":
    test_my_design_runner()