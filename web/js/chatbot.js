
  const chatButton = document.getElementById("chatButton");
  const generateButton = document.getElementById("generateButton");
  const promptInput = document.getElementById("promptInput");
  const output = document.getElementById("output");

  chatButton.addEventListener("click", () => {
    const prompt = promptInput.value.trim();
    if (prompt === "") return;
    displayUserInput(prompt);
    setTimeout(() => {
      displayBotTyping();
      setTimeout(() => {
        const response = getChatbotResponse(prompt);
        displayBotResponse(response);
      }, 1300); // Adjusted to 1.3 seconds
    }, 500); // Slight delay before typing starts
  });

  generateButton.addEventListener("click", () => {
    const prompt = promptInput.value.trim();
    if (prompt === "") return;
    displayUserInput(prompt);
    setTimeout(() => {
      displayBotTyping();
      setTimeout(() => {
        const response = generateText(prompt);
        displayBotResponse(response);
      }, 1300); // Adjusted to 1.3 seconds
    }, 500); // Slight delay before typing starts
  });

  

  function displayUserInput(prompt) {
    const userInput = `
      <p class="user-message"><strong>You:</strong> ${prompt}</p>
    `;
    output.innerHTML += userInput;
    promptInput.value = "";
  }

  function displayBotTyping() {
    const botTyping = `
      <p class="bot-message bot-typing"><strong>Chatbot:</strong> Typing...</p>
    `;
    output.innerHTML += botTyping;
    output.scrollTop = output.scrollHeight; // Scroll to bottom
  }

  function displayBotResponse(response) {
    const botResponse = `
      <p class="bot-message"><strong>Chatbot:</strong> ${response}</p>
    `;
    output.innerHTML = output.innerHTML.replace('<p class="bot-message bot-typing"><strong>Chatbot:</strong> Typing...</p>', botResponse);
    output.scrollTop = output.scrollHeight; // Scroll to bottom
  }

  function getChatbotResponse(prompt) {
    // Define predefined conversations and responses
    const conversations = {
      "hello": "Hi there! How can I assist you?",
      "how are you": "I'm just a chatbot, but I'm here to help!",
      "tell me a joke": "Sure! Why did the chicken go to the seance? To talk to the other side!"
      // You can add more conversations here
    };

    return conversations[prompt.toLowerCase()] || "I'm sorry, I don't understand that.";
  }

  function generateText(prompt) {
    // Replace with your predefined text generation logic based on the prompt
    // Example:
    return "Based on your prompt, here's some generated text.";
  }
