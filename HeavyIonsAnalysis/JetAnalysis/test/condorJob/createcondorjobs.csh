#!/bin/csh -f
#

set name = $1
set events = $2
set njobs = $3
set n = 1

while ( $n <= $njobs )
    ./job_template_condor.csh ${name} $events $n
    @ n++
end

