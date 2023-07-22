template_alu ='''
//-------------------------------------------------------------------------------
// Author: ALUator
// Time: {time}
// Module Name: alu
//--------------------------------------------------------------------------------

module alu
#(parameter size = {parameter_size})
(input logic control,
input logic [size-1:0]src1,src2,
output logic [size-1:0]out
    );
always_comb
    begin
        case(control)
            {cases}
            default: out = {parameter_size}'b{at_default};
        endcase
    end
endmodule

'''