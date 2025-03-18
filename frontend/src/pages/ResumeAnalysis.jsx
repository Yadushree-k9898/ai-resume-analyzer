import { useState } from "react";
import axios from "axios";
import { toast } from "sonner"; // Replaced use-toast with Sonner
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

const ResumeAnalyzer = () => {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [score, setScore] = useState(null);
  const [suggestions, setSuggestions] = useState([]);

  // Handle file selection
  const handleFileChange = (event) => {
    const selectedFile = event.target.files?.[0];
    if (!selectedFile) return;

    const allowedTypes = [
      "application/pdf",
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ];
    if (!allowedTypes.includes(selectedFile.type)) {
      toast.error("Invalid file type. Only PDF and DOCX files are allowed.");
      return;
    }

    setFile(selectedFile);
  };

  // Handle resume upload
  const handleUpload = async () => {
    if (!file) {
      toast.error("Please upload a resume first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    setLoading(true);

    try {
      const { data } = await axios.post(
        "http://localhost:8000/resumes/upload",
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      );

      console.log("Upload successful:", data);
      toast.success("Resume uploaded successfully!");
      await handleAnalyze(); // Automatically analyze after upload
    } catch (error) {
      toast.error("Error uploading resume. Please try again.");
      console.error("Upload Error:", error);
    } finally {
      setLoading(false);
    }
  };

  // Handle resume analysis
  const handleAnalyze = async () => {
    if (!file) {
      toast.error("Please upload a resume first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    setLoading(true);

    try {
      const { data } = await axios.post(
        "http://localhost:8000/scoring/analyze",
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      );

      setScore(data.resume_score);
      setSuggestions(data.suggestions || []);
      toast.success("Resume analyzed successfully!");
    } catch (error) {
      toast.error("Error analyzing resume. Please try again.");
      console.error("Analysis Error:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center space-y-4 p-6 border rounded-lg shadow-md max-w-lg mx-auto">
      <h2 className="text-xl font-bold">AI Resume Analyzer</h2>
      <Input type="file" accept=".pdf,.docx" onChange={handleFileChange} />
      <div className="flex space-x-2">
        <Button onClick={handleUpload} disabled={loading}>
          {loading ? "Uploading..." : "Upload Resume"}
        </Button>
        <Button onClick={handleAnalyze} disabled={loading}>
          {loading ? "Analyzing..." : "Analyze Resume"}
        </Button>
      </div>

      {score !== null && (
        <Card className="w-full max-w-lg mt-4">
          <CardHeader>
            <CardTitle>Resume Score: {score}/100</CardTitle>
          </CardHeader>
          <CardContent>
            <ul className="list-disc list-inside space-y-1">
              {suggestions.length > 0 ? (
                suggestions.map((suggestion, index) => <li key={index}>{suggestion}</li>)
              ) : (
                <li>No suggestions available.</li>
              )}
            </ul>
          </CardContent>
        </Card>
      )}
    </div>
  );
};

export default ResumeAnalyzer;