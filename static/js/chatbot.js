// chatbot.js

const responseContainer = document.getElementById("response-container");
const userInput = document.getElementById("user-input");

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function typeResponse(response) {
    let index = 0;

    function type() {
        if (index < response.length) {
            responseContainer.innerHTML += response.charAt(index);
            index++;
            setTimeout(type, 90); // Adjust the typing speed (in milliseconds)
        }
    }

    type();
}

function simulateChatbotResponse(userMessage) {
    // You can implement your chatbot logic here
    // For simplicity, we'll just echo the user's message
    return `HEALTH•E: Nah`;
}

async function sendMessage() {
    const userMessage = userInput.value.trim();
    if (userMessage === "") return;

    // Make an AJAX request to the Flask server
    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ userMessage }),
    });

    const data = await response.json();

    // Access the chatbot response from the server
    const chatbotResponse = data.chatbot_response;

    // Access the chatbot response from the server
    const currentContext = data.current_context;

    // Clear user input
    userInput.value = "";

    console.log(currentContext)

    // Display user message
    responseContainer.innerHTML += `<div class="user-message">${userMessage}</div>`;

    // Simulate delay before chatbot response
    await sleep(1000);

    console.log(currentContext)

    // Simulate chatbot response with typing effect
    // const chatbotResponse = simulateChatbotResponse(userMessage);
    typeResponse(chatbotResponse);

}
