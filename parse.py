import re


def parse_from_edgelist(filenamein, filenameout):
    with open(filenamein) as fin:
        with open(filenameout,"w") as fout:
            for line in fin:
                pattern = re.compile(r'\bGraph\s+([a-zA-Z0-9_]+)\b')
                match = pattern.match(line)
                if match:
                    print ("Found: Graph ", match.group(1))
                    fout.write("/* #name=Graph")
                    fout.write(match.group(1))
                    fout.write("\n")
                    fout.write(" */\n")
                    line = fin.readline()
                    for line in fin:
                        pattern = re.compile(r'(\d+) (\d+)')
                        match = pattern.findall(line)
                        if match:
                            for a, b in match:
                                edgestr = "a"+a+"a"+b
                                fout.write(edgestr)
                                fout.write(" ")
                        else:
                            break
                        fout.write("\n")

                    fout.write("END END\n\n")






parse_from_edgelist('graph5c.dat',"graph5c.fcg")
parse_from_edgelist('graph6c.dat',"graph6c.fcg")
parse_from_edgelist('graph7c.dat',"graph7c.fcg")
parse_from_edgelist('graph8c.dat',"graph8c.fcg")


