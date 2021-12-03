import bareflow as bf

def main():
    # scan class calls to establish connected nodes
    t1 = bf.SnowflakeTable(schema="public", table="people")
    t2 = bf.SnowflakeTable(schema="clean", table="people")

    # scan IO method alls on instances to draw edges between nodes
    for row in t1.each_row():
        clean_row = { 
            k:v for k,v in row.items() 
            if k not in ["ssn"]
        }
        t2.insert(clean_row)

main()
