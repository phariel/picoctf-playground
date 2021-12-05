Install RsaCtftool:

```
sudo apt-get install libgmp3-dev libmpc-dev

git clone https://github.com/Ganapati/RsaCtfTool.git temp/rsactftool

cd temp/rsactftool

pip install -r requirements.txt -t .

python RsaCtfTool.py -n 1422450808944701344261903748621562998784243662042303391362692043823716783771691667 -e 65537 --uncipher 843044897663847841476319711639772861390329326681532977209935413827620909782846667

```
