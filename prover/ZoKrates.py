import os

def witness(R, A, S, secret, bid1, bid2, bid3):
    os.system("zokrates compute-witness -a " + R[0] + " " + R[1] + " " + R[2] + " " + R[3] + " " + R[4] + " " + R[5] + " "  + A[0] + " "  + A[1] + " "  + A[2] + " "  + A[3] + " "  + A[4] + " "  + A[5] + " " + S[0] + " " + S[1] + " " + S[2] + " " + secret + " " + bid1 + " " + bid2 + " " + bid3)
    return

def proof():
    os.system("nohup zokrates generate-proof >/dev/null 2>&1")
    badProof = os.popen("zokrates print-proof --format remix --proofpath proof.json").read()
    goodProof = "[" + badProof[badProof.find("[")+1:len(badProof)-65] 
    return goodProof
