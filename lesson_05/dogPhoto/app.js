document.querySelector('#check').addEventListener('click', getDog)

function getDog(){
fetch("https://dog.ceo/api/breeds/image/random")
    .then(res => res.json()) // parse response as JSON
    .then(data => {
      console.log(data)
      console.log(data.message)
      document.querySelector('img').src = data.message
      
    })
    .catch(err => {
        console.log(`error ${err}`)
    })
  }


    