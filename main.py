import os, sys, shutil, zipfile

resource_pack_file_name = "FortuneResourcePack.zip"

ARGS = sys.argv
if (str(ARGS[1]).__contains__(".dat")):
    ARGS[1] = str(ARGS[1])[:-4]
if os.path.exists(resource_pack_file_name):
    os.remove(resource_pack_file_name)


count = len(ARGS)
count = count - 1
for i in range(count):
    counts = i + 1
    FortunePath = open(str(ARGS[counts]),"r")
    lines = FortunePath.read()
    line = str(lines)
    line = line.replace('\n', '')
    line = line.replace('%', ' \n')
    splashes = open("splashes.txt", "a")
    splashes.write(str(line))

# Create needed paths
if not os.path.exists("assets"):
    os.mkdir("assets")
if not os.path.exists("assets/minecraft"):
    os.mkdir("assets/minecraft")
if not os.path.exists("assets/minecraft/texts"):
    os.mkdir("assets/minecraft/texts")


# Create splashes.txt file


with open('splashes.txt', 'r') as splash:
    lines = splash.readlines()
    with open('assets/minecraft/texts/splashes.txt', 'w') as fw:
        for line in lines:
            if not line.isspace():
                fw.write(line)
splashes.close()

# Put everything in a zip file
with zipfile.ZipFile(resource_pack_file_name, 'w') as myzip:
    myzip.write('assets/minecraft/texts/splashes.txt')
    myzip.write('pack.mcmeta')
    myzip.write('pack.png')

# Cleanup
os.remove("splashes.txt")
shutil.rmtree("assets")

# Print
print("Saved resource pack to folder " + resource_pack_file_name)
