"use client";

import { useState } from "react";
import {
  User,
  Mail,
  Phone,
  MapPin,
  Calendar,
  FileText,
  Briefcase,
  Award,
  Edit,
  Save,
  Trash2,
  Upload,
  Download,
  Settings,
  Shield,
  LogOut,
  Sparkles,
  Star,
  Zap,
  CheckCircle,
  Clock,
} from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
  CardDescription,
  CardFooter,
} from "@/components/ui/card";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Badge } from "@/components/ui/badge";
import { Progress } from "@/components/ui/progress";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Label } from "@/components/ui/label";
import { Switch } from "@/components/ui/switch";
import { useNavigate } from "react-router-dom";
import AppliedJobs from "./AppliedJobs";

const Profile = () => {
  const [isEditing, setIsEditing] = useState(false);
  const navigate = useNavigate();
  const [profileData, setProfileData] = useState({
    name: "Alex Johnson",
    email: "alex.johnson@example.com",
    phone: "+1 (555) 123-4567",
    location: "San Francisco, CA",
    bio: "Senior Software Engineer with 5+ years of experience in full-stack development. Passionate about creating efficient, scalable applications and mentoring junior developers.",
    joinDate: "January 2022",
    resumeScore: 85,
    jobApplications: 12,
    interviews: 4,
    skills: [
      { name: "JavaScript", level: 90 },
      { name: "React", level: 85 },
      { name: "Node.js", level: 80 },
      { name: "TypeScript", level: 75 },
      { name: "Python", level: 65 },
    ],
    education: [
      {
        degree: "M.S. Computer Science",
        institution: "Stanford University",
        year: "2018-2020",
      },
      {
        degree: "B.S. Computer Engineering",
        institution: "UC Berkeley",
        year: "2014-2018",
      },
    ],
    experience: [
      {
        title: "Senior Software Engineer",
        company: "TechCorp Inc.",
        period: "2020-Present",
        description:
          "Lead developer for the company's flagship product. Managed a team of 5 engineers.",
      },
      {
        title: "Software Developer",
        company: "InnovateTech",
        period: "2018-2020",
        description:
          "Developed and maintained web applications using React and Node.js.",
      },
    ],
    certifications: [
      {
        name: "AWS Certified Solutions Architect",
        issuer: "Amazon Web Services",
        date: "2021",
      },
      {
        name: "Professional Scrum Master I",
        issuer: "Scrum.org",
        date: "2020",
      },
    ],
  });

  const handleEdit = () => {
    setIsEditing(true);
  };

  const handleSave = () => {
    setIsEditing(false);
    // Here you would typically save the data to your backend
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setProfileData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  return (
    <div className="flex justify-center items-center min-h-screen relative overflow-hidden">
      {/* Background gradients */}
      <div className="absolute inset-0 bg-gradient-to-b from-white to-indigo-50/50 dark:from-background dark:to-indigo-950/20 pointer-events-none"></div>
      <div className="absolute -top-40 -right-40 w-80 h-80 bg-pink-400/10 dark:bg-pink-600/5 rounded-full blur-3xl"></div>
      <div className="absolute -bottom-40 -left-40 w-80 h-80 bg-blue-400/10 dark:bg-blue-600/5 rounded-full blur-3xl"></div>

      <div className="container mx-auto px-4 py-8 relative z-10">
        <div className="flex flex-col items-center justify-center mb-8">
          <div className="relative mb-2">
            <div className="absolute -inset-1 bg-gradient-to-r from-violet-600 to-indigo-600 rounded-full blur-sm opacity-70"></div>
            <div className="relative bg-white dark:bg-gray-900 rounded-full p-1.5">
              <User className="h-6 w-6 text-transparent bg-gradient-to-br from-violet-500 to-indigo-600 bg-clip-text" />
            </div>
          </div>
          <h1 className="text-3xl font-bold bg-gradient-to-r from-violet-600 via-indigo-600 to-purple-600 bg-clip-text text-transparent">
            Profile
          </h1>
          <p className="text-muted-foreground mt-1">
            Manage your personal information and career details
          </p>
        </div>

        <Tabs defaultValue="overview" className="w-full max-w-4xl mx-auto">
          <TabsList className="grid grid-cols-4 mb-6 bg-indigo-50/50 dark:bg-indigo-950/20">
            <TabsTrigger
              value="overview"
              className="data-[state=active]:bg-gradient-to-r data-[state=active]:from-violet-500/10 data-[state=active]:to-indigo-500/10 data-[state=active]:text-indigo-700 dark:data-[state=active]:text-indigo-300"
            >
              Overview
            </TabsTrigger>
            <TabsTrigger
              value="resume"
              className="data-[state=active]:bg-gradient-to-r data-[state=active]:from-violet-500/10 data-[state=active]:to-indigo-500/10 data-[state=active]:text-indigo-700 dark:data-[state=active]:text-indigo-300"
            >
              Resume
            </TabsTrigger>
            <TabsTrigger
              value="applications"
              className="data-[state=active]:bg-gradient-to-r data-[state=active]:from-violet-500/10 data-[state=active]:to-indigo-500/10 data-[state=active]:text-indigo-700 dark:data-[state=active]:text-indigo-300"
            >
              Applications
            </TabsTrigger>
            <TabsTrigger
              value="settings"
              className="data-[state=active]:bg-gradient-to-r data-[state=active]:from-violet-500/10 data-[state=active]:to-indigo-500/10 data-[state=active]:text-indigo-700 dark:data-[state=active]:text-indigo-300"
            >
              Settings
            </TabsTrigger>
          </TabsList>

          <TabsContent value="overview" className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {/* Profile Card */}
              <Card className="md:col-span-1 bg-white/50 dark:bg-gray-900/50 backdrop-blur-sm border-indigo-100/30 dark:border-indigo-800/30 shadow-md">
                <CardContent className="p-6 flex flex-col items-center">
                  <div className="relative mb-4">
                    <div className="absolute -inset-1 bg-gradient-to-r from-violet-600 to-indigo-600 rounded-full blur-sm opacity-70"></div>
                    <Avatar className="h-24 w-24 border-2 border-white dark:border-gray-800">
                      <AvatarImage
                        src="/placeholder.svg?height=96&width=96"
                        alt={profileData.name}
                      />
                      <AvatarFallback className="bg-gradient-to-br from-violet-500 to-indigo-600 text-white text-xl">
                        {profileData.name
                          .split(" ")
                          .map((n) => n[0])
                          .join("")}
                      </AvatarFallback>
                    </Avatar>
                  </div>

                  <h2 className="text-xl font-bold bg-gradient-to-r from-violet-600 to-indigo-600 bg-clip-text text-transparent mb-1">
                    {profileData.name}
                  </h2>

                  <Badge className="mb-4 bg-indigo-100 text-indigo-700 dark:bg-indigo-900/30 dark:text-indigo-300 border-indigo-200 dark:border-indigo-800">
                    Senior Software Engineer
                  </Badge>

                  <div className="w-full space-y-3 text-sm">
                    <div className="flex items-center">
                      <Mail className="h-4 w-4 text-indigo-500 mr-2" />
                      <span className="text-muted-foreground">
                        {profileData.email}
                      </span>
                    </div>
                    <div className="flex items-center">
                      <Phone className="h-4 w-4 text-indigo-500 mr-2" />
                      <span className="text-muted-foreground">
                        {profileData.phone}
                      </span>
                    </div>
                    <div className="flex items-center">
                      <MapPin className="h-4 w-4 text-indigo-500 mr-2" />
                      <span className="text-muted-foreground">
                        {profileData.location}
                      </span>
                    </div>
                    <div className="flex items-center">
                      <Calendar className="h-4 w-4 text-indigo-500 mr-2" />
                      <span className="text-muted-foreground">
                        Member since {profileData.joinDate}
                      </span>
                    </div>
                  </div>
                </CardContent>
              </Card>

              {/* Bio Card */}
              <Card className="md:col-span-2 bg-white/50 dark:bg-gray-900/50 backdrop-blur-sm border-indigo-100/30 dark:border-indigo-800/30 shadow-md">
                <CardHeader>
                  <CardTitle className="flex items-center">
                    <User className="h-5 w-5 text-indigo-500 mr-2" />
                    <span className="bg-gradient-to-r from-indigo-600 to-blue-600 bg-clip-text text-transparent">
                      About Me
                    </span>
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  {isEditing ? (
                    <Textarea
                      name="bio"
                      value={profileData.bio}
                      onChange={handleInputChange}
                      className="min-h-[120px] bg-white/70 dark:bg-gray-900/70 border-indigo-200 dark:border-indigo-800 focus:border-indigo-400 focus:ring-indigo-400"
                    />
                  ) : (
                    <p className="text-muted-foreground">{profileData.bio}</p>
                  )}
                </CardContent>
                <CardFooter className="flex justify-end gap-2">
                  {isEditing ? (
                    <Button
                      onClick={handleSave}
                      className="bg-gradient-to-r from-indigo-600 to-violet-600 hover:from-indigo-700 hover:to-violet-700 text-white"
                    >
                      <Save className="h-4 w-4 mr-2" />
                      Save
                    </Button>
                  ) : (
                    <Button
                      onClick={handleEdit}
                      variant="outline"
                      className="border-indigo-200 dark:border-indigo-800 text-indigo-600 dark:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-indigo-950/50"
                    >
                      <Edit className="h-4 w-4 mr-2" />
                      Edit
                    </Button>
                  )}
                </CardFooter>
              </Card>

              {/* Stats Cards */}
              <Card className="md:col-span-1 bg-white/50 dark:bg-gray-900/50 backdrop-blur-sm border-indigo-100/30 dark:border-indigo-800/30 shadow-md group hover:shadow-lg transition-shadow">
                <div className="absolute inset-0 bg-gradient-to-br from-violet-500/5 to-indigo-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg"></div>
                <CardContent className="p-6">
                  <div className="flex items-center mb-4">
                    <div className="relative mr-2">
                      <div className="absolute -inset-1 bg-gradient-to-r from-violet-600 to-indigo-600 rounded-full blur-sm opacity-70"></div>
                      <div className="relative bg-white dark:bg-gray-900 rounded-full p-1.5">
                        <FileText className="h-5 w-5 text-transparent bg-gradient-to-br from-violet-500 to-indigo-600 bg-clip-text" />
                      </div>
                    </div>
                    <h3 className="text-lg font-semibold bg-gradient-to-r from-violet-600 to-indigo-600 bg-clip-text text-transparent">
                      Resume Score
                    </h3>
                  </div>
                  <div className="text-center mb-4">
                    <div className="relative inline-flex items-center justify-center">
                      <div className="absolute inset-0 bg-gradient-to-r from-violet-600/20 to-indigo-600/20 rounded-full blur-sm"></div>
                      <div className="text-4xl font-bold text-indigo-600 dark:text-indigo-400">
                        {profileData.resumeScore}
                      </div>
                      <div className="text-lg text-indigo-400 dark:text-indigo-500">
                        /100
                      </div>
                    </div>
                  </div>
                  <div className="relative">
                    <div className="absolute -inset-0.5 bg-gradient-to-r from-violet-500/20 to-indigo-500/20 rounded-full blur-sm"></div>
                    <Progress
                      value={profileData.resumeScore}
                      className="h-2 bg-indigo-100 dark:bg-indigo-950/30"
                      indicatorClassName="bg-gradient-to-r from-violet-500 to-indigo-600"
                    />
                  </div>
                  <p className="text-xs text-center mt-2 text-muted-foreground">
                    Your resume is performing better than 75% of users
                  </p>
                </CardContent>
              </Card>

              <Card className="md:col-span-1 bg-white/50 dark:bg-gray-900/50 backdrop-blur-sm border-indigo-100/30 dark:border-indigo-800/30 shadow-md group hover:shadow-lg transition-shadow">
                <div className="absolute inset-0 bg-gradient-to-br from-blue-500/5 to-cyan-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg"></div>
                <CardContent className="p-6">
                  <div className="flex items-center mb-4">
                    <div className="relative mr-2">
                      <div className="absolute -inset-1 bg-gradient-to-r from-blue-600 to-cyan-600 rounded-full blur-sm opacity-70"></div>
                      <div className="relative bg-white dark:bg-gray-900 rounded-full p-1.5">
                        <Briefcase className="h-5 w-5 text-transparent bg-gradient-to-br from-blue-500 to-cyan-600 bg-clip-text" />
                      </div>
                    </div>
                    <h3 className="text-lg font-semibold bg-gradient-to-r from-blue-600 to-cyan-600 bg-clip-text text-transparent">
                      Applications
                    </h3>
                  </div>
                  <div className="grid grid-cols-2 gap-2 text-center">
                    <div className="bg-blue-50 dark:bg-blue-950/20 rounded-lg p-2">
                      <div className="text-2xl font-bold text-blue-600 dark:text-blue-400">
                        {profileData.jobApplications}
                      </div>
                      <div className="text-xs text-muted-foreground">
                        Applied
                      </div>
                    </div>
                    <div className="bg-emerald-50 dark:bg-emerald-950/20 rounded-lg p-2">
                      <div className="text-2xl font-bold text-emerald-600 dark:text-emerald-400">
                        {profileData.interviews}
                      </div>
                      <div className="text-xs text-muted-foreground">
                        Interviews
                      </div>
                    </div>
                  </div>
                  <div className="flex items-center justify-center mt-4">
                    <Badge className="bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-300 border-blue-200 dark:border-blue-800">
                      <CheckCircle className="h-3 w-3 mr-1" />
                      33% Interview Rate
                    </Badge>
                  </div>
                </CardContent>
              </Card>

              <Card className="md:col-span-1 bg-white/50 dark:bg-gray-900/50 backdrop-blur-sm border-indigo-100/30 dark:border-indigo-800/30 shadow-md group hover:shadow-lg transition-shadow">
                <div className="absolute inset-0 bg-gradient-to-br from-amber-500/5 to-yellow-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg"></div>
                <CardContent className="p-6">
                  <div className="flex items-center mb-4">
                    <div className="relative mr-2">
                      <div className="absolute -inset-1 bg-gradient-to-r from-amber-500 to-yellow-500 rounded-full blur-sm opacity-70"></div>
                      <div className="relative bg-white dark:bg-gray-900 rounded-full p-1.5">
                        <Award className="h-5 w-5 text-transparent bg-gradient-to-br from-amber-500 to-yellow-500 bg-clip-text" />
                      </div>
                    </div>
                    <h3 className="text-lg font-semibold bg-gradient-to-r from-amber-500 to-yellow-500 bg-clip-text text-transparent">
                      Activity
                    </h3>
                  </div>
                  <div className="space-y-2">
                    <div className="flex items-center justify-between">
                      <div className="flex items-center">
                        <Clock className="h-4 w-4 text-amber-500 mr-2" />
                        <span className="text-sm">Last login</span>
                      </div>
                      <span className="text-sm text-muted-foreground">
                        Today, 9:42 AM
                      </span>
                    </div>
                    <div className="flex items-center justify-between">
                      <div className="flex items-center">
                        <FileText className="h-4 w-4 text-amber-500 mr-2" />
                        <span className="text-sm">Resume updated</span>
                      </div>
                      <span className="text-sm text-muted-foreground">
                        2 days ago
                      </span>
                    </div>
                    <div className="flex items-center justify-between">
                      <div className="flex items-center">
                        <Briefcase className="h-4 w-4 text-amber-500 mr-2" />
                        <span className="text-sm">Last application</span>
                      </div>
                      <span className="text-sm text-muted-foreground">
                        3 days ago
                      </span>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>

            {/* Skills Section */}
            <Card className="bg-white/50 dark:bg-gray-900/50 backdrop-blur-sm border-indigo-100/30 dark:border-indigo-800/30 shadow-md">
              <CardHeader>
                <CardTitle className="flex items-center">
                  <Zap className="h-5 w-5 text-amber-500 mr-2" />
                  <span className="bg-gradient-to-r from-amber-500 to-yellow-500 bg-clip-text text-transparent">
                    Skills
                  </span>
                </CardTitle>
                <CardDescription>
                  Your professional skills and proficiency levels
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  {profileData.skills.map((skill, index) => (
                    <div key={index}>
                      <div className="flex justify-between mb-1">
                        <span className="text-sm font-medium">
                          {skill.name}
                        </span>
                        <span className="text-sm font-medium">
                          {skill.level}%
                        </span>
                      </div>
                      <div className="relative">
                        <div className="absolute -inset-0.5 bg-gradient-to-r from-amber-500/20 to-yellow-500/20 rounded-full blur-sm"></div>
                        <Progress
                          value={skill.level}
                          className="h-2 bg-amber-100 dark:bg-amber-950/30"
                          indicatorClassName="bg-gradient-to-r from-amber-500 to-yellow-500"
                        />
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="resume" className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {/* Education Section */}
              <Card className="bg-white/50 dark:bg-gray-900/50 backdrop-blur-sm border-indigo-100/30 dark:border-indigo-800/30 shadow-md">
                <CardHeader>
                  <CardTitle className="flex items-center">
                    <Award className="h-5 w-5 text-indigo-500 mr-2" />
                    <span className="bg-gradient-to-r from-indigo-600 to-blue-600 bg-clip-text text-transparent">
                      Education
                    </span>
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    {profileData.education.map((edu, index) => (
                      <div
                        key={index}
                        className="border-l-2 border-indigo-300 dark:border-indigo-700 pl-4 py-1 group hover:border-indigo-500 dark:hover:border-indigo-500 transition-colors"
                      >
                        <h4 className="font-semibold group-hover:text-indigo-600 dark:group-hover:text-indigo-400 transition-colors">
                          {edu.degree}
                        </h4>
                        <p className="text-sm text-muted-foreground">
                          {edu.institution}
                        </p>
                        <p className="text-xs text-muted-foreground">
                          {edu.year}
                        </p>
                      </div>
                    ))}
                  </div>
                </CardContent>
                <CardFooter>
                  <Button
                    variant="outline"
                    size="sm"
                    className="w-full border-indigo-200 dark:border-indigo-800 text-indigo-600 dark:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-indigo-950/50"
                  >
                    <Edit className="h-4 w-4 mr-2" />
                    Edit Education
                  </Button>
                </CardFooter>
              </Card>

              {/* Experience Section */}
              <Card className="bg-white/50 dark:bg-gray-900/50 backdrop-blur-sm border-indigo-100/30 dark:border-indigo-800/30 shadow-md">
                <CardHeader>
                  <CardTitle className="flex items-center">
                    <Briefcase className="h-5 w-5 text-blue-500 mr-2" />
                    <span className="bg-gradient-to-r from-blue-600 to-cyan-600 bg-clip-text text-transparent">
                      Experience
                    </span>
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    {profileData.experience.map((exp, index) => (
                      <div
                        key={index}
                        className="border-l-2 border-blue-300 dark:border-blue-700 pl-4 py-1 group hover:border-blue-500 dark:hover:border-blue-500 transition-colors"
                      >
                        <h4 className="font-semibold group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">
                          {exp.title}
                        </h4>
                        <p className="text-sm text-muted-foreground">
                          {exp.company}
                        </p>
                        <p className="text-xs text-muted-foreground">
                          {exp.period}
                        </p>
                        <p className="text-sm mt-1">{exp.description}</p>
                      </div>
                    ))}
                  </div>
                </CardContent>
                <CardFooter>
                  <Button
                    variant="outline"
                    size="sm"
                    className="w-full border-blue-200 dark:border-blue-800 text-blue-600 dark:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-950/50"
                  >
                    <Edit className="h-4 w-4 mr-2" />
                    Edit Experience
                  </Button>
                </CardFooter>
              </Card>
            </div>

            {/* Certifications Section */}
            <Card className="bg-white/50 dark:bg-gray-900/50 backdrop-blur-sm border-indigo-100/30 dark:border-indigo-800/30 shadow-md">
              <CardHeader>
                <CardTitle className="flex items-center">
                  <Star className="h-5 w-5 text-amber-500 mr-2" />
                  <span className="bg-gradient-to-r from-amber-500 to-yellow-500 bg-clip-text text-transparent">
                    Certifications
                  </span>
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {profileData.certifications.map((cert, index) => (
                    <div
                      key={index}
                      className="bg-amber-50/50 dark:bg-amber-950/10 rounded-lg p-4 border border-amber-200/50 dark:border-amber-800/30 group hover:border-amber-300 dark:hover:border-amber-700 transition-colors"
                    >
                      <h4 className="font-semibold group-hover:text-amber-600 dark:group-hover:text-amber-400 transition-colors">
                        {cert.name}
                      </h4>
                      <p className="text-sm text-muted-foreground">
                        {cert.issuer}
                      </p>
                      <p className="text-xs text-muted-foreground">
                        {cert.date}
                      </p>
                    </div>
                  ))}
                </div>
              </CardContent>
              <CardFooter className="flex justify-between">
                <Button
                  variant="outline"
                  size="sm"
                  className="border-amber-200 dark:border-amber-800 text-amber-600 dark:text-amber-400 hover:bg-amber-50 dark:hover:bg-amber-950/50"
                >
                  <Edit className="h-4 w-4 mr-2" />
                  Edit Certifications
                </Button>
                <Button
                  size="sm"
                  className="bg-gradient-to-r from-amber-500 to-yellow-500 hover:from-amber-600 hover:to-yellow-600 text-white"
                >
                  <Upload className="h-4 w-4 mr-2" />
                  Add New
                </Button>
              </CardFooter>
            </Card>

            {/* Resume Actions */}
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <div className="relative group">
                <div className="absolute -inset-0.5 bg-gradient-to-r from-violet-600 to-indigo-600 rounded-lg blur opacity-30 group-hover:opacity-100 transition duration-300"></div>
                <Button
                  onClick={() => navigate("/resume-upload")}
                  className="relative w-full sm:w-auto bg-white dark:bg-gray-900 text-indigo-600 dark:text-indigo-400 border border-indigo-200 dark:border-indigo-800 hover:bg-indigo-50 dark:hover:bg-indigo-950/50"
                >
                  <Upload className="h-4 w-4 mr-2" />
                  Upload New Resume
                </Button>
              </div>
              <Button
                variant="outline"
                className="w-full sm:w-auto border-blue-200 dark:border-blue-800 text-blue-600 dark:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-950/50"
              >
                <Download className="h-4 w-4 mr-2" />
                Download Current Resume
              </Button>
              <Button
                variant="outline"
                className="w-full sm:w-auto border-amber-200 dark:border-amber-800 text-amber-600 dark:text-amber-400 hover:bg-amber-50 dark:hover:bg-amber-950/50"
              >
                <Sparkles className="h-4 w-4 mr-2" />
                AI Resume Analysis
              </Button>
            </div>
          </TabsContent>

       

<TabsContent value="applications" className="space-y-6">
  <Card className="bg-white/50 dark:bg-gray-900/50 backdrop-blur-sm border-indigo-100/30 dark:border-indigo-800/30 shadow-md">
    <CardHeader>
      <CardTitle className="flex items-center">
        <Briefcase className="h-5 w-5 text-blue-500 mr-2" />
        <span className="bg-gradient-to-r from-blue-600 to-cyan-600 bg-clip-text text-transparent">
          Job Applications
        </span>
      </CardTitle>
      <CardDescription>
        Track your recent job applications and their status
      </CardDescription>
    </CardHeader>
    <CardContent>
      <AppliedJobs /> {/* ✅ Render the AppliedJobs component here */}
    </CardContent>
    <CardFooter className="flex justify-between">
      <Button
        variant="outline"
        className="border-blue-200 dark:border-blue-800 text-blue-600 dark:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-950/50"
      >
        <Briefcase className="h-4 w-4 mr-2" />
        View All Applications
      </Button>
      <Button
        className="bg-gradient-to-r from-blue-600 to-cyan-600 hover:from-blue-700 hover:to-cyan-700 text-white"
        onClick={() => navigate("/job-matches")}
      >
        <Sparkles className="h-4 w-4 mr-2" />
        Find Jobs
      </Button>
    </CardFooter>
  </Card>
</TabsContent>


          <TabsContent value="settings" className="space-y-6">
            <Card className="bg-white/50 dark:bg-gray-900/50 backdrop-blur-sm border-indigo-100/30 dark:border-indigo-800/30 shadow-md">
              <CardHeader>
                <CardTitle className="flex items-center">
                  <Settings className="h-5 w-5 text-indigo-500 mr-2" />
                  <span className="bg-gradient-to-r from-indigo-600 to-blue-600 bg-clip-text text-transparent">
                    Account Settings
                  </span>
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="space-y-2">
                  <Label htmlFor="name">Full Name</Label>
                  <Input
                    id="name"
                    name="name"
                    value={profileData.name}
                    onChange={handleInputChange}
                    className="bg-white/70 dark:bg-gray-900/70 border-indigo-200 dark:border-indigo-800 focus:border-indigo-400 focus:ring-indigo-400"
                  />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="email">Email Address</Label>
                  <Input
                    id="email"
                    name="email"
                    type="email"
                    value={profileData.email}
                    onChange={handleInputChange}
                    className="bg-white/70 dark:bg-gray-900/70 border-indigo-200 dark:border-indigo-800 focus:border-indigo-400 focus:ring-indigo-400"
                  />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="phone">Phone Number</Label>
                  <Input
                    id="phone"
                    name="phone"
                    value={profileData.phone}
                    onChange={handleInputChange}
                    className="bg-white/70 dark:bg-gray-900/70 border-indigo-200 dark:border-indigo-800 focus:border-indigo-400 focus:ring-indigo-400"
                  />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="location">Location</Label>
                  <Input
                    id="location"
                    name="location"
                    value={profileData.location}
                    onChange={handleInputChange}
                    className="bg-white/70 dark:bg-gray-900/70 border-indigo-200 dark:border-indigo-800 focus:border-indigo-400 focus:ring-indigo-400"
                  />
                </div>
              </CardContent>
              <CardFooter>
                <Button className="w-full bg-gradient-to-r from-indigo-600 to-violet-600 hover:from-indigo-700 hover:to-violet-700 text-white">
                  <Save className="h-4 w-4 mr-2" />
                  Save Changes
                </Button>
              </CardFooter>
            </Card>

            <Card className="bg-white/50 dark:bg-gray-900/50 backdrop-blur-sm border-indigo-100/30 dark:border-indigo-800/30 shadow-md">
              <CardHeader>
                <CardTitle className="flex items-center">
                  <Shield className="h-5 w-5 text-indigo-500 mr-2" />
                  <span className="bg-gradient-to-r from-indigo-600 to-blue-600 bg-clip-text text-transparent">
                    Privacy & Notifications
                  </span>
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="flex items-center justify-between">
                  <div className="space-y-0.5">
                    <Label className="text-base">Email Notifications</Label>
                    <p className="text-sm text-muted-foreground">
                      Receive job alerts and application updates
                    </p>
                  </div>
                  <Switch defaultChecked />
                </div>
                <div className="flex items-center justify-between">
                  <div className="space-y-0.5">
                    <Label className="text-base">Profile Visibility</Label>
                    <p className="text-sm text-muted-foreground">
                      Allow recruiters to view your profile
                    </p>
                  </div>
                  <Switch defaultChecked />
                </div>
                <div className="flex items-center justify-between">
                  <div className="space-y-0.5">
                    <Label className="text-base">
                      Two-Factor Authentication
                    </Label>
                    <p className="text-sm text-muted-foreground">
                      Add an extra layer of security
                    </p>
                  </div>
                  <Switch />
                </div>
              </CardContent>
            </Card>

            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button
                variant="outline"
                className="w-full sm:w-auto border-red-200 dark:border-red-800 text-red-600 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-950/50"
              >
                <LogOut className="h-4 w-4 mr-2" />
                Sign Out
              </Button>
              <Button
                variant="outline"
                className="w-full sm:w-auto border-red-200 dark:border-red-800 text-red-600 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-950/50"
              >
                <Trash2 className="h-4 w-4 mr-2" />
                Delete Account
              </Button>
            </div>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  );
};

export default Profile;

/**
 * Custom Progress component with gradient support
 */
const CustomProgress = ({ value, className, indicatorClassName, ...props }) => {
  return (
    <div
      className={`h-2 w-full overflow-hidden rounded-full bg-secondary ${className}`}
      {...props}
    >
      <div
        className={`h-full ${indicatorClassName || "bg-primary"}`}
        style={{ width: `${value}%` }}
      />
    </div>
  );
};
