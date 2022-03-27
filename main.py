import os, sys, shutil
import zipfile

ARGS = sys.argv
FortunePath = open(str(ARGS[1]),"r")
lines = FortunePath.read()
line = str(lines)
resource_pack_file_name = "FortuneResourcePack.zip"
line = line.replace('%', ' ')



if not os.path.exists("assets"):
    os.mkdir("assets")
if not os.path.exists("assets/minecraft"):
    os.mkdir("assets/minecraft")
if not os.path.exists("assets/minecraft/texts"):
    os.mkdir("assets/minecraft/texts")

with open("pack.mcmeta", "a") as pack:
    pack.writelines(["{\n", '    "pack_format": 8,\n', '    "description": "Fortune Resource pack"\n', '  }\n', '}\n' ])

splashes = open("splashes.txt", "w")
splashes.write(str(line))


with open('splashes.txt', 'r') as splash:
    lines = splash.readlines()
    with open('assets/minecraft/texts/splashes.txt', 'w') as fw:
        for line in lines:
            if line.find('BOFH excuse') == -1:
                fw.write(line)

splashes.close()

with zipfile.ZipFile(resource_pack_file_name, 'a') as myzip:
    myzip.write('assets/minecraft/texts/splashes.txt')
    myzip.write('pack.mcmeta')

os.remove("splashes.txt")
shutil.rmtree("assets")
os.remove("pack.mcmeta")
print("Saved resource pack to folder FortuneResourcePack.zip")
