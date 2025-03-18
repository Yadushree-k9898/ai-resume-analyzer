import { Mail, Twitter, Instagram, Linkedin, Github, Sparkles } from "lucide-react";

export default function Footer() {
  return (
    <footer className="relative overflow-hidden border-t border-indigo-100 dark:border-indigo-900">
      {/* Background Gradients */}
      <div className="absolute inset-0 bg-gradient-to-b from-white to-indigo-50/50 dark:from-background dark:to-indigo-950/20 pointer-events-none"></div>
      <div className="absolute -top-40 -right-40 w-80 h-80 bg-pink-400/10 dark:bg-pink-600/5 rounded-full blur-3xl"></div>
      <div className="absolute -bottom-40 -left-40 w-80 h-80 bg-blue-400/10 dark:bg-blue-600/5 rounded-full blur-3xl"></div>

      {/* Top Decorative Border */}
      <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-indigo-300 dark:via-indigo-700 to-transparent"></div>

      <div className="container px-4 py-16 mx-auto relative z-10">
        <div className="grid grid-cols-1 gap-12 lg:grid-cols-2 md:grid-cols-1">
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
            
            {/* Social Links */}
            <div className="flex space-x-5">
              {[
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
        </div>

        {/* Footer Bottom Section */}
        <div className="pt-10 mt-10 border-t border-indigo-100/30 dark:border-indigo-800/30 relative">
          <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-indigo-300/50 dark:via-indigo-700/50 to-transparent"></div>
          <div className="flex flex-col md:flex-row justify-between items-center">
            <p className="text-sm text-muted-foreground">
              © {new Date().getFullYear()} AnalyseAI. All rights reserved.
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
}