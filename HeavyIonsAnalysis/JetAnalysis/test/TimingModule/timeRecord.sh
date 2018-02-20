#!/bin/sh


InFile=$1
OutFile=$2

echo "InFile = $InFile"
echo "OutFile = $OutFile"

#cat PbPbstep3.txt | grep "Total job" | awk '{print $4}' >CPUratio.txt
cat $InFile | grep "Total job" | awk '{print $4}' >CPUratio.txt

#grep TimeModule\> PbPbstep3.txt > TimingInfo.txt
grep TimeModule\> $InFile > TimingInfo.txt

g++ timing.cpp -o timing.out

#./timing.out >TimingModule.txt
./timing.out >$OutFile

