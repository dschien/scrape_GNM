#!/Users/schien/workspaces/virtualenvs/modelling/bin/python

import json
import pygraphviz as pg

def loadgraph(fname):
        G=pg.AGraph(directed=True)
        for line in open(fname):
            j=json.loads(line)
            url=j["url"]
            G.add_node(url)
            for linked_url in j["linkedurls"]:
                G.add_edge(url,linked_url)
        return G

if __name__=='__main__':
        G=loadgraph("sitegraph_single.json")
        G.layout(prog='dot',args="-Grankdir=LR")
        G.draw("sitegraph.png")