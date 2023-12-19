import React, { useState } from 'react';
import './App.css';
import UploadCenter from './UploadCenter';
import Chat from './Chat';

function App() {
  const [uploadedFiles, setUploadedFiles] = useState([]);

  return (
    <div className="App">
      <header className="App-header">
        <UploadCenter uploadedFiles={uploadedFiles} setUploadedFiles={setUploadedFiles} />
      </header>
      <Chat uploadedFiles={uploadedFiles} />      
    </div>
  );
}

export default App;