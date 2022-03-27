import os, sys, shutil, zipfile

# Variables
ARGS = sys.argv
FortunePath = open(str(ARGS[1]),"r")
lines = FortunePath.read()
line = str(lines)
resource_pack_file_name = "FortuneResourcePack.zip"
line = line.replace('%', ' ')

# Create needed paths
if not os.path.exists("assets"):
    os.mkdir("assets")
if not os.path.exists("assets/minecraft"):
    os.mkdir("assets/minecraft")
if not os.path.exists("assets/minecraft/texts"):
    os.mkdir("assets/minecraft/texts")

# Create pack.mcmeta file
with open("pack.mcmeta", "a") as pack:
     pack.writelines(["{\n", '  "pack_format": 8,\n', '    "description": "Fortune Resource pack"\n', '  }\n', '}\n' ])

# Create splashes.txt file ZipFile.testzip()¶
splashes = open("splashes.txt", "a")
splashes.write(str(line))
with open('splashes.txt', 'r') as splash:
    lines = splash.readlines()
    with open('assets/minecraft/texts/splashes.txt', 'w') as fw:
        for line in lines:
            if line.find('BOFH excuse') == -1:
                fw.write(line)
splashes.close()

# Put everything in a zip file
with zipfile.ZipFile(resource_pack_file_name, 'w') as myzip:
    myzip.write('assets/minecraft/texts/splashes.txt')
    myzip.write('pack.mcmeta')

# Cleanup files
os.remove("splashes.txt")
shutil.rmtree("assets")

# Print
print("Saved resource pack to folder FortuneResourcePack.zip")
