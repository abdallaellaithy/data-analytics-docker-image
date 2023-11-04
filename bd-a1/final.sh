#!/bin/bash

mkdir -p bd-a1/service-result/

# Copy the output files 
docker cp fd8be78ee485ab6001b14f274febc8e5df5da82f4612cf22f0a38ce77a51a4c9:/home/doc-bd-a1/res_dpre.csv bd-a1/service-result/
docker cp fd8be78ee485ab6001b14f274febc8e5df5da82f4612cf22f0a38ce77a51a4c9:/home/doc-bd-a1/eda-in-1.txt bd-a1/service-result/
docker cp fd8be78ee485ab6001b14f274febc8e5df5da82f4612cf22f0a38ce77a51a4c9:/home/doc-bd-a1/vis.png bd-a1/service-result/
docker cp fd8be78ee485ab6001b14f274febc8e5df5da82f4612cf22f0a38ce77a51a4c9:/home/doc-bd-a1/k.txt bd-a1/service-result/

docker stop fd8be78ee485ab6001b14f274febc8e5df5da82f4612cf22f0a38ce77a51a4c9
