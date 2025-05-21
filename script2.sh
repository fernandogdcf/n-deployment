#!/bin/bash

ini=130
var=30
tau1=30
tau2=30
tau3=30

executa() {
    for (( i=0; i<var; i++ ))
    do
        exp=$((ini + i))
        command_to_run="./nsga2 $exp $tau1 $tau2 $tau3 >> output$exp.log"
        nohup sh -c "$command_to_run" &
        echo "$command_to_run"
    done
    ini=$((ini + var))
}

tau1=30
tau2=60
tau3=120
executa
tau2=120
tau3=60
executa
tau1=60
tau2=30
tau3=120
executa
tau2=120
tau3=30
executa
tau1=120
tau2=30
tau3=60
executa
tau2=60
tau3=30
executa

echo "Commands started in the background."