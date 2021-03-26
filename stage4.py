# Whenever a module is imported it is FULLY EXECUTED and then added to your current namespace.
# Even special forms of import statement such as from module import something don't affect that fact.
# To solve this issue, use the __main__ pattern.

# The name of the module is always available in the built-in variable __name__.
# When you are executing a script __name__ has a value "__main__".
# So here we check the value of __name__ and print the line only if the module is executed as a script.

# Packages are a collection of modules.
# The module name "sun.moon" designates a submodule named "moon" in a package named "sun".

xrub = 2.98
xars = 0.82
xhnl = 0.17
xaud = 1.9622
xmad = 0.208
conicount = float(input())

# CALCS
rub = round(conicount * xrub, 2)
ars = round(conicount * xars, 2)
hnl = round(conicount * xhnl, 2)
aud = round(conicount * xaud, 2)
mad = round(conicount * xmad, 2)

print(f"""
I will get {rub} RUB from the sale of {conicount} conicoins.
I will get {ars} ARS from the sale of {conicount} conicoins.
I will get {hnl} HNL from the sale of {conicount} conicoins.
I will get {aud} AUD from the sale of {conicount} conicoins.
I will get {mad} MAD from the sale of {conicount} conicoins.""")