import template as temp
import yaml
import time

def generator(build_dir):
    ti = time.ctime()
    data = []
    with open('test/pass/pass1.yaml') as f:
        data = yaml.load(f, Loader= yaml.SafeLoader)

    
    
    with open(f"{build_dir}/generated.py","w") as fp:
        # Creating the groud  plane and the substrate
        fp.write(temp.template_alu.format(
            time = "",
            parameter_size ="",
            control_width="",
            cases="",
            at_default=""
        ))
        