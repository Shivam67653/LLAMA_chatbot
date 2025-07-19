async function sendMessage() {
  const inputField = document.getElementById("user-input");
  const message = inputField.value;
  inputField.value = "";

  appendMessage("You", message);

  const response = await fetch("http://localhost:5000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  });

  const data = await response.json();
  appendMessage("Bot", data.response || data.error);
}

function appendMessage(sender, text) {
  const chatLog = document.getElementById("chat-log");
  const msg = document.createElement("div");
  // Assign class based on sender
  if (sender === "You") {
    msg.className = "chat-message user";
  } else {
    msg.className = "chat-message bot";
  }
  msg.textContent = text;
  chatLog.appendChild(msg);
  chatLog.scrollTop = chatLog.scrollHeight;
}
