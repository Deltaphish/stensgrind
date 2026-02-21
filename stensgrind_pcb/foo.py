import re

content = ""
with open("stensgrind_pcb.kicad_pcb", "r") as f:
    content = f.read()

## GET NETS

result = re.findall(r'\(net (\d+) "(.*)"\)', content)
nets = {}
for (id,net) in result:
    nets[net] = id
print(nets)

for col in range(1,15):
    net = f"ROW{col}"
    net_id = nets[net]
    new_net = f"/RIGHT_SIDE/TOUCH_ROW{col}"
    new_net_id = nets[new_net]
    if net_id == None:
        print(f"OWW {net} {new_net} {col}")
    content = re.sub(f'\(net {net_id} "{net}"\)', f'(net {new_net_id} "{new_net}")', content)
    content = re.sub(f'\(net {net_id}\)', f'(net {new_net_id})', content)

with open("stensgrind_pcb.kicad_pcb", "w") as f:
    f.write(content)
