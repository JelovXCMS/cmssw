#!/bin/csh 
set name = $1
set nsubmit = $2
set n = 1
 


while ( $n <= $nsubmit )
    condor_submit condor_${name}_${n}.job
    @ n++
end


