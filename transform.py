
lines = open('names.txt').read().splitlines()
print('-- This is autogenerated, do not edit')
print('local p = {}')
print('function p.hello(frame)')
table = ""
for name in lines:
    table += "\"" + name.replace("'", '\\\'').replace("\"", "\\\"") + "\","

print(" math.randomseed(mw.site.stats.edits + mw.site.stats.pages + os.time() + math.floor(os.clock() * 1000000000))")
print(" local myTable = { " + table[:-1] + " }")
print(" return myTable[math.random(#myTable)]")
print("end")
print("return p")
