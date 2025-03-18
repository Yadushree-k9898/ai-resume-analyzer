import React, { useState } from "react";
import axios from "axios";

const ResumeAnalyzer = () => {
    const [file, setFile] = useState(null);
    const [result, setResult] = useState(null);

    const handleFileChange = (event) => {
        setFile(event.target.files[0]); // Store selected file
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        if (!file) {
            alert("Please select a file first!");
            return;
        }

        const formData = new FormData();
        formData.append("file", file); // Ensure key name is "file"

        try {
            const response = await axios.post("http://127.0.0.1:8000/scoring/analyze", formData, {
                headers: { "Content-Type": "multipart/form-data" },
            });

            console.log("Response:", response.data);
            setResult(response.data); // Show extracted results
        } catch (error) {
            console.error("Error analyzing resume:", error);
            alert("Failed to analyze resume");
        }
    };

    return (
        <div>
            <h2>Upload Resume for Analysis</h2>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleFileChange} />
                <button type="submit">Analyze Resume</button>
            </form>
            {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
        </div>
    );
};

export default ResumeAnalyzer;
