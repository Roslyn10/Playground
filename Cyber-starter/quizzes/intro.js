function submitQuiz() {
    const answers = ["A", "A", "A,B,C,D", "A", "A"];
    let score = 0;
    let index = 0;

    // Go through each question and check answers
    for (const question of document.querySelectorAll('.question')) {
        const selectedOption = question.querySelector('input[type="radio"]:checked');
        if (selectedOption && selectedOption.value === answers[index]) {
            score++;
        }
        index++;
    }

    // Display the final score
    document.getElementById('score-container').innerText = `Your final score is ${score}/${answers.length}`;
}
