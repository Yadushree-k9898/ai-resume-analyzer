import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { ExclamationTriangleIcon } from "@radix-ui/react-icons";

const Dashboard = () => {
  const API_URL = import.meta.env.VITE_API_URL;
  const [dashboard, setDashboard] = useState(null);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchDashboard = async () => {
      const token = localStorage.getItem("token");
      if (!token) {
        setError("You need to be logged in to access the dashboard.");
        setIsLoading(false);
        return;
      }

      try {
        const response = await fetch(`${API_URL}/dashboard`, {
          method: "GET",
          headers: {
            "Authorization": `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        });

        const data = await response.json();
        if (!response.ok) throw new Error(data.detail || "Failed to fetch dashboard data");

        if (data.dashboard) {
          setDashboard(data.dashboard);
        } else {
          setError("No dashboard data available. Please upload a resume or apply for a job.");
        }
      } catch (err) {
        setError(err.message || "Failed to fetch dashboard data");
      } finally {
        setIsLoading(false);
      }
    };

    fetchDashboard();
  }, [API_URL]);

  const handleUpdate = async () => {
    setIsLoading(true);
    try {
      const token = localStorage.getItem("token");
      const response = await fetch(`${API_URL}/dashboard/update`, {
        method: "PUT",
        headers: {
          "Authorization": `Bearer ${token}`,
          "Content-Type": "application/json",
        },
      });

      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || "Failed to update dashboard");

      setDashboard(data.dashboard); // Update the state with the new data
    } catch (err) {
      setError(err.message || "Failed to update dashboard");
    } finally {
      setIsLoading(false);
    }
  };

  const handleDelete = async () => {
    setIsLoading(true);
    try {
      const token = localStorage.getItem("token");
      const response = await fetch(`${API_URL}/dashboard`, {
        method: "DELETE",
        headers: {
          "Authorization": `Bearer ${token}`,
          "Content-Type": "application/json",
        },
      });

      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || "Failed to delete dashboard");

      setDashboard(null); // Clear the dashboard from the state
    } catch (err) {
      setError(err.message || "Failed to delete dashboard");
    } finally {
      setIsLoading(false);
    }
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="flex justify-center items-center min-h-screen bg-background p-4">
      <Card className="w-full max-w-md shadow-lg border-border">
        <CardHeader className="space-y-1">
          <CardTitle className="text-2xl font-bold text-center">Dashboard</CardTitle>
          <CardDescription className="text-center">Your personal dashboard overview</CardDescription>
        </CardHeader>
        <CardContent>
          {error && (
            <Alert variant="destructive" className="border-destructive/50 text-destructive dark:border-destructive dark:text-destructive">
              <ExclamationTriangleIcon className="h-4 w-4" />
              <AlertDescription>{error}</AlertDescription>
            </Alert>
          )}

          {dashboard ? (
            <div className="space-y-4">
              <p><strong>Total Resumes:</strong> {dashboard.total_resumes}</p>
              <p><strong>Latest Resume ID:</strong> {dashboard.latest_resume_id}</p>
              <p><strong>Best Resume ID:</strong> {dashboard.best_resume_id}</p>
              <p><strong>Resume Score:</strong> {dashboard.resume_score}</p>
              <p><strong>Average Resume Score:</strong> {dashboard.average_resume_score}</p>
              <p><strong>Total Jobs Applied:</strong> {dashboard.total_jobs_applied}</p>
              <p><strong>Job Application Status:</strong> {JSON.stringify(dashboard.job_application_status)}</p>
              <p><strong>Job Matches:</strong> {JSON.stringify(dashboard.job_matches)}</p>
              <p><strong>Missing Skills:</strong> {JSON.stringify(dashboard.missing_skills)}</p>
              <p><strong>Skills Analysis:</strong> {JSON.stringify(dashboard.skills_analysis)}</p>
              <p><strong>Last Updated:</strong> {dashboard.last_updated}</p>

              <Button onClick={handleUpdate} className="w-full">Update Dashboard</Button>
              <Button onClick={handleDelete} className="w-full mt-2" variant="destructive">Delete Dashboard</Button>
            </div>
          ) : (
            <div>No dashboard data available. Please upload a resume or apply for a job.</div>
          )}
        </CardContent>
      </Card>
    </div>
  );
};

export default Dashboard;
