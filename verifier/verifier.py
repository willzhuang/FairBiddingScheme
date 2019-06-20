import ZoKrates
import os

ZoKrates.compile("verifybid.code")
ZoKrates.setup()
ZoKrates.verify()

# Simulates publishing into Blockchain or similar
os.system("cp proving.key out.code out ../prover/")
os.system("nc -lvp 9090")

