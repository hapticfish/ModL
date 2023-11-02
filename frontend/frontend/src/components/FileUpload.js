import React, { useState } from 'react';

//TODO make the buttons for file upload floadted right like the heading

const FileUpload = () => {
    const [file, setFile] = useState(null);
    const [message, setMessage] = useState("");

    const onFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const onUpload = async () => {
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('http://localhost:5000/upload', {
                method: 'POST',
                body: formData,
            });

            const data = await response.json();
            if (data.error) {
                setMessage(data.error);
            } else {
                setMessage("File uploaded successfully");
            }
        } catch (error) {
            setMessage("Error uploading file.");
        }
    };

    const onClear = () => {
        setFile(null);
        document.querySelector("input[type='file']").value = '';
    }

    return (
        <div className="file-upload-container">
            <div className="left-side-panel">


            </div>
            <div className="right-side-panel">
                <div className="input-clear-group">
                    <input className="upload-button" type="file" onChange={onFileChange}/>
                    <button className="clear-button" onClick={onClear}>Clear</button>
                </div>
                <div className="upload-button-group">
                    <button onClick={onUpload}>Upload</button>
                </div>
                <div className="message">
                    <p>{message}</p>
                </div>
            </div>


        </div>
    );
}

export default FileUpload;