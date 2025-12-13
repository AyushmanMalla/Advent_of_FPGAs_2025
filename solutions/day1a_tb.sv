`timescale 1ns/1ps

module tb_processor;

    // DUT signals
    reg         clk;
    reg         rst;
    reg         i_dataValid;
    reg [31:0]  i_packet;
    wire [31:0] o_answer;

    // Instantiate DUT
    processor dut (
        .clk(clk),
        .rst(rst),
        .i_dataValid(i_dataValid),
        .i_packet(i_packet),
        .o_answer(o_answer)
    );

    // Clock generation: 10ns period
    always #5 clk = ~clk;

    // Task to send a packet
    task send_packet;
        input direction;        // 1 = R (add), 0 = L (sub)
        input [30:0] value;
        begin
            @(posedge clk);
            i_dataValid <= 1'b1;
            i_packet    <= {direction, value};

            @(posedge clk);
            i_dataValid <= 1'b0;
            i_packet    <= 32'd0;
        end
    endtask

    initial begin
      // VCD dump
      $dumpfile("dump.vcd");
      $dumpvars(0, tb_processor);

      clk         = 0;
      rst         = 1;
      i_dataValid = 0;
      i_packet    = 0;

      repeat (3) @(posedge clk);
      rst = 0;

      send_packet(1'b0, 31'd68);
      send_packet(1'b0, 31'd30);
      send_packet(1'b1, 31'd48);
      send_packet(1'b0, 31'd5);
      send_packet(1'b1, 31'd60);
      send_packet(1'b0, 31'd55);
      send_packet(1'b0, 31'd1);
      send_packet(1'b0, 31'd99);
      send_packet(1'b1, 31'd14);
      send_packet(1'b0, 31'd82);

        // Wait a few cycles
        repeat (5) @(posedge clk);

        $finish;
    end

endmodule
