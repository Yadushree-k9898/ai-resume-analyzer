import { Mail, Facebook, Twitter, Instagram, Linkedin, Github, ArrowRight, Sparkles, Star, Zap } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

export default function Footer() {
  return (
    <footer className="relative overflow-hidden border-t border-indigo-100 dark:border-indigo-900">
      {/* Background gradients */}
      <div className="absolute inset-0 bg-gradient-to-b from-white to-indigo-50/50 dark:from-background dark:to-indigo-950/20 pointer-events-none"></div>
      <div className="absolute -top-40 -right-40 w-80 h-80 bg-pink-400/10 dark:bg-pink-600/5 rounded-full blur-3xl"></div>
      <div className="absolute -bottom-40 -left-40 w-80 h-80 bg-blue-400/10 dark:bg-blue-600/5 rounded-full blur-3xl"></div>

      {/* Top decorative border */}
      <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-indigo-300 dark:via-indigo-700 to-transparent"></div>

      <div className="container px-4 py-16 mx-auto relative z-10">
        <div className="grid grid-cols-1 gap-12 lg:grid-cols-4 md:grid-cols-2">
          {/* Company Info */}
          <div className="space-y-5">
            <div className="flex items-center gap-2">
              <div className="relative">
                <div className="absolute -inset-1 bg-gradient-to-r from-violet-600 to-indigo-600 rounded-full blur-sm opacity-70"></div>
                <div className="relative bg-white dark:bg-gray-900 rounded-full p-1.5">
                  <Mail className="h-6 w-6 text-transparent bg-gradient-to-br from-violet-500 to-indigo-600 bg-clip-text" />
                </div>
              </div>
              <h3 className="text-xl font-bold bg-gradient-to-r from-violet-600 via-indigo-600 to-purple-600 bg-clip-text text-transparent">
                AnalyseAI
              </h3>
              <Sparkles className="h-4 w-4 text-amber-400" />
            </div>
            <p className="text-muted-foreground text-sm">
              Empowering job seekers with AI-powered resume analysis and career insights to land their dream jobs.
            </p>
            <div className="flex space-x-5">
              {[
                { icon: Facebook, color: "hover:text-blue-600 dark:hover:text-blue-400", label: "Facebook" },
                { icon: Twitter, color: "hover:text-sky-500 dark:hover:text-sky-400", label: "Twitter" },
                { icon: Instagram, color: "hover:text-pink-600 dark:hover:text-pink-400", label: "Instagram" },
                { icon: Linkedin, color: "hover:text-blue-700 dark:hover:text-blue-500", label: "LinkedIn" },
                { icon: Github, color: "hover:text-gray-900 dark:hover:text-white", label: "GitHub" },
              ].map((social, index) => (
                <a
                  key={index}
                  href="#"
                  className={`text-muted-foreground ${social.color} transition-all duration-300 transform hover:scale-110`}
                  aria-label={social.label}
                >
                  <social.icon className="h-5 w-5" />
                </a>
              ))}
            </div>
          </div>

          {/* Quick Links */}
          <div className="space-y-5">
            <h3 className="text-lg font-semibold relative inline-flex items-center">
              <span className="bg-gradient-to-r from-indigo-600 to-blue-600 bg-clip-text text-transparent">
                Quick Links
              </span>
              <Zap className="ml-2 h-4 w-4 text-amber-500" />
            </h3>
            <ul className="space-y-3 grid">
              {[
                { name: "Home", path: "/" },
                { name: "Features", path: "/features" },
                { name: "Pricing", path: "/pricing" },
                { name: "Blog", path: "/blog" },
                { name: "About Us", path: "/about" },
                { name: "Contact", path: "/contact" },
              ].map((link, index) => (
                <li key={index}>
                  <a
                    href={link.path}
                    className="text-muted-foreground hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors text-sm flex items-center group"
                  >
                    <span className="w-0 h-px bg-indigo-600 dark:bg-indigo-400 transition-all duration-300 mr-0 group-hover:w-2 group-hover:mr-2"></span>
                    {link.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Resources */}
          <div className="space-y-5">
            <h3 className="text-lg font-semibold relative inline-flex items-center">
              <span className="bg-gradient-to-r from-blue-600 to-cyan-600 bg-clip-text text-transparent">
                Resources
              </span>
              <Star className="ml-2 h-4 w-4 text-amber-500" />
            </h3>
            <ul className="space-y-3 grid">
              {[
                { name: "Help Center", path: "/help" },
                { name: "Career Tips", path: "/career-tips" },
                { name: "Resume Templates", path: "/resume-templates" },
                { name: "Interview Prep", path: "/interview-prep" },
                { name: "API Documentation", path: "/api" },
                { name: "Privacy Policy", path: "/privacy" },
                { name: "Terms of Service", path: "/terms" },
              ].map((link, index) => (
                <li key={index}>
                  <a
                    href={link.path}
                    className="text-muted-foreground hover:text-blue-600 dark:hover:text-blue-400 transition-colors text-sm flex items-center group"
                  >
                    <span className="w-0 h-px bg-blue-600 dark:bg-blue-400 transition-all duration-300 mr-0 group-hover:w-2 group-hover:mr-2"></span>
                    {link.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Newsletter */}
          <div className="space-y-5">
            <h3 className="text-lg font-semibold relative inline-flex items-center">
              <span className="bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
                Stay Updated
              </span>
              <Sparkles className="ml-2 h-4 w-4 text-amber-500" />
            </h3>
            <p className="text-muted-foreground text-sm">
              Subscribe to our newsletter for the latest career tips and updates.
            </p>
            <form className="space-y-3">
              <div className="relative group">
                <div className="absolute -inset-0.5 bg-gradient-to-r from-purple-600 to-pink-600 rounded-lg blur opacity-30 group-hover:opacity-100 transition duration-300"></div>
                <div className="relative flex gap-2 bg-background rounded-lg p-0.5">
                  <Input
                    type="email"
                    placeholder="Your email address"
                    className="bg-background border-0 focus-visible:ring-1 focus-visible:ring-purple-500"
                    required
                  />
                  <Button
                    type="submit"
                    size="sm"
                    className="shrink-0 bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 text-white border-0"
                  >
                    <ArrowRight className="h-4 w-4" />
                  </Button>
                </div>
              </div>
              <p className="text-xs text-muted-foreground">
                By subscribing, you agree to our Privacy Policy and consent to receive updates.
              </p>
            </form>
          </div>
        </div>

        <div className="pt-10 mt-10 border-t border-indigo-100/30 dark:border-indigo-800/30 relative">
          <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-indigo-300/50 dark:via-indigo-700/50 to-transparent"></div>
          <div className="flex flex-col md:flex-row justify-between items-center">
            <p className="text-sm text-muted-foreground">
              © {new Date().getFullYear()} AnalyseAI. All rights reserved.
            </p>
            <div className="flex space-x-6 mt-4 md:mt-0">
              {[
                { name: "Privacy", path: "/privacy" },
                { name: "Terms", path: "/terms" },
                { name: "Cookies", path: "/cookies" },
                { name: "Sitemap", path: "/sitemap" },
              ].map((link, index) => (
                <a
                  key={index}
                  href={link.path}
                  className="text-sm text-muted-foreground hover:text-primary transition-colors relative group"
                >
                  <span>{link.name}</span>
                  <span className="absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-indigo-600 to-purple-600 transition-all duration-300 group-hover:w-full"></span>
                </a>
              ))}
            </div>
          </div>
        </div>
      </div>
    </footer>
  )
}

