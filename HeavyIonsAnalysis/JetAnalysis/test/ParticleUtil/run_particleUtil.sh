#!/bin/sh

for i in {0..50}
do
	cat particleUtil.py | sed 's@skipEvents = cms.untracked.uint32(0)@skipEvents = cms.untracked.uint32('${i}')@g' >test_particleUtil.py
	cmsRun test_particleUtil.py >event$i.txt
done

