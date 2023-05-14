document.querySelector('#check').addEventListener('click', checkDay)

function checkDay() {
  
  const day = document.querySelector('#day').value

  // logic goes here
  day = day.toLowerCase(); 

  if (day === "monday" || day === "tuesday"){
    document.write(id = "placeToSee" + "hello world"); 
  }

}

document.querySelector("#placeToSee").innerHTML = "weekend"