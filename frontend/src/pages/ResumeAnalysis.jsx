import React, { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import axios from "axios";

const ResumeAnalyzer = () => {
  const [file, setFile] = useState(null);
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      setError("Please upload a resume.");
      return;
    }
    setError(null);
    setLoading(true);
    
    const formData = new FormData();
    formData.append("resume", file);

    try {
      const response = await axios.post("http://localhost:8000/resumes/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setAnalysis(response.data);
    } catch (err) {
      console.error(err);
      setError("Failed to analyze resume. Try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center p-4">
      <Card className="w-full max-w-md p-4">
        <CardContent className="flex flex-col gap-4">
          <h2 className="text-xl font-bold">AI Resume Analyzer</h2>
          <Input type="file" onChange={handleFileChange} />
          <Button onClick={handleUpload} disabled={loading}>
            {loading ? "Analyzing..." : "Upload & Analyze"}
          </Button>
          {error && <p className="text-red-500">{error}</p>}
          {analysis && (
            <div className="mt-4">
              <h3 className="text-lg font-semibold">Analysis Results:</h3>
              <p>Score: {analysis.score}</p>
              <p>Suggestions: {analysis.suggestions.join(", ")}</p>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
};

export default ResumeAnalyzer;
