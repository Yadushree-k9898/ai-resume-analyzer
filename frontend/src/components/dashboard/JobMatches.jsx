import {  useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import axios from "axios";

const JobMatches = () => {
  const API_URL = import.meta.env.VITE_API_URL;
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [resumeText, setResumeText] = useState("");
  const [location, setLocation] = useState("");

  const fetchJobs = async () => {
    setLoading(true);
    setError(null);

    try {
      const response = await axios.post(
        `${API_URL}/api/match_jobs/`,
        {
          resume_text: resumeText || "Your extracted resume text here",
          location: location || "New York",
          num_pages: 1,
        },
        {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
            "Content-Type": "application/json",
          },
        }
      );
      setJobs(response.data.jobs || []);
    } catch (err) {
      setError("Failed to load job matches. Please try again.");
      console.error("Error fetching jobs:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-4">Job Matches</h2>

      {/* Input Fields */}
      <div className="mb-4 flex flex-col gap-2">
        <textarea
          className="p-2 border rounded-md w-full"
          rows="3"
          placeholder="Paste your resume text here..."
          value={resumeText}
          onChange={(e) => setResumeText(e.target.value)}
        />
        <input
          type="text"
          className="p-2 border rounded-md w-full"
          placeholder="Preferred location (e.g., New York)"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
        />
        <Button onClick={fetchJobs} disabled={loading}>
          {loading ? "Fetching..." : "Find Jobs"}
        </Button>
      </div>

      {/* Error Message */}
      {error && <p className="text-red-500">{error}</p>}

      {/* Job Listings */}
      {jobs.length === 0 && !loading ? (
        <p>No matching jobs found.</p>
      ) : (
        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          {jobs.map((job) => (
            <Card key={job.id} className="p-4 border rounded-lg shadow-md">
              <CardContent>
                <h3 className="text-lg font-semibold">{job.title}</h3>
                <p className="text-gray-600">{job.company}</p>
                <p className="text-sm text-gray-500">{job.location}</p>
                <p className="mt-2 text-gray-700">{job.description}</p>
                <Button className="mt-4 w-full" onClick={() => window.open(job.link, "_blank")}>
                  Apply Now
                </Button>
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </div>
  );
};

export default JobMatches;
