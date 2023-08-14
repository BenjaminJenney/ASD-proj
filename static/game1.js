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
    const emotionQuizButton = document.getElementById("emotionQuizButton");
    const conversationalAIButton = document.getElementById("conversationalAIButton");
    const goToTheGameButton = document.getElementById("goToTheGameButton");
    
  
    emotionGameButton.addEventListener("click", function() {
      window.location.href = "learnEmotions.html";
    });

    emotionQuizButton.addEventListener("click", function() {
        window.location.href = "emotionsQuiz.html";
    });

    conversationalAIButton.addEventListener("click", function() {
        window.location.href = "conversationalAI.html";
    });

    goToTheGameButton.addEventListener("click", function() {
        window.location.href = "game.html";
    });

  });``