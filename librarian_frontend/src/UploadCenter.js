import React from 'react';
import axios from 'axios'

function UploadCenter({ uploadedFiles, setUploadedFiles }) {
    const [isLoading, setIsLoading] = React.useState(false);

    const handleUpload = async (event) => {
        setIsLoading(true);
        const response = await axios.post('http://127.0.0.1:5000/clear')
        console.log(response.data);
        const files = event.target.files;
        let fileNames = [];
        for (let i = 0; i < files.length; i++) {
            fileNames.push(files[i].name);

            const formData = new FormData();
            formData.append('file', files[i]);
            await axios.post('http://127.0.0.1:5000/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
        }
        setUploadedFiles(fileNames);
        setIsLoading(false);
    };

    return (
        <div>
     
            <label htmlFor="fileUpload" className="custom-file-upload">
                Choose Library
            </label>
            <input id="fileUpload" type="file" multiple onChange={handleUpload} style={{ display: 'none' }} />            <div>
            {uploadedFiles.length > 0 && (
                <h3>Uploaded files:</h3>
                )}
                
                {isLoading ? <p>Loading...</p> : uploadedFiles.map((file, index) => (
                    <p key={index}>{file}</p>
                ))}
            </div>
        </div>
    );
}

export default UploadCenter;