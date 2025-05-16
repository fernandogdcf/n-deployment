#!/bin/bash

ini=21
var=30
tau=30

executa() {
    for (( i=0; i<var; i++ ))
    do
        exp=$((ini + i))
        command_to_run="./nsga2 1 $tau $exp >> output$exp.log"
        nohup sh -c "$command_to_run" &
        echo "$command_to_run"
    done
    ini=$((ini + var))
}

tau=30
executa
tau=60
executa
tau=120
executa

echo "Commands started in the background."