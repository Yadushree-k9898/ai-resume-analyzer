import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { FileUp, CheckCircle, Search, TrendingUp, ArrowRight, FileSearch, Award, Sparkles, Star } from "lucide-react"

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen">
      <main className="flex-1">
        {/* Hero Section with vibrant gradient */}
        <section className="w-full py-12 md:py-24 lg:py-32 relative overflow-hidden">
          {/* Animated background elements */}
          <div className="absolute inset-0 bg-gradient-to-br from-violet-500/20 via-indigo-400/10 to-blue-500/20 dark:from-violet-500/10 dark:via-indigo-400/5 dark:to-blue-500/10"></div>
          <div className="absolute -top-40 -right-40 w-80 h-80 bg-pink-400/30 dark:bg-pink-600/20 rounded-full blur-3xl"></div>
          <div className="absolute -bottom-40 -left-40 w-80 h-80 bg-blue-400/30 dark:bg-blue-600/20 rounded-full blur-3xl"></div>

          <div className="container px-4 md:px-6 relative z-10">
            <div className="grid gap-6 lg:grid-cols-2 lg:gap-12 items-center">
              <div className="flex flex-col justify-center space-y-4">
                <div className="inline-flex items-center rounded-lg bg-gradient-to-r from-violet-500 to-indigo-500 px-3 py-1 text-sm text-white shadow-lg shadow-violet-500/20 dark:shadow-violet-700/20 max-w-fit">
                  <Sparkles className="mr-1 h-4 w-4" />
                  AI-Powered Resume Analysis
                </div>
                <div className="space-y-2">
                  <h1 className="text-3xl font-bold tracking-tighter sm:text-5xl xl:text-6xl/none bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-600 dark:from-indigo-400 dark:via-purple-400 dark:to-pink-400 bg-clip-text text-transparent">
                    Elevate Your Career with AnalyseAI
                  </h1>
                  <p className="max-w-[600px] text-muted-foreground md:text-xl">
                    Our intelligent resume analyzer helps you land your dream job by providing personalized insights,
                    skill gap analysis, and job matching.
                  </p>
                </div>
                <div className="flex flex-col gap-2 min-[400px]:flex-row">
                  <Button
                    size="lg"
                    className="gap-1 bg-gradient-to-r from-violet-600 to-indigo-600 hover:from-violet-700 hover:to-indigo-700 border-0 text-white shadow-lg shadow-indigo-500/30 dark:shadow-indigo-700/30 transition-all duration-300"
                  >
                    Upload Resume <FileUp className="h-4 w-4 ml-1" />
                  </Button>
                  <Button
                    size="lg"
                    variant="outline"
                    className="border-indigo-200 dark:border-indigo-800 hover:bg-indigo-50 dark:hover:bg-indigo-950 transition-all duration-300"
                  >
                    See How It Works
                  </Button>
                </div>
              </div>
              <div className="mx-auto lg:mx-0 relative w-full max-w-[500px] aspect-video rounded-xl overflow-hidden border bg-background/80 backdrop-blur-sm p-4 shadow-2xl shadow-indigo-500/20 dark:shadow-indigo-700/20 transition-all duration-300 hover:shadow-indigo-500/30 dark:hover:shadow-indigo-700/30">
                <div className="absolute inset-0 bg-gradient-to-r from-violet-500/5 to-indigo-500/10 rounded-lg"></div>
                <div className="relative z-10 h-full flex flex-col justify-center items-center gap-4 p-6 text-center">
                  <div className="w-full max-w-sm p-4 bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-indigo-100 dark:border-indigo-900">
                    <div className="flex items-center mb-3">
                      <FileSearch className="h-5 w-5 text-indigo-500 mr-2" />
                      <div className="h-2 w-24 bg-indigo-200 dark:bg-indigo-700 rounded"></div>
                    </div>
                    <div className="h-2 w-full bg-muted rounded mb-2"></div>
                    <div className="h-2 w-full bg-muted rounded mb-2"></div>
                    <div className="h-2 w-3/4 bg-muted rounded"></div>
                  </div>
                  <div className="flex gap-2">
                    <div className="h-10 w-10 rounded-full bg-gradient-to-br from-violet-500 to-indigo-500 flex items-center justify-center shadow-md">
                      <ArrowRight className="h-5 w-5 text-white" />
                    </div>
                    <div className="h-10 w-10 rounded-full bg-gradient-to-br from-indigo-500 to-blue-500 flex items-center justify-center shadow-md">
                      <ArrowRight className="h-5 w-5 text-white" />
                    </div>
                  </div>
                  <div className="w-full max-w-sm p-4 bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-indigo-100 dark:border-indigo-900">
                    <div className="flex justify-between mb-3">
                      <div className="h-2 w-24 bg-green-300 dark:bg-green-700 rounded"></div>
                      <div className="h-2 w-16 bg-green-400 dark:bg-green-600 rounded"></div>
                    </div>
                    <div className="h-2 w-full bg-muted rounded mb-2"></div>
                    <div className="h-2 w-full bg-muted rounded mb-2"></div>
                    <div className="h-2 w-3/4 bg-muted rounded"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* How it Works Section */}
        <section className="w-full py-12 md:py-24 lg:py-32 relative">
          <div className="absolute inset-0 bg-gradient-to-t from-indigo-50/50 to-white/0 dark:from-indigo-950/50 dark:to-background/0"></div>
          <div className="container px-4 md:px-6 relative z-10">
            <div className="flex flex-col items-center justify-center space-y-4 text-center">
              <div className="inline-flex items-center rounded-lg bg-gradient-to-r from-amber-400 to-orange-400 px-3 py-1 text-sm text-white shadow-lg shadow-amber-500/20 dark:shadow-amber-700/20 max-w-fit">
                <Award className="mr-1 h-4 w-4" />
                Trusted by 10,000+ professionals
              </div>
              <div className="space-y-2">
                <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl bg-gradient-to-r from-amber-600 to-orange-600 dark:from-amber-400 dark:to-orange-400 bg-clip-text text-transparent">
                  How AnalyseAI Works
                </h2>
                <p className="max-w-[900px] text-muted-foreground md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                  Our AI-powered system analyzes your resume and provides personalized recommendations in minutes.
                </p>
              </div>
            </div>
            <div className="mx-auto grid max-w-5xl items-center gap-6 py-12 lg:grid-cols-3 lg:gap-12">
              <div className="flex flex-col justify-center space-y-4 group">
                <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-violet-500 to-indigo-600 text-white shadow-lg shadow-violet-500/20 dark:shadow-violet-700/20 transition-all duration-300 group-hover:shadow-violet-500/40 dark:group-hover:shadow-violet-700/40">
                  <FileUp className="h-8 w-8" />
                </div>
                <h3 className="text-xl font-bold">Upload Your Resume</h3>
                <p className="text-muted-foreground">
                  Simply upload your resume in PDF, DOCX, or TXT format and our AI will start analyzing it immediately.
                </p>
              </div>
              <div className="flex flex-col justify-center space-y-4 group">
                <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-indigo-500 to-blue-600 text-white shadow-lg shadow-indigo-500/20 dark:shadow-indigo-700/20 transition-all duration-300 group-hover:shadow-indigo-500/40 dark:group-hover:shadow-indigo-700/40">
                  <Search className="h-8 w-8" />
                </div>
                <h3 className="text-xl font-bold">Get Detailed Analysis</h3>
                <p className="text-muted-foreground">
                  Receive insights on your resume's strengths, weaknesses, and suggestions for improvement tailored to
                  your industry.
                </p>
              </div>
              <div className="flex flex-col justify-center space-y-4 group">
                <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-blue-500 to-cyan-600 text-white shadow-lg shadow-blue-500/20 dark:shadow-blue-700/20 transition-all duration-300 group-hover:shadow-blue-500/40 dark:group-hover:shadow-blue-700/40">
                  <TrendingUp className="h-8 w-8" />
                </div>
                <h3 className="text-xl font-bold">Find Opportunities</h3>
                <p className="text-muted-foreground">
                  Discover job opportunities that match your skills and experience, with personalized recommendations to
                  improve your chances.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Features Section */}
        <section className="w-full py-12 md:py-24 lg:py-32 bg-gradient-to-b from-indigo-50 to-white dark:from-indigo-950 dark:to-background relative overflow-hidden">
          <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-indigo-300 dark:via-indigo-700 to-transparent"></div>
          <div className="absolute bottom-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-indigo-300 dark:via-indigo-700 to-transparent"></div>

          {/* Decorative elements */}
          <div className="absolute top-40 right-20 w-64 h-64 bg-pink-400/10 dark:bg-pink-600/10 rounded-full blur-3xl"></div>
          <div className="absolute bottom-40 left-20 w-64 h-64 bg-blue-400/10 dark:bg-blue-600/10 rounded-full blur-3xl"></div>

          <div className="container px-4 md:px-6 relative z-10">
            <div className="flex flex-col items-center justify-center space-y-4 text-center">
              <div className="space-y-2">
                <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl bg-gradient-to-r from-blue-600 to-cyan-600 dark:from-blue-400 dark:to-cyan-400 bg-clip-text text-transparent">
                  Key Features
                </h2>
                <p className="max-w-[900px] text-muted-foreground md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                  Our comprehensive analysis helps you stand out in the job market.
                </p>
              </div>
            </div>
            <div className="mx-auto grid max-w-5xl grid-cols-1 gap-6 py-12 md:grid-cols-2 lg:gap-12">
              <Card className="group overflow-hidden border-indigo-100 dark:border-indigo-900 bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm hover:shadow-lg hover:shadow-indigo-500/10 dark:hover:shadow-indigo-700/10 transition-all duration-300">
                <div className="absolute inset-0 bg-gradient-to-br from-violet-500/5 via-transparent to-transparent rounded-lg"></div>
                <CardHeader className="relative z-10">
                  <div className="flex items-center gap-2">
                    <div className="flex h-8 w-8 items-center justify-center rounded-full bg-gradient-to-br from-violet-500 to-indigo-600 text-white">
                      <FileUp className="h-4 w-4" />
                    </div>
                    <CardTitle>Resume Improvement</CardTitle>
                  </div>
                  <CardDescription>Get actionable feedback to enhance your resume</CardDescription>
                </CardHeader>
                <CardContent className="relative z-10">
                  <ul className="grid gap-2">
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-5 w-5 text-green-500" />
                      <span>Content and formatting suggestions</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-5 w-5 text-green-500" />
                      <span>Industry-specific keyword recommendations</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-5 w-5 text-green-500" />
                      <span>ATS compatibility check</span>
                    </li>
                  </ul>
                </CardContent>
              </Card>

              <Card className="group overflow-hidden border-indigo-100 dark:border-indigo-900 bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm hover:shadow-lg hover:shadow-indigo-500/10 dark:hover:shadow-indigo-700/10 transition-all duration-300">
                <div className="absolute inset-0 bg-gradient-to-br from-indigo-500/5 via-transparent to-transparent rounded-lg"></div>
                <CardHeader className="relative z-10">
                  <div className="flex items-center gap-2">
                    <div className="flex h-8 w-8 items-center justify-center rounded-full bg-gradient-to-br from-indigo-500 to-blue-600 text-white">
                      <Search className="h-4 w-4" />
                    </div>
                    <CardTitle>Job Matching</CardTitle>
                  </div>
                  <CardDescription>Find opportunities that align with your profile</CardDescription>
                </CardHeader>
                <CardContent className="relative z-10">
                  <ul className="grid gap-2">
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-5 w-5 text-green-500" />
                      <span>Personalized job recommendations</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-5 w-5 text-green-500" />
                      <span>Skills gap analysis for specific roles</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-5 w-5 text-green-500" />
                      <span>Application eligibility assessment</span>
                    </li>
                  </ul>
                </CardContent>
              </Card>

              <Card className="group overflow-hidden border-indigo-100 dark:border-indigo-900 bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm hover:shadow-lg hover:shadow-indigo-500/10 dark:hover:shadow-indigo-700/10 transition-all duration-300">
                <div className="absolute inset-0 bg-gradient-to-br from-blue-500/5 via-transparent to-transparent rounded-lg"></div>
                <CardHeader className="relative z-10">
                  <div className="flex items-center gap-2">
                    <div className="flex h-8 w-8 items-center justify-center rounded-full bg-gradient-to-br from-blue-500 to-cyan-600 text-white">
                      <Star className="h-4 w-4" />
                    </div>
                    <CardTitle>Skills Analysis</CardTitle>
                  </div>
                  <CardDescription>Understand your strengths and areas for growth</CardDescription>
                </CardHeader>
                <CardContent className="relative z-10">
                  <ul className="grid gap-2">
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-5 w-5 text-green-500" />
                      <span>Identification of key skills and competencies</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-5 w-5 text-green-500" />
                      <span>Comparison with industry standards</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-5 w-5 text-green-500" />
                      <span>Skill development recommendations</span>
                    </li>
                  </ul>
                </CardContent>
              </Card>

              <Card className="group overflow-hidden border-indigo-100 dark:border-indigo-900 bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm hover:shadow-lg hover:shadow-indigo-500/10 dark:hover:shadow-indigo-700/10 transition-all duration-300">
                <div className="absolute inset-0 bg-gradient-to-br from-cyan-500/5 via-transparent to-transparent rounded-lg"></div>
                <CardHeader className="relative z-10">
                  <div className="flex items-center gap-2">
                    <div className="flex h-8 w-8 items-center justify-center rounded-full bg-gradient-to-br from-cyan-500 to-teal-600 text-white">
                      <TrendingUp className="h-4 w-4" />
                    </div>
                    <CardTitle>Career Insights</CardTitle>
                  </div>
                  <CardDescription>Get data-driven career guidance</CardDescription>
                </CardHeader>
                <CardContent className="relative z-10">
                  <ul className="grid gap-2">
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-5 w-5 text-green-500" />
                      <span>Salary expectations based on your profile</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-5 w-5 text-green-500" />
                      <span>Industry trends and demand analysis</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle className="h-5 w-5 text-green-500" />
                      <span>Career progression pathways</span>
                    </li>
                  </ul>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* CTA Section */}
        <section className="w-full py-12 md:py-24 lg:py-32 relative overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-indigo-500/10 via-purple-500/5 to-pink-500/10 dark:from-indigo-500/5 dark:via-purple-500/5 dark:to-pink-500/5"></div>
          <div className="absolute -top-40 -left-40 w-80 h-80 bg-pink-400/20 dark:bg-pink-600/10 rounded-full blur-3xl"></div>
          <div className="absolute -bottom-40 -right-40 w-80 h-80 bg-indigo-400/20 dark:bg-indigo-600/10 rounded-full blur-3xl"></div>

          <div className="container px-4 md:px-6 relative z-10">
            <div className="flex flex-col items-center justify-center space-y-4 text-center max-w-3xl mx-auto">
              <div className="inline-flex items-center rounded-full bg-gradient-to-r from-pink-500 to-purple-500 px-4 py-1.5 text-sm text-white shadow-lg shadow-pink-500/20 dark:shadow-pink-700/20 max-w-fit">
                <Sparkles className="mr-1 h-4 w-4" />
                Limited Time Offer
              </div>
              <div className="space-y-2">
                <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl bg-gradient-to-br from-pink-600 via-purple-600 to-indigo-600 dark:from-pink-400 dark:via-purple-400 dark:to-indigo-400 bg-clip-text text-transparent">
                  Ready to Transform Your Job Search?
                </h2>
                <p className="max-w-[900px] text-muted-foreground md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                  Upload your resume now and get personalized insights in minutes.
                </p>
              </div>
              <div className="flex flex-col gap-2 min-[400px]:flex-row mt-6">
                <Button
                  size="lg"
                  className="gap-1 bg-gradient-to-r from-pink-600 to-purple-600 hover:from-pink-700 hover:to-purple-700 border-0 text-white shadow-lg shadow-pink-500/30 dark:shadow-pink-700/30 transition-all duration-300"
                >
                  Get Started <ArrowRight className="h-4 w-4 ml-1" />
                </Button>
                <Button
                  size="lg"
                  variant="outline"
                  className="border-purple-200 dark:border-purple-800 hover:bg-purple-50 dark:hover:bg-purple-950 transition-all duration-300"
                >
                  View Pricing
                </Button>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
  )
}

