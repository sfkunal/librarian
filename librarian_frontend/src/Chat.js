import React, { useState } from "react";
import axios from "axios";
import "./Chat.css";

function Chat({ uploadedFiles }) {
  const [inputText, setInputText] = useState("");
  const [responses, setResponses] = useState([]);

  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  const handleSend = async () => {
    const userMessage = inputText;
    const response = await axios.post("http://127.0.0.1:5000/sendquery", {
      text: inputText,
    });
    console.log(response.data);
    setResponses([...responses, { text: userMessage, sender: 'user' }, { text: response.data.response, sender: 'bot' }]);
    setInputText(""); // Clear the input field
  };

  return (
    <div className="ChatUI">
      {uploadedFiles.length > 0 && (
        <>
          <div className="chatContainer">
            {responses.map((response, index) => (
              <p key={index} className={response.sender}>{response.text}</p>
            ))}
          </div>
          <div className="inputContainer">
            <input
              type="text"
              placeholder="Type a message..."
              onChange={handleInputChange}
              value={inputText}
            />
            <button disabled={inputText.length < 10} onClick={handleSend}>
              Send
            </button>
          </div>
        </>
      )}
    </div>
  );
}

export default Chat;