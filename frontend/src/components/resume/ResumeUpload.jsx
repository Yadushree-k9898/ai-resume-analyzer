import React from "react";
import axios from "axios";

const ResumeUpload = () => {
    const handleFileUpload = async (event) => {
        const file = event.target.files[0];
        if (!file) return;
    
        const formData = new FormData();
        formData.append("file", file);
    
        try {
            const response = await axios.post("http://localhost:8000/resumes/upload", formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            });
    
            console.log("Upload Successful:", response.data);
        } catch (error) {
            console.error("Error uploading file:", error);
        }
    };
    

    return (
        <div>
            <input type="file" onChange={handleFileUpload} />
        </div>
    );
};

export default ResumeUpload;
