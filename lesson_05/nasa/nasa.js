
document.querySelector('button').addEventListener('click', nasaPhoto)
localStorage.setItem('#date', '0000-00-00')

async function nasaPhoto(){
let APIKey = 's91S07HXdgecIg7eKgx1vF98vTB1o0hVxQtIvQHk'

let date = document.querySelector("#date")

let finalDate = "&date=" + date.value
console.log(finalDate)
const websiteUrl = "https://api.nasa.gov/planetary/apod?api_key="

let finalUrl = ("GET", websiteUrl +APIKey + finalDate)
let data = await fetch(finalUrl)
let response = await data.json()

document.querySelector('h2').innerHTML = response.date
document.querySelector('img').src = response.hdurl
document.querySelector('h3').innerHTML= response.title

localStorage.setItem('date', "Date: "+date.value)
localStorage.setItem('img', "Name: "+ response.hdurl)
localStorage.setItem('url', "URL: "+ websiteUrl)

const getDate = localStorage.getItem('date')
const getName = localStorage.getItem('h3')
const getURL = localStorage.getItem('url')

console.log(finalUrl)
console.log(response)
}
