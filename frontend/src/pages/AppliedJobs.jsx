import { useEffect, useState } from "react";
import axios from "axios";
import { Card, CardHeader, CardTitle, CardContent, CardDescription } from "@/components/ui/card";
import { Briefcase } from "lucide-react";

const AppliedJobs = () => {
  const [appliedJobs, setAppliedJobs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchAppliedJobs = async () => {
      try {
        const token = localStorage.getItem("token");
        const response = await axios.get("http://localhost:8000/api/job_applications/applied_jobs/", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setAppliedJobs(response.data.applied_jobs || []);
      } catch (err) {
        setError("Failed to fetch applied jobs", err);
      } finally {
        setLoading(false);
      }
    };

    fetchAppliedJobs();
  }, []);

  if (loading) return <p>Loading applied jobs...</p>;
  if (error) return <p className="text-red-500">{error}</p>;

  return (
    <Card className="bg-white dark:bg-gray-900 shadow-md p-6">
      <CardHeader>
        <CardTitle className="flex items-center">
          <Briefcase className="h-5 w-5 text-blue-500 mr-2" />
          Applied Jobs
        </CardTitle>
        <CardDescription>Track the jobs you have applied for.</CardDescription>
      </CardHeader>
      <CardContent>
        {appliedJobs.length === 0 ? (
          <p>No jobs applied yet.</p>
        ) : (
          <div className="space-y-6">
            {appliedJobs.map((job) => (
              <div key={job.job_id} className="p-4 border rounded-lg bg-gray-100 dark:bg-gray-800">
                <h3 className="text-lg font-semibold">Applied for {job.title} - {job.company}</h3>
                <p className="mt-2 text-gray-600 dark:text-gray-400">I just applied for the {job.title} role at {job.company}. The position is in {job.location}, offering {job.work_mode}.</p>
                {job.roles && job.roles.length > 0 && (
                  <div className="mt-3">
                    {job.roles.map((role, index) => (
                      <div key={index} className="mt-3">
                        <span className="text-blue-500 font-bold">🔹 Role {index + 1}: {role.title}</span>
                        <ul className="mt-1 text-sm text-gray-700 dark:text-gray-300">
                          <li><strong>Experience:</strong> {role.experience}</li>
                          <li><strong>Salary:</strong> {role.salary}</li>
                          <li><strong>Tech Stack:</strong> {role.tech_stack.join(", ")}</li>
                          <li><strong>Clearance:</strong> {role.clearance}</li>
                        </ul>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            ))}
          </div>
        )}
      </CardContent>
    </Card>
  );
};

export default AppliedJobs;