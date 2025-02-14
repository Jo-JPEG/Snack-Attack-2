document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById("game-board");
    const ctx = canvas.getContext("2d");
    const startStopButton = document.getElementById("start-stop-button");
    const scoreElement = document.getElementById("score");
    const highScoreElement = document.getElementById("high-score");
    const timerElement = document.getElementById("timer");

    // Set canvas dimensions dynamically
    const boxSize = 20; // Grid cell size
    const rows = 20;
    const cols = 20;
    canvas.width = cols * boxSize;
    canvas.height = rows * boxSize;

    let snake = [{ x: 5 * boxSize, y: 5 * boxSize }];
    let food = generateFood();
    let direction = "RIGHT";
    let score = 0;
    let highScore = localStorage.getItem("highScore") || 0;
    let speed = 200; // Initial speed (lower is faster)
    let gameInterval;
    let timer = 60;
    let isRunning = false;

    highScoreElement.innerText = highScore;

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw Snake
        snake.forEach((segment, index) => {
            ctx.fillStyle = index === 0 ? "#00FF00" : "#32CD32"; // Head is a different shade
            ctx.fillRect(segment.x, segment.y, boxSize, boxSize);

            // Create snake mouth (a simple open mouth effect)
            if (index === 0) {
                ctx.fillStyle = "black";
                if (direction === "RIGHT") {
                    ctx.fillRect(segment.x + boxSize - 5, segment.y + 5, 5, 10);
                } else if (direction === "LEFT") {
                    ctx.fillRect(segment.x, segment.y + 5, 5, 10);
                } else if (direction === "UP") {
                    ctx.fillRect(segment.x + 5, segment.y, 10, 5);
                } else if (direction === "DOWN") {
                    ctx.fillRect(segment.x + 5, segment.y + boxSize - 5, 10, 5);
                }
            }
        });

        // Draw Food
        ctx.fillStyle = "red";
        ctx.fillRect(food.x, food.y, boxSize, boxSize);

        moveSnake();
        checkCollision();
    }

    function moveSnake() {
        let head = { ...snake[0] };

        switch (direction) {
            case "UP":
                head.y -= boxSize;
                break;
            case "DOWN":
                head.y += boxSize;
                break;
            case "LEFT":
                head.x -= boxSize;
                break;
            case "RIGHT":
                head.x += boxSize;
                break;
        }

        snake.unshift(head);

        if (head.x === food.x && head.y === food.y) {
            score += 10;
            scoreElement.innerText = score;
            food = generateFood();
            speed = Math.max(50, speed - 5); // Speed up the game slightly
            clearInterval(gameInterval);
            gameInterval = setInterval(draw, speed);
        } else {
            snake.pop(); // Remove last tail segment
        }
    }

    function generateFood() {
        return {
            x: Math.floor(Math.random() * cols) * boxSize,
            y: Math.floor(Math.random() * rows) * boxSize
        };
    }

    function checkCollision() {
        let head = snake[0];

        // Wall Collision
        if (head.x < 0 || head.x >= canvas.width || head.y < 0 || head.y >= canvas.height) {
            gameOver();
        }

        // Self Collision
        for (let i = 1; i < snake.length; i++) {
            if (head.x === snake[i].x && head.y === snake[i].y) {
                gameOver();
            }
        }
    }

    function gameOver() {
        clearInterval(gameInterval);
        isRunning = false;
        startStopButton.innerText = "Start";

        alert("Game Over! Your score: " + score);

        if (score > highScore) {
            highScore = score;
            localStorage.setItem("highScore", highScore);
            highScoreElement.innerText = highScore;
        }

        resetGame();
    }

    function resetGame() {
        snake = [{ x: 5 * boxSize, y: 5 * boxSize }];
        direction = "RIGHT";
        score = 0;
        timer = 60;
        speed = 200;
        scoreElement.innerText = score;
        timerElement.innerText = timer;
    }

    function toggleGame() {
        if (isRunning) {
            clearInterval(gameInterval);
            isRunning = false;
            startStopButton.innerText = "Start";
        } else {
            gameInterval = setInterval(draw, speed);
            isRunning = true;
            startStopButton.innerText = "Stop";
            startTimer();
        }
    }

    function startTimer() {
        let countdown = setInterval(() => {
            if (!isRunning) {
                clearInterval(countdown);
                return;
            }

            timer--;
            timerElement.innerText = timer;

            if (timer <= 0) {
                clearInterval(countdown);
                gameOver();
            }
        }, 1000);
    }

    document.addEventListener("keydown", (event) => {
        if (event.key === "ArrowUp" && direction !== "DOWN") direction = "UP";
        else if (event.key === "ArrowDown" && direction !== "UP") direction = "DOWN";
        else if (event.key === "ArrowLeft" && direction !== "RIGHT") direction = "LEFT";
        else if (event.key === "ArrowRight" && direction !== "LEFT") direction = "RIGHT";
    });

    // Mobile Controls
    document.getElementById("up").addEventListener("click", () => { if (direction !== "DOWN") direction = "UP"; });
    document.getElementById("down").addEventListener("click", () => { if (direction !== "UP") direction = "DOWN"; });
    document.getElementById("left").addEventListener("click", () => { if (direction !== "RIGHT") direction = "LEFT"; });
    document.getElementById("right").addEventListener("click", () => { if (direction !== "LEFT") direction = "RIGHT"; });

    startStopButton.addEventListener("click", toggleGame);
});
