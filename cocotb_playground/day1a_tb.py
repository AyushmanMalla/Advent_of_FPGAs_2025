import os
from pathlib import Path
import cocotb
from cocotb.triggers import Timer, FallingEdge, RisingEdge
from cocotb_tools.runner import get_runner

ROOT_DIR = Path(__file__).resolve().parent.parent
MODULE_DIR = os.path.join(ROOT_DIR, "solutions")
SOURCES = os.path.join(MODULE_DIR, "day1a.v")
TOP_LEVEL = "my_design"


def file_parser(file_path):
    file_object = open("../puzzle_inputs/day1.txt", "r")
    content = file_object.read()
    packets = []
    for line in content.splitlines():
        #insert code here to pass the puzzle input as packets the module can take
        #Packet -> 32 bits of data with the first bit being encoded as the dir
        packet = 0
        if line[0] == 'L':
            #every packet is a 32-bit int
            packet = 0 << 31
            packet = 

            
             
def test_my_design_runner():
    sim = os.getenv("SIM", "icarus")
    runner = get_runner(sim)
    runner.build(
        sources=[Path(__file__).resolve().parent / "my_design.sv"],
        hdl_toplevel=TOP_LEVEL,
    )
    runner.test(hdl_toplevel=TOP_LEVEL, test_module=Path(__file__).stem)


async def generate_clock(dut):
    """Generate clock pulses."""

    for _ in range(10):
        dut.clk.value = 0
        await Timer(1, unit="ns")
        dut.clk.value = 1
        await Timer(1, unit="ns")

@cocotb.test()
async def first_test(dut):
    """Try accessing the design."""

    # for _ in range(10):
    #     dut.clk.value = 0
    #     await Timer(1, unit="ns")
    #     dut.clk.value = 1
    #     await Timer(1, unit="ns")
    # cocotb.start_soon(generate_clock(dut))
    # await Timer(5, unit="ns")  # wait a bit
    # await FallingEdge(dut.clk)  # wait for falling edge/"negedge"
    cocotb.log.info("my_signal_1 is %s", dut.my_signal_1.value)
    assert dut.my_signal_2.value == 0



@cocotb.test()
async def second_test(dut):
    """Try accessing the design."""

    cocotb.start_soon(generate_clock(dut))  # run the clock "in the background"

    await Timer(5, unit="ns")  # wait a bit
    await FallingEdge(dut.clk)  # wait for falling edge/"negedge"

    cocotb.log.info("my_signal_1 is %s", dut.my_signal_1.value)
    assert dut.my_signal_2.value == 0


if __name__ == "__main__":
    test_my_design_runner()
