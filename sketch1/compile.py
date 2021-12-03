
import pathlib
import importlib

files = pathlib.Path(".").glob("*.py")
for f in files:
    if f.stem in ('bareflow', 'compile'):
        continue

    m = importlib.machinery.SourceFileLoader('modulename', str(f)).load_module()
    
    # resolve edges
    edges_in = []
    edges_out = []
    nodes = []
    for edge in m.bf.edge_partials:
        direction, identifier = edge
        if direction == "in":
            edges_in.append(identifier)
        else:
            edges_out.append(identifier)
    
    print("node:", f.stem)
    print("edges in:", edges_in)
    print("edges out:", edges_out)



