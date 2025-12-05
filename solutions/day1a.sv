//this solution is essentially implementing an adder
// L represents - ; R represents +
// since we need to count the number of zeroes starting from the top,
// its just sequential logic, update every clock cycle
// check accumulated sum every cycle, if 0, increment answer by 1

//first byte in the input data represents add or subtract operation
//all subsequent bits/bytes are effectively the number to be added/subtracted


module day1a(input clk,
             input logic data_valid,
             input logic [31:0] data,
             output logic [31:0] answer);

    logic [7:0] op;
    logic [23:0] val;

    assign op = data[31:24];
    assign val = data[23:0];

    //internal counter and adder to keep track of the occurences of zeros and running sum
    logic [31:0] counter;
    logic signed [31:0] current_sum = 32'd50;

    always @(posedge clk) begin 
        if (data_valid) begin 
            if (op == "R") begin 
                current_sum <= current_sum + val;
            end else if (op == "L") begin 
                current_sum <= current_sum - val;
            end
        end

    if (current_sum % 100 == 0) begin 
        counter <= counter + 1;
        end
    end

    assign answer = counter;

endmodule