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

    const emotionLearningButton = document.getElementById('emotionLearningButton');
    const emotionQuizButton = document.getElementById('emotionQuizButton');
    const conversationalAIButton = document.getElementById('conversationalAIButton');
    const joyfulButton = document.getElementById('joyfulButton');
    const powerfulButton = document.getElementById('powerfulButton');
    const peacefulButton = document.getElementById('peacefulButton');
    const scaredButton = document.getElementById('scaredButton');
    const sadButton = document.getElementById('sadButton');
    const madButton = document.getElementById('madButton');

    emotionLearningButton.addEventListener("click", function() {
    window.location.href = "learnEmotions.html";
    });

    emotionQuizButton.addEventListener("click", function() {
        window.location.href = "emotionsQuiz.html";
    });

    conversationalAIButton.addEventListener("click", function() {
        window.location.href = "conversationalAI.html";
    });

    joyfulButton.addEventListener("click", function() {
        window.location.href = "game.html?emotion=joyful";
    });

    powerfulButton.addEventListener("click", function() {
    window.location.href = "game.html";
    });

    peacefulButton.addEventListener("click", function() {
    window.location.href = "game.html";
    });

    scaredButton.addEventListener("click", function() {
    window.location.href = "game.html";
    });

    sadButton.addEventListener("click", function() {
    window.location.href = "game.html";
    });

    madButton.addEventListener("click", function() {
        window.location.href = "game.html?emotion=mad";
    });
});

function checkAnswer(userAnswer) {
    const correctAnswer = "{{correctAnswer}}"; 
    console.log("User Answer:", userAnswer);
    console.log("Correct Answer:", correctAnswer);

    if (userAnswer == correctAnswer) {
        window.location.href = 'goodJob.html'; 
    } else {
        window.location.href = 'tryAgain.html'; 
    }
}


function goBackToGame() {
    window.location.href = "x_joyful.html";
}
function joyful() {
    window.location.href = "x_joyful.html";
}
function mad() {
    window.location.href = "x_mad.html";
}