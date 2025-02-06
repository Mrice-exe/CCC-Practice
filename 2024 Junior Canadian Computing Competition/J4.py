typed = input("")
outcome = input("")
typedarr = [typed]
outcomearr = [outcome]

weirdinput = []
weirdinputnum = []
weirdoutput = []
quite = []
silly = []
for x in typed:
    typednum = typed.count(x)
    outcomenum = outcome.count(x)
    if typednum > outcomenum:
        weirdinput.append(x)
        weirdinputnum.append(typednum)
for q in outcome:
        typednumq = typed.count(q)
        outcomenumq = outcome.count(q)
        if outcomenumq > typednumq:
            weirdoutput.append(q)

weirdinputnumint = weirdinputnum[0]
if len(weirdinput) !=  int(weirdinputnumint):
    thecharacter = weirdinput[0]
    quite.extend(weirdinput)
    for p in range(weirdinputnumint):
        quite.remove(thecharacter)
    silly.extend(weirdinput)
    silly.remove(quite[0])
    print(silly[0],weirdoutput[0])
    print(quite[0])
else:
    silly = weirdinput[0]
    quite = "-"
    print(silly,weirdoutput[0])
    print(quite)