import { NavLink } from "react-router-dom";
import { FileSearch, Menu, X } from "lucide-react";
import { useState } from "react";
import ThemeToggle from "../ThemeToggle";

function Navbar() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <nav className="flex justify-between items-center p-4 bg-background shadow-md">
      <div className="flex items-center gap-2 text-xl font-bold text-primary">
        <FileSearch className="h-6 w-6" />
        <span>AnalyseAI</span>
      </div>
      
      {/* Mobile menu button */}
      <button 
        className="md:hidden text-foreground"
        onClick={toggleMenu}
        aria-label={isMenuOpen ? "Close menu" : "Open menu"}
      >
        {isMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
      </button>
      
      {/* Desktop navigation */}
      <div className="hidden md:flex items-center gap-4">
        <NavLink
          to="/signup"
          className={({ isActive }) =>
            `px-4 py-2 rounded-md transition-colors ${
              isActive
                ? "bg-primary text-white"
                : "text-foreground hover:bg-primary/90 hover:text-white dark:text-white dark:hover:bg-primary/90"
            }`
          }
        >
          Signup
        </NavLink>
        <NavLink
          to="/login"
          className={({ isActive }) =>
            `px-4 py-2 rounded-md font-medium transition-colors ${
              isActive
                ? "bg-primary text-white"
                : "text-foreground hover:bg-primary/90 hover:text-white dark:text-white dark:hover:bg-primary/90"
            }`
          }
        >
          Login
        </NavLink>
        <ThemeToggle />
      </div>
      
      {/* Mobile navigation menu */}
      {isMenuOpen && (
        <div className="md:hidden absolute top-16 left-0 right-0 bg-background shadow-md z-50 border-t">
          <div className="flex flex-col p-4 gap-2">
            <NavLink
              to="/signup"
              className={({ isActive }) =>
                `px-4 py-3 rounded-md transition-colors ${
                  isActive
                    ? "bg-primary text-white"
                    : "text-foreground hover:bg-primary/90 hover:text-white dark:text-white dark:hover:bg-primary/90"
                }`
              }
              onClick={toggleMenu}
            >
              Signup
            </NavLink>
            <NavLink
              to="/login"
              className={({ isActive }) =>
                `px-4 py-3 rounded-md transition-colors ${
                  isActive
                    ? "bg-primary text-white"
                    : "text-foreground hover:bg-primary/90 hover:text-white dark:text-white dark:hover:bg-primary/90"
                }`
              }
              onClick={toggleMenu}
            >
              Login
            </NavLink>
            <div className="flex justify-start py-2">
              <ThemeToggle />
            </div>
          </div>
        </div>
      )}
    </nav>
  );
}

export default Navbar;
