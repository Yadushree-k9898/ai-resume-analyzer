import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent } from "@/components/ui/card";
import { toast } from "sonner";

export default function ResumeAnalyzer() {
  const API_URL = import.meta.env.VITE_API_URL;
  const [file, setFile] = useState(null);
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const uploadResume = async () => {
    if (!file) {
      toast.error("Please select a resume file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    try {
      console.log("Uploading resume...");

      // Upload Resume
      const uploadRes = await fetch(`${API_URL}/resumes/upload`, {
        method: "POST",
        body: formData,
      });

      if (!uploadRes.ok) {
        throw new Error(`Upload failed: ${uploadRes.statusText}`);
      }

      const uploadData = await uploadRes.json();
      console.log("Upload Response:", uploadData);

      if (!uploadData.extracted_text) {
        throw new Error("Resume text extraction failed");
      }

      // Analyze Resume
      console.log("Sending for analysis...");
      const scoringRes = await fetch(`${API_URL}/scoring/analyze`, {
        method: "POST",
        body: JSON.stringify({ resume_text: uploadData.extracted_text }), // ✅ Fixed
        headers: { "Content-Type": "application/json" },
      });

      if (!scoringRes.ok) {
        throw new Error(`Analysis failed: ${scoringRes.statusText}`);
      }

      const scoringData = await scoringRes.json();
      console.log("Analysis Response:", scoringData);

      setAnalysis(scoringData);
      toast.success("Resume analyzed successfully!");
    } catch (error) {
      console.error("Error:", error);
      toast.error(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6 max-w-2xl mx-auto">
      <h2 className="text-xl font-bold mb-4">AI Resume Analyzer</h2>
      <Input type="file" accept=".pdf,.docx" onChange={handleFileChange} />
      <Button className="mt-4" onClick={uploadResume} disabled={loading}>
        {loading ? "Analyzing..." : "Upload & Analyze"}
      </Button>

      {analysis && (
        <Card className="mt-6">
          <CardContent>
            <h3 className="font-bold">Resume Score: {analysis.score}/100</h3>
            <p className="mt-2">
              <strong>Extracted Skills:</strong> {analysis.skills?.join(", ") || "N/A"}
            </p>
            <h4 className="font-semibold mt-4">Recommended Jobs:</h4>
            <ul className="list-disc list-inside">
              {analysis.jobs?.length > 0 ? (
                analysis.jobs.map((job, index) => (
                  <li key={index}>
                    {job.title} at {job.company}
                  </li>
                ))
              ) : (
                <li>No job recommendations found</li>
              )}
            </ul>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
