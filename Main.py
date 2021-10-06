from LCA import LCA

def main():
        lca = LCA([10,5,20,3,7,15,25,1,4,6,8,12,17,22,27])
        print(lca.bst.printTreeOneLine())
        val1 = int(input("pick the first number: "))
        val2 = int(input("pick the second number: "))
        print(str(lca.findLCA(val1,val2)))

if __name__ == "__main__":
    main()