#!/bin/bash


~/gitstats/gitstats/./gitstats ~/networklab1 ~/weekly_report
tar -zcvf RoR-Report.tar.gz ~/weekly_report

mutt -s "Weekly Stat Report" jub205@nyu.edu, nm1345@nyu.edu -a /home/jinu/RoR-Report.tar.gz < /dev/null



