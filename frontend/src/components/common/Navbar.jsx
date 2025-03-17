// import { NavLink } from "react-router-dom";
// import { FileSearch, Menu, X, Sparkles } from 'lucide-react';
// import { useState, useEffect } from "react";
// import ThemeToggle from "../ThemeToggle";
// import useAuth from "@/hooks/useAuth";

// function Navbar() {
//   const [isMenuOpen, setIsMenuOpen] = useState(false);
//   const [scrolled, setScrolled] = useState(false);
//   const { user, logout } = useAuth(); // Get user authentication state

//   // Scroll effect
//   useEffect(() => {
//     const handleScroll = () => setScrolled(window.scrollY > 20);
//     window.addEventListener("scroll", handleScroll);
//     return () => window.removeEventListener("scroll", handleScroll);
//   }, []);

//   const toggleMenu = () => setIsMenuOpen(!isMenuOpen);

//   return (
//     <nav className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${scrolled ? "py-2 bg-background/80 backdrop-blur-md shadow-lg" : "py-4 bg-background/60 backdrop-blur-sm"}`}>
//       <div className="container mx-auto px-4 flex justify-between items-center">
//         {/* Logo */}
//         <div className="flex items-center gap-2 text-xl font-bold">
//           <div className="relative">
//             <div className="absolute -inset-1 bg-gradient-to-r from-violet-600 to-indigo-600 rounded-full blur-sm opacity-70"></div>
//             <div className="relative bg-background dark:bg-gray-900 rounded-full p-1.5">
//               <FileSearch className="h-6 w-6 text-transparent bg-gradient-to-br from-violet-500 to-indigo-600 bg-clip-text" />
//             </div>
//           </div>
//           <span className="bg-gradient-to-r from-violet-600 via-indigo-600 to-purple-600 bg-clip-text text-transparent">
//             AnalyseAI
//           </span>
//           <Sparkles className="h-4 w-4 text-amber-400 animate-pulse" />
//         </div>

//         {/* Mobile Menu Button */}
//         <button className="md:hidden relative group" onClick={toggleMenu} aria-label={isMenuOpen ? "Close menu" : "Open menu"}>
//           <div className="absolute -inset-2 bg-gradient-to-r from-violet-600/20 to-indigo-600/20 rounded-full blur-sm opacity-0 group-hover:opacity-100 transition-opacity"></div>
//           {isMenuOpen ? <X className="h-6 w-6 text-indigo-600 dark:text-indigo-400 relative" /> : <Menu className="h-6 w-6 text-indigo-600 dark:text-indigo-400 relative" />}
//         </button>

//         {/* Desktop Navigation */}
//         <div className="hidden md:flex items-center gap-4">
//           {user ? (
//             <>
//               <NavLink to="/dashboard" className="nav-link">Dashboard</NavLink>
//               <NavLink to="/profile" className="nav-link">Profile</NavLink>
//               <button onClick={logout} className="nav-link text-red-500">Logout</button>
//             </>
//           ) : (
//             <>
//               <NavLink to="/signup" className="nav-link">Signup</NavLink>
//               <NavLink to="/login" className="nav-link">Login</NavLink>
//             </>
//           )}
//           <ThemeToggle />
//         </div>

//         {/* Mobile Menu */}
//         {isMenuOpen && (
//           <div className="md:hidden fixed top-[3.5rem] left-0 right-0 bg-background/95 backdrop-blur-md shadow-lg z-50 border-t border-indigo-100 dark:border-indigo-900 animate-in slide-in-from-top duration-300">
//             <div className="flex flex-col p-4 gap-3">
//               {user ? (
//                 <>
//                   <NavLink to="/dashboard" className="mobile-link" onClick={toggleMenu}>Dashboard</NavLink>
//                   <NavLink to="/profile" className="mobile-link" onClick={toggleMenu}>Profile</NavLink>
//                   <button onClick={logout} className="mobile-link text-red-500">Logout</button>
//                 </>
//               ) : (
//                 <>
//                   <NavLink to="/signup" className="mobile-link" onClick={toggleMenu}>Signup</NavLink>
//                   <NavLink to="/login" className="mobile-link" onClick={toggleMenu}>Login</NavLink>
//                 </>
//               )}
//               <ThemeToggle />
//             </div>
//           </div>
//         )}
//       </div>
//     </nav>
//   );
// }

// export default Navbar;



import { NavLink } from "react-router-dom";
import { useState, useEffect } from "react";
import { FileSearch, Menu, X, Sparkles } from "lucide-react";
import ThemeToggle from "../ThemeToggle";
import useAuth from "@/hooks/useAuth";

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const { user, logoutUser } = useAuth(); // Use the updated useAuth hook

  // Scroll effect
  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const toggleMenu = () => setIsMenuOpen(!isMenuOpen);

  return (
    <nav
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        scrolled
          ? "py-2 bg-background/80 backdrop-blur-md shadow-lg"
          : "py-4 bg-background/60 backdrop-blur-sm"
      }`}
    >
      <div className="container mx-auto px-4 flex justify-between items-center">
        {/* Logo */}
        <div className="flex items-center gap-2 text-xl font-bold">
          <div className="relative">
            <div className="absolute -inset-1 bg-gradient-to-r from-violet-600 to-indigo-600 rounded-full blur-sm opacity-70"></div>
            <div className="relative bg-background dark:bg-gray-900 rounded-full p-1.5">
              <FileSearch className="h-6 w-6 text-transparent bg-gradient-to-br from-violet-500 to-indigo-600 bg-clip-text" />
            </div>
          </div>
          <span className="bg-gradient-to-r from-violet-600 via-indigo-600 to-purple-600 bg-clip-text text-transparent">
            AnalyseAI
          </span>
          <Sparkles className="h-4 w-4 text-amber-400 animate-pulse" />
        </div>

        {/* Mobile Menu Button */}
        <button
          className="md:hidden relative group"
          onClick={toggleMenu}
          aria-label={isMenuOpen ? "Close menu" : "Open menu"}
        >
          {isMenuOpen ? (
            <X className="h-6 w-6 text-indigo-600 dark:text-indigo-400 relative" />
          ) : (
            <Menu className="h-6 w-6 text-indigo-600 dark:text-indigo-400 relative" />
          )}
        </button>

        {/* Desktop Navigation */}
        <div className="hidden md:flex items-center gap-4">
          {user ? (
            <>
              <NavLink to="/dashboard" className="nav-link">
                Dashboard
              </NavLink>
              <NavLink to="/profile" className="nav-link">
                Profile
              </NavLink>
              <button onClick={logoutUser} className="nav-link text-red-500">
                Logout
              </button>
            </>
          ) : (
            <>
              <NavLink to="/signup" className="nav-link">
                Signup
              </NavLink>
              <NavLink to="/login" className="nav-link">
                Login
              </NavLink>
            </>
          )}
          <ThemeToggle />
        </div>

        {/* Mobile Menu */}
        {isMenuOpen && (
          <div className="md:hidden fixed top-[3.5rem] left-0 right-0 bg-background/95 backdrop-blur-md shadow-lg z-50 border-t border-indigo-100 dark:border-indigo-900 animate-in slide-in-from-top duration-300">
            <div className="flex flex-col p-4 gap-3">
              {user ? (
                <>
                  <NavLink
                    to="/dashboard"
                    className="mobile-link"
                    onClick={toggleMenu}
                  >
                    Dashboard
                  </NavLink>
                  <NavLink
                    to="/profile"
                    className="mobile-link"
                    onClick={toggleMenu}
                  >
                    Profile
                  </NavLink>
                  <button
                    onClick={logoutUser}
                    className="mobile-link text-red-500"
                  >
                    Logout
                  </button>
                </>
              ) : (
                <>
                  <NavLink
                    to="/signup"
                    className="mobile-link"
                    onClick={toggleMenu}
                  >
                    Signup
                  </NavLink>
                  <NavLink
                    to="/login"
                    className="mobile-link"
                    onClick={toggleMenu}
                  >
                    Login
                  </NavLink>
                </>
              )}
              <ThemeToggle />
            </div>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
