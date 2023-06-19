// Establish a WebSocket connection
var socket = new WebSocket('ws://localhost:8765');

// Connection opened event
socket.onopen = function() {
  console.log('WebSocket connection established.');
};

// Message received event
socket.onmessage = function(event) {
  var message = event.data;
  console.log('Received message: ' + message);
  // Process the received message
};

// Error event
socket.onerror = function(error) {
  console.error('WebSocket error: ' + error);
};

// Connection closed event
socket.onclose = function(event) {
  console.log('WebSocket connection closed with code: ' + event.code);
};

// Function to send a message
function sendMessage(message) {
  socket.send(message);
  console.log('Sent message: ' + message);
}

function send() {
    var messageInput = document.getElementById('messageInput');
    var message = messageInput.value;
    sendMessage(message);
    messageInput.value = '';
  }

