import { useState } from "react";
import { Button } from "@/components/ui/button";
import { toast } from "sonner";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

const JobRecommendations = () => {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [resume, setResume] = useState(null);

  const handleFileChange = (event) => {
    setResume(event.target.files[0]);
  };

  const uploadAndFetchJobs = async () => {
    if (!resume) {
      toast.error("Please upload a resume first.");
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append("resume", resume);

    try {
      const response = await fetch("http://localhost:8000/api/match_jobs/", {
        method: "POST",
        body: formData,
      });
      
      const data = await response.json();
      
      if (!response.ok || !data?.jobs?.length) {
        throw new Error(data.detail || "No job recommendations available.");
      }
      
      setJobs(data.jobs);
      toast.success("Here are your recommended jobs based on your resume!");
    } catch (error) {
      toast.error(error.message || "Something went wrong while fetching jobs.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center space-y-4 p-6 border rounded-lg shadow-md w-full max-w-xl">
      <h2 className="text-lg font-semibold">Job Recommendations</h2>
      <input type="file" accept=".pdf,.docx" onChange={handleFileChange} className="border p-2 rounded-md" />
      <Button onClick={uploadAndFetchJobs} disabled={loading}>
        {loading ? "Fetching Jobs..." : "Get Job Recommendations"}
      </Button>

      {loading && <p className="text-gray-500">Loading job recommendations...</p>}

      {jobs.length > 0 ? (
        <div className="w-full space-y-3">
          {jobs.map((job, index) => (
            <Card key={index} className="w-full">
              <CardHeader>
                <CardTitle>{job.title || "No title available"}</CardTitle>
              </CardHeader>
              <CardContent>
                <p><strong>Company:</strong> {job.company_name || "Not specified"}</p>
                <p><strong>Location:</strong> {job.location || "Not specified"}</p>
                <p><strong>Required Skills:</strong> {job.skills_required?.join(", ") || "Not specified"}</p>
                {job.apply_link ? (
                  <a href={job.apply_link} target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline">
                    View Job
                  </a>
                ) : (
                  <p className="text-red-500">Apply link not available</p>
                )}
              </CardContent>
            </Card>
          ))}
        </div>
      ) : (
        !loading && <p className="text-gray-500">No job recommendations available. Try again later.</p>
      )}
    </div>
  );
};

export default JobRecommendations;