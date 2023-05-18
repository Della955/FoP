let total = 0
let stringNum = ""

document.querySelector('#clear').addEventListener('click', clearInput)
document.querySelector("#plus").addEventListener('click', add)
document.querySelector('#equals').addEventListener('click', equals)
document.querySelector('#minus').addEventListener('click', minus)

document.querySelector('#one').addEventListener('click', addOne)

function add(){
  stringNum += "+"
  document.querySelector('#placeToPutResult').innerText = stringNum
}

function minus(){
  stringNum += "-"
  document.querySelector('#placeToPutResult').innerText = stringNum
}

function multiply(){
  stringNum += "*"
  document.querySelector('#placeToPutResult').innerText = stringNum
}

function clearInput() {
  arrayNum = []
  total = 0
  stringNum = ""; 
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





