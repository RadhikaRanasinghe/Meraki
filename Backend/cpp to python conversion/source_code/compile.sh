#!/bin/bash

arq="extractFeats.cpp"; shift
nome="${arq/.cpp/}"
g++ -ggdb `pkg-config --cflags opencv` ${arq} -o ${nome} `pkg-config --libs opencv`

arq="extractTemplate.cpp"; shift
nome="${arq/.cpp/}"
g++ -ggdb `pkg-config --cflags opencv` ${arq} -o ${nome} `pkg-config --libs opencv`

arq="extractPen.cpp"; shift
nome="${arq/.cpp/}"
g++ -ggdb `pkg-config --cflags opencv` ${arq} -o ${nome} `pkg-config --libs opencv`