//this solution is essentially implementing an adder
// L represents - ; R represents -
// since we need to count the number of zeroes starting from the top,
// its just sequential logic, update every clock cycle
// check accumulated sum every cycle, if 0, increment answer by 1

//NOTE - i converted my puzzle input with the following encoding
// R26 - 026, L26 = 126 => first char is encoded with 1 or 0 


module solution(input clk,
                input logic data_valid,
                output answer); 
                
                
localparam INPUT_SIZE = 'd4126; //4126 lines in my puzzle input
localparam WIDTH =  'd11; //took the liberty to do 1+10 bits as the input, 1st bit represents sign and next 10 bits represent the number
localparam INPUT_ADDR_SIZE = $clog2(INPUT_SIZE);

logic [WIDTH-1: 0] puzzle_input [0: INPUT_SIZE-1];
// needs to init at sim time using $readmemb("../puzzle_inputs/day1.mem", puzzle_input)

logic [10:0] counter = 'd0; 
logic [$clog2(INPUT_SIZE-1):0] current_index = 'd0

always @(posedge clk) begin
    if (data_valid) begin 
        current_index <= current_index + 1;
        if (!puzzle_input[current_index][0]) current_sum <= current_sum + puzzle_input[current_index][1:];
        else if current_sum <= current_sum - puzzle_input[current_index][1:];
        if (!current_sum) counter <= counter + 1;
        if (current_index == INPUT_SIZE-1) data_valid <= 1'b0;
    end

answer = counter;

 end

endmodule