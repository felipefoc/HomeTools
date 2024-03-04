from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class VirtualMachine:
    name: str
    state: bool
    cpu_usage: float
    memory_assigned: float
    uptime: datetime
    status: str
    version: float

def format_vm(source_string) -> VirtualMachine:
    row_to_split = source_string.split()
    if len(row_to_split) > 8:
        row_to_split.reverse()
        index_off_on = row_to_split.index('Off') if 'Off' in row_to_split else row_to_split.index('On')
        problematic_name = ' '.join(reversed(row_to_split[index_off_on + 1:]))
        row_to_split = row_to_split[:index_off_on + 1]
        row_to_split.append(problematic_name)
        row_to_split.reverse()
    
    values = [v.strip() for v in row_to_split]

    vm = VirtualMachine(
        name=values[0],
        state=values[1],
        cpu_usage=values[2],
        memory_assigned=values[3],
        uptime=values[4],
        status=values[5],
        version=values[6]
    )
    return vm

def format_output(output) -> list:
    vms = []
    # Dividir as linhas do output
    lines = output.strip().split('\n')

    for line in lines[2:]:
        dict_vm = asdict(format_vm(line))
        vms.append(dict_vm)

    print(vms)
    return vms