`timescale 1ns/1ps

module tb_solution;

    logic clk = 0;
    logic data_valid = 0;
    logic [31:0] data;
    logic [31:0] answer;

    // Instantiate DUT
    day1a dut (
        .clk(clk),
        .data_valid(data_valid),
        .data(data),
        .answer(answer)
    );

    // Clock generation (100 MHz)
    always #5 clk = ~clk;

    // integer fd; //file descriptor??
    // string line;
    // byte op_char;
    // int  number;

    // Convert text line → 32-bit packed data word
    function automatic [31:0] pack_data(input byte op, input int num);
        pack_data = {op, num[23:0]};  // op is 8 bits, num is 24 bits
    endfunction

    // initial begin
    //     // Open file
    //     fd = $fopen("../puzzle_inputs/day1a.txt", "r");
    //     if (fd == 0) begin
    //         $fatal("ERROR: Could not open input.txt");
    //     end

    //     $display("Starting simulation...");
        
    //     // Read each line while clocking data into DUT
    //     while (!$feof(fd)) begin

    //         // Read a line from file
    //         void'($fgets(line, fd));

    //         // Parse:   <char><integer>
    //         // Example: "R26"
    //         if ($sscanf(line, "%c%d", op_char, number) == 2) begin
    //             @(posedge clk);
    //             data       = pack_data(op_char, number);
    //             data_valid = 1;

    //             $display("Time %0t:  Read '%s' → op=%c num=%0d, packed=%h",
    //                       $time, line, op_char, number, data);

    //         end else begin
    //             $display("WARNING: Could not parse line '%s'", line);
    //         end

    //     end

    //     // Stop sending new data
    //     @(posedge clk);
    //     data_valid = 0;

    //     // Let DUT run for a few more cycles
    //     repeat (10) @(posedge clk);

    //     $display("Final answer = %0d", answer);

    //     $finish;
    // end

    initial begin 
        data_valid = 1;
        #5;
        data = 32'h4c000044;
        #10;
        data = 32'h4c00001e;

    end
    // Waveform dump
    initial begin
        $dumpfile("wave.vcd");
        $dumpvars(0, tb_solution);
    end

endmodule
