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

                 assign iw_direction = i_packet[31];
                 assign iw_val = i_packet[30:0];

                 reg signed [31:0] ir_counter;
                 reg signed [31:0] ir_newCounter;
                 reg [31:0] ir_zerosInStep;


                 always @(*) begin 
                    if (!iw_direction) begin
                        ir_newCounter = ir_counter - iw_val;
                        ir_zerosInStep = ((ir_counter - 1) / 100) - ((ir_newCounter - 1) / 100);
                    end else begin
                        ir_newCounter = ir_counter + iw_val;
                        ir_zerosInStep = (ir_newCounter / 100) - (ir_counter /100);
                    end
                 end

                 always @(posedge clk) begin 
                    if (rst) begin 
                        ir_counter <= p_initSum;
                        o_answer <= 0;
                    end else if (i_dataValid) begin 
                        ir_counter <= ir_newCounter;
                        o_answer <= o_answer + ir_zerosInStep;
                    end
                 end
                 

endmodule
