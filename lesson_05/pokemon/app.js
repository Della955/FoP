document.querySelector('button').addEventListener('click', getFetch)




async function getFetch() {
    
    const choice = document.querySelector('input').value.toLowerCase()  
    const url = 'https://pokeapi.co/api/v2/pokemon/'+choice

    
    let data = await fetch(url)
    let pokemonInfo = await data.json()

    console.log(pokemonInfo)
   
    document.querySelector('h2').innerHTML = choice
    document.querySelector('img').src = pokemonInfo.sprites.front_default
    document.querySelector('h3').innerHTML = pokemonInfo.types[0].type.name
    

    var checkbox = document.querySelector("input[name=checkbox]")
    checkbox.addEventListener('change', function(){
        if (this.checked) {
          document.querySelector('img').src = pokemonInfo.sprites.front_shiny
       }
        else if (!this.checked){
            document.querySelector('img').src = pokemonInfo.sprites.front_default
        }
    }); 
 
 
    }


        

