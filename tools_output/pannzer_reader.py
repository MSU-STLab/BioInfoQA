lines = []

terms_initial = []
terms_followup = []

with open("../pfp_tools/set_pannzer/tlr4_original.txt", "r") as f:
    lines = f.readlines()
    
for l in lines:
    l_arr = l.split()
    i = l.find("GO:")
    if len(l_arr) == 0 or i < 0:
        continue
    
    if l_arr[0] != "mf" and l_arr[0] != "bp" and l_arr[0] != "cc":
        continue
    
    g = l[i:i + 10]
    term = l_arr[0] + "_" + g
    terms_initial.append(term)


with open("../pfp_tools/set_pannzer/tlr4_iso3.txt", "r") as f:
    lines = f.readlines()
    
for l in lines:
    l_arr = l.split()
    i = l.find("GO:")
    if len(l_arr) == 0 or i < 0:
        continue
    
    if l_arr[0] != "mf" and l_arr[0] != "bp" and l_arr[0] != "cc":
        continue
    
    g = l[i:i + 10]
    term = l_arr[0] + "_" + g
    terms_followup.append(term)
    
for t in terms_initial:
    if not t in terms_followup:
        print "Deleted: " + t
        
for t in terms_followup:
    if not t in terms_initial:
        print "Added: " + t