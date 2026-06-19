def flying_cowlyn():
    f=open("cowlyn_pandey.txt","r")
    count=0
    for line in f:
        if line.startswith("A") or  line.startswith("a"):
            count+=1
    f.close()
    print("Number of Lines starting with A or a",count)



if __name__=="__main__":
    flying_cowlyn()

