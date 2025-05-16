let counter = 0;
let score = 0;

const questionElement = document.getElementById("question");
const ans1Element = document.getElementById("ans1");
const ans2Element = document.getElementById("ans2");
const ans3Element = document.getElementById("ans3");
const ans4Element = document.getElementById("ans4");
const scoreElement = document.getElementById("scoretext");
const nextButton = document.getElementById("next");
const correctElement = document.getElementById("correct");
const wrongElement = document.getElementById("wrong");
const explanationElement = document.getElementById("explanation");

function displayQuestion() {
  const question = questions[counter];
  const answers = question.answer;

  questionElement.innerHTML = question.question;
  ans1Element.src = answers[0].pic || "";
  ans2Element.src = answers[1].pic || "";
  ans3Element.src = answers[2].pic || "";
  ans4Element.src = answers[3].pic || "";
  ans1Element.alt = answers[0].id || "";
  ans2Element.alt = answers[1].id || "";
  ans3Element.alt = answers[2].id || "";
  ans4Element.alt = answers[3].id || "";
  ans1Element.title = answers[0].id || "";
  ans2Element.title = answers[1].id || "";
  ans3Element.title = answers[2].id || "";
  ans4Element.title = answers[3].id || "";

  correctElement.style.display = "none";
  wrongElement.style.display = "none";
  explanationElement.style.display = "none";
}

function checkAnswer(event) {
  const selectedAnswer = event.target.alt;
  const question = questions[counter];
  const answers = question.answer;
  const correctAnswer = answers.find((answer) => answer.correct).id;

  if (selectedAnswer === correctAnswer) {
    score++;
    correctElement.style.display = "block";
    wrongElement.style.display = "none";
  } else {
    correctElement.style.display = "none";
    wrongElement.style.display = "block";
  }

  explanationElement.innerHTML = question.explain;
  explanationElement.style.display = "block";
  scoreElement.innerHTML = `Score : ${score}`;
}

function nextQuestion() {
  counter = (counter + 1) % questions.length;
  displayQuestion();
}

ans1Element.addEventListener("click", checkAnswer);
ans2Element.addEventListener("click", checkAnswer);
ans3Element.addEventListener("click", checkAnswer);
ans4Element.addEventListener("click", checkAnswer);
nextButton.addEventListener("click", nextQuestion);

displayQuestion();
