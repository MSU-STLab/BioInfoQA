from goatools import obo_parser

obo = obo_parser.GODag("/students/shahri/pppp/codes/data/go-basic.obo")

path = "/students/shahri/bsqa/pfp_tools/set_inga/"

org_file = "tlr4_original"
followup_file = "tlr4_iso3"


    
tools = ["consensus"]
sub_onts = ["F", "P", "C"]

consensus_org_terms_mf = []
consensus_org_terms_bp = []
consensus_org_terms_cc = []

tool_index_o = 10
sub_index_o = 11
go_index_o = 12

diff = 1

tool_index_f = tool_index_o + diff
sub_index_f = sub_index_o + diff
go_index_f = go_index_o + diff

for cur_tool in tools:
    for cur_sub in sub_onts:
        diff_found = False
        org_data = []
        fup_data = []
        
        temp_lines = []
        with open(path + org_file, "r") as f:
            temp_lines = f.readlines()
        for l in temp_lines:
            arr = l.split()
            if len(arr) < go_index_o:
                continue
            if arr[tool_index_o] != cur_tool:
                continue
            if arr[sub_index_o] != cur_sub:
                continue
            if "GO:" in arr[go_index_o]:
                org_data.append(arr[go_index_o])
                
#                if cur_tool == "consensus" and cur_sub == "F":
#                    if arr[go_index] in obo and len(obo[arr[go_index]].children) == 0:
#                        consensus_org_terms_mf.append(arr[go_index])
#                        
#                if cur_tool == "consensus" and cur_sub == "P":
#                    if arr[go_index] in obo and len(obo[arr[go_index]].children) == 0:
#                        consensus_org_terms_bp.append(arr[go_index])
#                        
#                if cur_tool == "consensus" and cur_sub == "C":
#                    if arr[go_index] in obo and len(obo[arr[go_index]].children) == 0:
#                        consensus_org_terms_cc.append(arr[go_index])
        
        temp_lines = []
        with open(path + followup_file, "r") as f:
            temp_lines = f.readlines()
                
        for l in temp_lines:
            arr = l.split()
            if len(arr) < go_index_f:
                continue
            if arr[tool_index_f] != cur_tool:
                continue
            if arr[sub_index_f] != cur_sub:
                continue
            if "GO:" in arr[go_index_f]:
                fup_data.append(arr[go_index_f])
                
        
        for i in org_data:
            if not i in fup_data:
                diff_found = True
#                print "Deleted: " + i
        for i in fup_data:
            if not i in org_data:
                diff_found = True
#                print "Added: " + i
        if diff_found:
            print cur_tool + ", " + cur_sub + ": Passed"
            print len(org_data) - len(fup_data)
        else:
            print cur_tool + ", " + cur_sub + ": Failed"
            
            
#for t in consensus_org_terms_cc:
#    print t + "\t" + obo[t].name + "\\\\"