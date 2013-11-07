#!/bin/sh


for blog in `ls blogs/`
do
	python parse.py blogs/$blog
done
