//this solution is essentially implementing an adder
// L represents - ; R represents +
// since we need to count the number of zeroes starting from the top,
// its just sequential logic, update every clock cycle
// check accumulated sum every cycle, if 0, increment answer by 1

//first bit after pre-processing the input data represents add or subtract operation
//all subsequent bits/bytes are effectively the number to be added/subtracted


//INTUITION - simple adder circuit -> add a module operator for every clock cycle to keep track of number of zeros

module processor(clk, rst, i_dataValid, i_packet
                 o_sum);


                 input clk;
                 input rst;
                 input i_dataValid;
                 input [31:0] i_packet;
                 output [32:0] o_sum;

                 localparam p_initSum = 32'd50;

                 assign wire iw_direction = i_packet[31];  //iw = internal wire
                 assign wire [30:0] iw_val = i_packet[30:0];

                 signed reg [31:0] ir_counter; //ir = internal reg

                 always @(posedge clk) begin 
                    if (rst) begin 
                        ir_counter <= p_initSum;
                    end else if (i_dataValid) begin 
                        if (!iw_direction) ir_counter <= ir_counter - iw_val;
                        else if (iw_direction) ir_counter <= ir_counter + ir_val;

                        
                    end
                 end

                 assign o_sum = ir_counter;
endmodule