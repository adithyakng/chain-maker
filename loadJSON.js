import {State, Attack, AttackDB} from "./makeChain.js";
import fs from 'fs';

function loadAttacks(attackData){
    // For Local Use
    /*
    const jsonData = fs.readFileSync(filename, 'utf8');
    let attackData;
    try {
        attackData = JSON.parse(jsonData);
    } catch (error) {
        console.error(error);
    }*/

    function createAttack(data) {
        return data.map(attack => {
        const { name, initState, endState } = attack;
        return new Attack(name, new State(initState), new State(endState));
        });
    }
    return createAttack(attackData);
}

function loadState(filename){
    const jsonData = fs.readFileSync(filename, 'utf8');

    let state;
    try {
        state = JSON.parse(jsonData);
    } catch (error) {
        console.error(error);
    }

    return new State(state);
}

// Just a logging function
function logAttacks(attakcs){
    attacks.forEach((attack, index) => {
        console.log(`Attack ${index + 1}:`);
        console.log(`Name: ${attack.name}`);
        console.log(`Init State: ${JSON.stringify(attack.initState)}`);
        console.log(`End State: ${JSON.stringify(attack.endState)}`);
        console.log('\n');
    })
}


export {loadAttacks, loadState, logAttacks};