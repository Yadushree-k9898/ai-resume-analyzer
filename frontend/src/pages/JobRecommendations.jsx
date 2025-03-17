import { useState } from "react";
import { Button } from "@/components/ui/button";
import { toast } from "sonner";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

const JobRecommendations = () => {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchJobs = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://localhost:8000/recommend-jobs");
      const data = await response.json();

      if (!response.ok || !data.jobs) throw new Error(data.detail || "Failed to fetch job recommendations");

      setJobs(data.jobs);
      toast.success("Here are your recommended jobs based on your resume!");
    } catch (error) {
      toast.error(error.message || "Something went wrong while fetching jobs.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center space-y-4 p-6 border rounded-lg shadow-md">
      <h2 className="text-lg font-semibold">Job Recommendations</h2>
      <Button onClick={fetchJobs} disabled={loading}>
        {loading ? "Fetching Jobs..." : "Get Job Recommendations"}
      </Button>

      {loading && <p>Loading job recommendations...</p>}

      {jobs.length > 0 ? (
        <div className="w-full max-w-lg mt-4 space-y-3">
          {jobs.map((job, index) => (
            <Card key={index} className="w-full">
              <CardHeader>
                <CardTitle>{job.title}</CardTitle>
              </CardHeader>
              <CardContent>
                <p><strong>Company:</strong> {job.company}</p>
                <p><strong>Location:</strong> {job.location}</p>
                <p><strong>Required Skills:</strong> {job.skills.join(", ")}</p>
                <a href={job.link} target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline">
                  View Job
                </a>
              </CardContent>
            </Card>
          ))}
        </div>
      ) : (
        !loading && <p>No job recommendations available. Try again later.</p>
      )}
    </div>
  );
};

export default JobRecommendations;
