import template as temp
import yaml
import time
import math

def generator(build_dir):
    ti = time.ctime()
    data = []
    with open('test/pass/pass1.yaml') as f:
        data = yaml.load(f, Loader= yaml.SafeLoader)

    case_statements = ""
    for cases in data['ALU']:
        binary = bin(cases)
        case_statements += "\t\t\t" + temp.template_case.format(
            control_width = math.ceil(math.log2(len(data['ALU']))),
            encoding = binary.replace("0b",""),
            operation = data['ALU'][cases]
        )
        pass
    
    with open(f"{build_dir}/alu.sv","w") as fp:
        # Creating the groud  plane and the substrate
        fp.write(temp.template_alu.format(
            time = "",
            parameter_size = data['Alu_size'],
            control_width= math.ceil(math.log2(len(data['ALU']))),
            cases= case_statements,
            at_default=""
        ))
        