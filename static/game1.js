/*function mySadFunction() {
   document.getElementById("demo").innerHTML = "Sorry, you are Sad";
}
// this is a comment when we press a button we will want to update the backend
//how do we know if they are right or wrong?
function myHappyFunction() {
    document.getElementById("demo").innerHTML = "Great, you are Happy";
}

//function randomClickCounter() {
    // Illigitimate click count variable (from DB) will be updated here for each click 
//}
*/
document.addEventListener("DOMContentLoaded", function() {

    const emotionGameButton = document.getElementById("emotionGameButton");
  
    emotionGameButton.addEventListener("click", function() {
      window.location.href = "game1.html";
    });
  });