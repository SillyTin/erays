from erays.graphbuilder import *

if __name__ == "__main__":

    f = open('/root/projects/ethereum_decompiler/1/func_call/func_call.bin','r')
    line = f.readline().strip()
    if " " in line:
        line = line.split(" ")[1]
    f.close()
    a = GraphBuilder(line)
