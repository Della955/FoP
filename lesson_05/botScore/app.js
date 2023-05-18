localStorage.setItem('count', 1)

let currentNum = localStorage.getItem('count')
//const getStr = localStorage.getItem('count')
document.querySelector('#add').addEventListener('click', addOne)
document.querySelector('#subtract').addEventListener('click', minusOne)

function addOne(){
    currentNum++
   localStorage.setItem('count', currentNum)
   document.querySelector('h4').innerText = currentNum
}

function minusOne(){
    currentNum = currentNum - 1
    localStorage.setItem('count', currentNum)
    document.querySelector('h4').innerText = currentNum
}

//document.querySelector('h4').innerHTML = getStr
//console.log(getStr)