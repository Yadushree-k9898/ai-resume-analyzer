"use client"

import { useState, useEffect } from "react"
import {
  FileText,
  RefreshCw,
  Trash2,
  Briefcase,
  Star,
  BarChart3,
  Clock,
  AlertCircle,
  CheckCircle2,
  XCircle,
  HourglassIcon,
  Lightbulb,
  Zap,
  ArrowUpRight,
} from "lucide-react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle, CardDescription, CardFooter } from "@/components/ui/card"
import { Alert, AlertDescription } from "@/components/ui/alert"
import { Progress } from "@/components/ui/progress"
import { Badge } from "@/components/ui/badge"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Skeleton } from "@/components/ui/skeleton"

const Dashboard = () => {
  const API_URL = import.meta.env.VITE_API_URL
  const [dashboard, setDashboard] = useState(null)
  const [error, setError] = useState(null)
  const [isLoading, setIsLoading] = useState(true)
  const [isUpdating, setIsUpdating] = useState(false)

  useEffect(() => {
    const fetchDashboard = async () => {
      const token = localStorage.getItem("token")
      if (!token) {
        setError("You need to be logged in to access the dashboard.")
        setIsLoading(false)
        return
      }

      try {
        const response = await fetch(`${API_URL}/dashboard`, {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        })

        const data = await response.json()
        if (!response.ok) throw new Error(data.detail || "Failed to fetch dashboard data")

        if (data.dashboard) {
          setDashboard(data.dashboard)
        } else {
          setError("No dashboard data available. Please upload a resume or apply for a job.")
        }
      } catch (err) {
        setError(err.message || "Failed to fetch dashboard data")
      } finally {
        setIsLoading(false)
      }
    }

    fetchDashboard()
  }, [API_URL])

  const handleUpdate = async () => {
    setIsUpdating(true)
    try {
      const token = localStorage.getItem("token")
      const response = await fetch(`${API_URL}/dashboard/update`, {
        method: "PUT",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
      })

      const data = await response.json()
      if (!response.ok) throw new Error(data.detail || "Failed to update dashboard")

      setDashboard(data.dashboard) // Update the state with the new data
    } catch (err) {
      setError(err.message || "Failed to update dashboard")
    } finally {
      setIsUpdating(false)
    }
  }

  const handleDelete = async () => {
    setIsLoading(true)
    try {
      const token = localStorage.getItem("token")
      const response = await fetch(`${API_URL}/dashboard`, {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
      })

      const data = await response.json()
      if (!response.ok) throw new Error(data.detail || "Failed to delete dashboard")

      setDashboard(null) // Clear the dashboard from the state
    } catch (err) {
      setError(err.message || "Failed to delete dashboard")
    } finally {
      setIsLoading(false)
    }
  }

  // Format job application status for better display
  const formatJobStatus = (status) => {
    if (!status) return []

    // If it's a string (JSON), parse it
    if (typeof status === "string") {
      try {
        status = JSON.parse(status)
      } catch {
        return []
      }
    }

    // Convert to array of objects with status and count
    return Object.entries(status).map(([key, value]) => ({
      status: key,
      count: value,
    }))
  }

  // Format skills for better display
  const formatSkills = (skills) => {
    if (!skills) return []

    // If it's a string (JSON), parse it
    if (typeof skills === "string") {
      try {
        skills = JSON.parse(skills)
      } catch {
        return []
      }
    }

    // If it's an array, return it
    if (Array.isArray(skills)) {
      return skills
    }

    // If it's an object, convert to array
    return Object.entries(skills).map(([key, value]) => ({
      skill: key,
      value: value,
    }))
  }

  // Get status icon based on status
  const getStatusIcon = (status) => {
    const statusLower = status.toLowerCase()
    if (statusLower.includes("applied") || statusLower.includes("submitted")) {
      return <CheckCircle2 className="h-4 w-4 text-green-500" />
    } else if (statusLower.includes("rejected") || statusLower.includes("declined")) {
      return <XCircle className="h-4 w-4 text-red-500" />
    } else if (statusLower.includes("interview") || statusLower.includes("screening")) {
      return <HourglassIcon className="h-4 w-4 text-amber-500" />
    } else {
      return <AlertCircle className="h-4 w-4 text-blue-500" />
    }
  }

  if (isLoading) {
    return (
      <div className="flex justify-center items-center min-h-screen bg-gradient-to-br from-background to-muted p-4">
        <Card className="w-full max-w-3xl shadow-lg border-border animate-pulse">
          <CardHeader className="space-y-2">
            <Skeleton className="h-8 w-3/4 mx-auto" />
            <Skeleton className="h-4 w-1/2 mx-auto" />
          </CardHeader>
          <CardContent className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <Skeleton className="h-24 rounded-lg" />
              <Skeleton className="h-24 rounded-lg" />
              <Skeleton className="h-24 rounded-lg" />
              <Skeleton className="h-24 rounded-lg" />
            </div>
            <Skeleton className="h-40 rounded-lg" />
          </CardContent>
        </Card>
      </div>
    )
  }

  return (
    <div className="flex justify-center items-center min-h-screen bg-gradient-to-br from-background to-muted p-4">
      <Card className="w-full max-w-3xl shadow-xl border-border overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-primary/10 to-secondary/5 opacity-50 pointer-events-none" />

        <CardHeader className="space-y-1 relative z-10">
          <div className="flex items-center justify-center mb-2">
            <BarChart3 className="h-8 w-8 text-primary mr-2" />
            <CardTitle className="text-3xl font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
              Dashboard
            </CardTitle>
          </div>
          <CardDescription className="text-center text-muted-foreground">
            Your personal career insights and analytics
          </CardDescription>
        </CardHeader>

        <CardContent className="relative z-10">
          {error && (
            <Alert
              variant="destructive"
              className="mb-6 border-destructive/50 text-destructive dark:border-destructive dark:text-destructive"
            >
              <AlertCircle className="h-4 w-4" />
              <AlertDescription>{error}</AlertDescription>
            </Alert>
          )}

          {dashboard ? (
            <Tabs defaultValue="overview" className="w-full">
              <TabsList className="grid grid-cols-3 mb-6">
                <TabsTrigger value="overview">Overview</TabsTrigger>
                <TabsTrigger value="jobs">Job Applications</TabsTrigger>
                <TabsTrigger value="skills">Skills Analysis</TabsTrigger>
              </TabsList>

              <TabsContent value="overview" className="space-y-6">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <Card className="bg-card/50 backdrop-blur-sm border-primary/20 shadow-md hover:shadow-lg transition-shadow">
                    <CardContent className="p-4 flex flex-col items-center">
                      <div className="rounded-full bg-primary/10 p-3 mb-2">
                        <FileText className="h-6 w-6 text-primary" />
                      </div>
                      <h3 className="text-xl font-semibold">Resume Stats</h3>
                      <div className="mt-2 text-center">
                        <p className="text-3xl font-bold text-primary">{dashboard.total_resumes || 0}</p>
                        <p className="text-sm text-muted-foreground">Total Resumes</p>
                      </div>
                    </CardContent>
                  </Card>

                  <Card className="bg-card/50 backdrop-blur-sm border-primary/20 shadow-md hover:shadow-lg transition-shadow">
                    <CardContent className="p-4 flex flex-col items-center">
                      <div className="rounded-full bg-primary/10 p-3 mb-2">
                        <Briefcase className="h-6 w-6 text-primary" />
                      </div>
                      <h3 className="text-xl font-semibold">Job Applications</h3>
                      <div className="mt-2 text-center">
                        <p className="text-3xl font-bold text-primary">{dashboard.total_jobs_applied || 0}</p>
                        <p className="text-sm text-muted-foreground">Total Applications</p>
                      </div>
                    </CardContent>
                  </Card>
                </div>

                <Card className="bg-card/50 backdrop-blur-sm border-primary/20 shadow-md">
                  <CardContent className="p-4">
                    <h3 className="text-xl font-semibold flex items-center mb-4">
                      <Star className="h-5 w-5 text-amber-500 mr-2" />
                      Resume Score
                    </h3>
                    <div className="space-y-4">
                      <div>
                        <div className="flex justify-between mb-1">
                          <span className="text-sm font-medium">Your Score</span>
                          <span className="text-sm font-medium">{dashboard.resume_score || 0}/100</span>
                        </div>
                        <Progress value={dashboard.resume_score || 0} className="h-2" />
                      </div>

                      <div>
                        <div className="flex justify-between mb-1">
                          <span className="text-sm font-medium">Average Score</span>
                          <span className="text-sm font-medium">{dashboard.average_resume_score || 0}/100</span>
                        </div>
                        <Progress value={dashboard.average_resume_score || 0} className="h-2" />
                      </div>

                      {dashboard.latest_resume_id && (
                        <div className="flex items-center justify-between mt-2 text-sm">
                          <span className="text-muted-foreground">Latest Resume:</span>
                          <Badge variant="outline" className="font-mono">
                            {dashboard.latest_resume_id}
                          </Badge>
                        </div>
                      )}

                      {dashboard.best_resume_id && (
                        <div className="flex items-center justify-between mt-2 text-sm">
                          <span className="text-muted-foreground">Best Resume:</span>
                          <Badge
                            variant="outline"
                            className="font-mono bg-amber-500/10 text-amber-500 border-amber-500/20"
                          >
                            {dashboard.best_resume_id}
                          </Badge>
                        </div>
                      )}
                    </div>
                  </CardContent>
                </Card>

                {dashboard.last_updated && (
                  <div className="flex items-center justify-center text-sm text-muted-foreground">
                    <Clock className="h-4 w-4 mr-1" />
                    Last updated: {new Date(dashboard.last_updated).toLocaleString()}
                  </div>
                )}
              </TabsContent>

              <TabsContent value="jobs" className="space-y-6">
                <Card className="bg-card/50 backdrop-blur-sm border-primary/20 shadow-md">
                  <CardContent className="p-4">
                    <h3 className="text-xl font-semibold flex items-center mb-4">
                      <Briefcase className="h-5 w-5 text-primary mr-2" />
                      Application Status
                    </h3>

                    <div className="space-y-3">
                      {formatJobStatus(dashboard.job_application_status).map((item, index) => (
                        <div key={index} className="flex items-center justify-between">
                          <div className="flex items-center">
                            {getStatusIcon(item.status)}
                            <span className="ml-2 capitalize">{item.status}</span>
                          </div>
                          <Badge variant="secondary">{item.count}</Badge>
                        </div>
                      ))}

                      {formatJobStatus(dashboard.job_application_status).length === 0 && (
                        <p className="text-muted-foreground text-center py-2">No application status data available</p>
                      )}
                    </div>
                  </CardContent>
                </Card>

                <Card className="bg-card/50 backdrop-blur-sm border-primary/20 shadow-md">
                  <CardContent className="p-4">
                    <h3 className="text-xl font-semibold flex items-center mb-4">
                      <ArrowUpRight className="h-5 w-5 text-emerald-500 mr-2" />
                      Job Matches
                    </h3>

                    <div className="space-y-3">
                      {formatSkills(dashboard.job_matches).map((item, index) => (
                        <div key={index} className="flex items-center justify-between">
                          <span>{typeof item === "string" ? item : item.skill || item.name}</span>
                          {typeof item !== "string" && item.value && (
                            <Badge
                              variant="outline"
                              className="bg-emerald-500/10 text-emerald-500 border-emerald-500/20"
                            >
                              {typeof item.value === "number" ? `${item.value}%` : item.value}
                            </Badge>
                          )}
                        </div>
                      ))}

                      {formatSkills(dashboard.job_matches).length === 0 && (
                        <p className="text-muted-foreground text-center py-2">No job match data available</p>
                      )}
                    </div>
                  </CardContent>
                </Card>
              </TabsContent>

              <TabsContent value="skills" className="space-y-6">
                <Card className="bg-card/50 backdrop-blur-sm border-primary/20 shadow-md">
                  <CardContent className="p-4">
                    <h3 className="text-xl font-semibold flex items-center mb-4">
                      <Lightbulb className="h-5 w-5 text-amber-500 mr-2" />
                      Skills Analysis
                    </h3>

                    <div className="space-y-3">
                      {formatSkills(dashboard.skills_analysis).map((item, index) => (
                        <div key={index}>
                          <div className="flex justify-between mb-1">
                            <span className="text-sm font-medium">{typeof item === "string" ? item : item.skill}</span>
                            {typeof item !== "string" && item.value && (
                              <span className="text-sm font-medium">
                                {typeof item.value === "number" ? `${item.value}%` : item.value}
                              </span>
                            )}
                          </div>
                          {typeof item !== "string" && typeof item.value === "number" && (
                            <Progress value={item.value} className="h-2" />
                          )}
                        </div>
                      ))}

                      {formatSkills(dashboard.skills_analysis).length === 0 && (
                        <p className="text-muted-foreground text-center py-2">No skills analysis data available</p>
                      )}
                    </div>
                  </CardContent>
                </Card>

                <Card className="bg-card/50 backdrop-blur-sm border-primary/20 shadow-md">
                  <CardContent className="p-4">
                    <h3 className="text-xl font-semibold flex items-center mb-4">
                      <Zap className="h-5 w-5 text-red-500 mr-2" />
                      Missing Skills
                    </h3>

                    <div className="flex flex-wrap gap-2">
                      {formatSkills(dashboard.missing_skills).map((item, index) => (
                        <Badge key={index} variant="outline" className="bg-red-500/10 text-red-500 border-red-500/20">
                          {typeof item === "string" ? item : item.skill}
                        </Badge>
                      ))}

                      {formatSkills(dashboard.missing_skills).length === 0 && (
                        <p className="text-muted-foreground text-center w-full py-2">
                          No missing skills data available
                        </p>
                      )}
                    </div>
                  </CardContent>
                </Card>
              </TabsContent>
            </Tabs>
          ) : (
            <div className="text-center py-8 space-y-4">
              <div className="rounded-full bg-primary/10 p-4 mx-auto w-fit">
                <FileText className="h-8 w-8 text-primary" />
              </div>
              <h3 className="text-xl font-medium">No dashboard data available</h3>
              <p className="text-muted-foreground">Please upload a resume or apply for a job to see your analytics.</p>
            </div>
          )}
        </CardContent>

        {dashboard && (
          <CardFooter className="flex flex-col sm:flex-row gap-3 relative z-10">
            <Button onClick={handleUpdate} className="w-full sm:w-auto flex items-center gap-2" disabled={isUpdating}>
              {isUpdating ? (
                <>
                  <RefreshCw className="h-4 w-4 animate-spin" />
                  Updating...
                </>
              ) : (
                <>
                  <RefreshCw className="h-4 w-4" />
                  Update Dashboard
                </>
              )}
            </Button>
            <Button onClick={handleDelete} variant="destructive" className="w-full sm:w-auto flex items-center gap-2">
              <Trash2 className="h-4 w-4" />
              Delete Dashboard
            </Button>
          </CardFooter>
        )}
      </Card>
    </div>
  )
}

export default Dashboard

