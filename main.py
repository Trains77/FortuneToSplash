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
    pack.writelines(["{\n", '    "pack_format": 8,\n', '    "description": "FortuneToSplashes Resource pack"\n', '  }\n', '}\n' ])

splashes = open("FortuneResourcePack/assets/minecraft/texts/splashes.txt", "w")
splashes.write(str(line))
splashes.close()

print("Saved resource pack to folder FortuneResourcePack")
