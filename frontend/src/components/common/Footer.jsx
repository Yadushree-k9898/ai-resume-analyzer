import { Mail, Facebook, Twitter, Instagram, Linkedin, Github, ArrowRight } from 'lucide-react';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

export default function Footer() {
  return (
    <footer className="bg-muted/40 border-t">
      <div className="container px-4 py-12 mx-auto">
        <div className="grid grid-cols-1 gap-8 lg:grid-cols-4 md:grid-cols-2">
          {/* Company Info */}
          <div className="space-y-4">
            <div className="flex items-center gap-2">
              <Mail className="h-6 w-6 text-primary" />
              <h3 className="text-xl font-bold">AnalyseAI</h3>
            </div>
            <p className="text-muted-foreground text-sm">
              Empowering job seekers with AI-powered resume analysis and career insights to land their dream jobs.
            </p>
            <div className="flex space-x-4">
              <a href="#" className="text-muted-foreground hover:text-primary transition-colors" aria-label="Facebook">
                <Facebook className="h-5 w-5" />
              </a>
              <a href="#" className="text-muted-foreground hover:text-primary transition-colors" aria-label="Twitter">
                <Twitter className="h-5 w-5" />
              </a>
              <a href="#" className="text-muted-foreground hover:text-primary transition-colors" aria-label="Instagram">
                <Instagram className="h-5 w-5" />
              </a>
              <a href="#" className="text-muted-foreground hover:text-primary transition-colors" aria-label="LinkedIn">
                <Linkedin className="h-5 w-5" />
              </a>
              <a href="#" className="text-muted-foreground hover:text-primary transition-colors" aria-label="GitHub">
                <Github className="h-5 w-5" />
              </a>
            </div>
          </div>

          {/* Quick Links */}
          <div className="space-y-4">
            <h3 className="text-lg font-semibold">Quick Links</h3>
            <ul className="space-y-2">
              <li>
                <a href="/" className="text-muted-foreground hover:text-primary transition-colors text-sm">Home</a>
              </li>
              <li>
                <a href="/features" className="text-muted-foreground hover:text-primary transition-colors text-sm">Features</a>
              </li>
              <li>
                <a href="/pricing" className="text-muted-foreground hover:text-primary transition-colors text-sm">Pricing</a>
              </li>
              <li>
                <a href="/blog" className="text-muted-foreground hover:text-primary transition-colors text-sm">Blog</a>
              </li>
              <li>
                <a href="/about" className="text-muted-foreground hover:text-primary transition-colors text-sm">About Us</a>
              </li>
              <li>
                <a href="/contact" className="text-muted-foreground hover:text-primary transition-colors text-sm">Contact</a>
              </li>
            </ul>
          </div>

          {/* Resources */}
          <div className="space-y-4">
            <h3 className="text-lg font-semibold">Resources</h3>
            <ul className="space-y-2">
              <li>
                <a href="/help" className="text-muted-foreground hover:text-primary transition-colors text-sm">Help Center</a>
              </li>
              <li>
                <a href="/career-tips" className="text-muted-foreground hover:text-primary transition-colors text-sm">Career Tips</a>
              </li>
              <li>
                <a href="/resume-templates" className="text-muted-foreground hover:text-primary transition-colors text-sm">Resume Templates</a>
              </li>
              <li>
                <a href="/interview-prep" className="text-muted-foreground hover:text-primary transition-colors text-sm">Interview Prep</a>
              </li>
              <li>
                <a href="/api" className="text-muted-foreground hover:text-primary transition-colors text-sm">API Documentation</a>
              </li>
              <li>
                <a href="/privacy" className="text-muted-foreground hover:text-primary transition-colors text-sm">Privacy Policy</a>
              </li>
              <li>
                <a href="/terms" className="text-muted-foreground hover:text-primary transition-colors text-sm">Terms of Service</a>
              </li>
            </ul>
          </div>

          {/* Newsletter */}
          <div className="space-y-4">
            <h3 className="text-lg font-semibold">Stay Updated</h3>
            <p className="text-muted-foreground text-sm">
              Subscribe to our newsletter for the latest career tips and updates.
            </p>
            <form className="space-y-2">
              <div className="flex gap-2">
                <Input 
                  type="email" 
                  placeholder="Your email address" 
                  className="bg-background" 
                  required
                />
                <Button type="submit" size="sm" className="shrink-0">
                  <ArrowRight className="h-4 w-4" />
                </Button>
              </div>
              <p className="text-xs text-muted-foreground">
                By subscribing, you agree to our Privacy Policy and consent to receive updates.
              </p>
            </form>
          </div>
        </div>

        <div className="pt-8 mt-8 border-t border-muted-foreground/20">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <p className="text-sm text-muted-foreground">
              © {new Date().getFullYear()} AnalyseAI. All rights reserved.
            </p>
            <div className="flex space-x-4 mt-4 md:mt-0">
              <a href="/privacy" className="text-sm text-muted-foreground hover:text-primary transition-colors">
                Privacy
              </a>
              <a href="/terms" className="text-sm text-muted-foreground hover:text-primary transition-colors">
                Terms
              </a>
              <a href="/cookies" className="text-sm text-muted-foreground hover:text-primary transition-colors">
                Cookies
              </a>
              <a href="/sitemap" className="text-sm text-muted-foreground hover:text-primary transition-colors">
                Sitemap
              </a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
