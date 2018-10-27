const DIMENSION = 10
let state = [
    ".",".",".",".",".",".",".",".",".",".",
    ".",".",".",".",".",".",".",".",".",".",
    ".",".",".",".",".",".",".",".",".",".",
    ".",".",".",".",".",".",".",".",".",".",
    ".",".",".",".","0",".",".",".",".",".",
    ".",".","0",".","0",".",".",".",".",".",
    ".",".",".","0","0",".",".",".",".",".",
    ".",".",".",".",".",".",".",".",".",".",
    ".",".",".",".",".",".",".",".",".",".",
    ".",".",".",".",".",".",".",".",".","."
]

function getAliveNeighbors(prevState, dimension, position){
    let aliveNeigbors = 0

    if (prevState[position-1] === "0"){
        aliveNeigbors += 1
    }
    if (prevState[position+1] === "0"){
        aliveNeigbors += 1
    }
    if (prevState[position+dimension] === "0"){
        aliveNeigbors += 1
    }
    if (prevState[position+dimension-1] === "0"){
        aliveNeigbors += 1
    }
    if (prevState[position+dimension+1] === "0"){
        aliveNeigbors += 1
    }
    if (prevState[position-dimension] === "0"){
        aliveNeigbors += 1
    }
    if (prevState[position-dimension-1] === "0"){
        aliveNeigbors += 1
    }
    if (prevState[position-dimension+1] === "0"){
        aliveNeigbors += 1
    }

    return aliveNeigbors
}

function getNextIteration(prevState, dimension) {
    let counter = 0
    let newState = []
    for (let cell of prevState){
        let aliveNeighbors = getAliveNeighbors(prevState, dimension, counter)
        let newCell = cell
        counter += 1
        if (cell === "." && aliveNeighbors === 3){
            newCell = "0"
        } else if (cell === "0" && aliveNeighbors === 1) {
            newCell = "."
        } else if (cell === "0" && aliveNeighbors > 3) {
            newCell = "."
        } 
        newState.push(newCell)
    }
    return newState
}

function printState(state, dimension) {
    let counter = 0
    let buffer = ""
    for (let cell of state) {
        buffer += cell
        if (counter % dimension === 0 && counter !== 0) {
            console.log(buffer)
            buffer = ""
        }
        counter += 1
    }

}



printState(state, DIMENSION)
for ( __ of [0,1,2,3,4,5,6,7,8,9]){
    console.log("")
    let i1 = getNextIteration(state, DIMENSION)
    printState(i1, DIMENSION)
    state = i1
}