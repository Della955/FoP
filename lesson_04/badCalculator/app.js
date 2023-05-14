let total = 0
let stringNum = ""


document.querySelector('#clear').addEventListener('click', clearInput)

document.querySelector('#one').addEventListener('click', addOne)

document.querySelector('#plus').addEventListener('click', add)
document.querySelector('#equals').addEventListener('click', equals)

function add(){
  stringNum += "+"
  document.querySelector('#placeToPutResult').innerText = stringNum
}

function clearInput() {
  arrayNum = []
  document.querySelector('#placeToPutResult').innerText = total
}

function addOne() {
  stringNum += "1"
  document.querySelector("#placeToPutResult").innerText = stringNum
}
function equals() {
  let total = eval(stringNum)
  document.querySelector("#placeToPutResult").innerText = `Total: ${total}:`
}




