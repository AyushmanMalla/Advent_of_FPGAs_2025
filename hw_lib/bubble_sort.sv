// Since we are describing hardware, we cannot deal with dynamic resizing of arrays -> must define the module appropriately

// ================================
//          PARAMETERS
// 1. input arr size
// 2. size of element being stored in bits
// ================================


module sorter(input_arr, output_arr, clk);

    parameter INPUT_ARR_SIZE = 100,
              ELEMENT_SIZE = 32;    //default size for int - 32 bits

    input logic [ELEMENT_SIZE-1: 0] input_arr[0:INPUT_ARR_SIZE-1];
    input clk;

    output logic [ELEMENT_SIZE-1: 0] output_arr[0:INPUT_ARR_SIZE-1];


    
    //internal state vars
    localparam reg_width = $clog2(INPUT_ARR_SIZE);
    reg reg_width i_limit = INPUT_ARR_SIZE - 1;
    reg reg_width iter_count = 1;
    reg swapped = 1'b0; //init to false by default

    always @(posedge clk) begin
        //is it possible to complete one entire iteration per cycle
        

    end 


endmodule
