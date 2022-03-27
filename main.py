import os, sys

ARGS = sys.argv
FortunePath = open(str(ARGS[1]),"r")
lines = FortunePath.read()
line = str(lines)

line = line.replace('%', ' ')


if not os.path.exists("FortuneResourcePack"):
    os.mkdir("FortuneResourcePack")
if not os.path.exists("FortuneResourcePack/assets"):
    os.mkdir("FortuneResourcePack/assets")
if not os.path.exists("FortuneResourcePack/assets/minecraft"):
    os.mkdir("FortuneResourcePack/assets/minecraft")
if not os.path.exists("FortuneResourcePack/assets/minecraft/texts"):
    os.mkdir("FortuneResourcePack/assets/minecraft/texts")

with open("FortuneResourcePack/pack.mcmeta", "a") as pack:
    pack.writelines(["{\n", '    "pack_format": 8,\n', '    "description": "Fortune Resource pack"\n', '  }\n', '}\n' ])

splashes = open("splashes.txt", "w")
splashes.write(str(line))

with open('splashes.txt', 'r') as splash:
    lines = splash.readlines()
    with open('FortuneResourcePack/assets/minecraft/texts/splashes.txt', 'w') as fw:
        for line in lines:
            if line.find('BOFH excuse') == -1:
                fw.write(line)
splashes.close()

print("Saved resource pack to folder FortuneResourcePack")
