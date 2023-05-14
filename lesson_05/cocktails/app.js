document.querySelector('#check').addEventListener('click', getDrink)

function getDrink(){
fetch('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita')
    .then(res => res.json()) // parse response as JSON
    .then(data => {
      console.log(data.drinks[0].strInstructions)
      document.getElementById('name').innerHTML = data.drinks[0].strDrink
      document.getElementById('instructions').innerHTML = data.drinks[0].strInstructions
     
     // document.querySelector('img').src = data.message
      
    })
    .catch(err => {
        console.log(`error ${err}`)
    })
}

document.querySelector('button').addEventListener('click', getCocktail)

function getCocktail(){
  let userInput = document.querySelector('input').value
  console.log(userInput)
}
