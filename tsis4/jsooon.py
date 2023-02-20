import json

f = open('sample_data.json')
y = json.load(f)
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")
for i in y["imdata"]:
    l = list()
    l.append(i["l1PhysIf"]["attributes"]["dn"])
    l.append(i["l1PhysIf"]["attributes"]["speed"])
    l.append(i["l1PhysIf"]["attributes"]["descr"])
    l.append(i["l1PhysIf"]["attributes"]["mtu"])
    print(*l, sep="\t")

f.close()
