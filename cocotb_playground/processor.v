//this solution is essentially implementing an adder
// L represents - ; R represents +
// since we need to count the number of zeroes starting from the top,
// its just sequential logic, update every clock cycle
// check accumulated sum every cycle, if 0, increment answer by 1

//first bit after pre-processing the input data represents add or subtract operation
//all subsequent bits/bytes are effectively the number to be added/subtracted


//INTUITION - simple adder circuit -> add a module operator for every clock cycle to keep track of number of zeros

module processor(clk, rst, i_dataValid, i_packet,
                 o_answer);


                 input clk;
                 input rst;
                 input i_dataValid;
                 input [31:0] i_packet;
                 output reg [31:0] o_answer;

                 localparam p_initSum = 32'd50;

                 wire iw_direction;
                 wire [30:0] iw_val;

                 assign iw_direction = i_packet[31];  //iw = internal wire
                 assign iw_val = i_packet[30:0];

                 reg signed [31:0] ir_counter; //ir = internal reg
                 reg signed [31:0] ir_newCounter;

                 always @(*) begin 
                    if (!iw_direction) ir_newCounter = ir_counter - iw_val;
                    else               ir_newCounter = ir_counter + iw_val;
                 end

                 always @(posedge clk) begin 
                    if (rst) begin 
                        ir_counter <= p_initSum;
                        o_answer <= 0;
                    end else if (i_dataValid) begin 
                        ir_counter <= ir_newCounter;

                        if (ir_newCounter % 100 == 0) o_answer <= o_answer + 1;
                    end
                 end
endmodule