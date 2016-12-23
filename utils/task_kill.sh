#! /bin/sh

worker=$1
ps axu|grep $worker|awk '{if($11 != "grep") print $2}'| xargs kill -9
