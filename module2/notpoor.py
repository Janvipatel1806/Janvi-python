s=input("Enter a string")
if "not" in s:
    l1=s.index("not")
    if "poor" in s:
        l2=s.index("poor")
    if l2-l1==4:
        print(s.replace("not poor","good"))
            
