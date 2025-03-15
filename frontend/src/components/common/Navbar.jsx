import { NavLink } from "react-router-dom";
import ThemeToggle from "../ThemeToggle";

function Navbar() {
  return (
    <nav className="flex justify-between items-center p-4 bg-background shadow-md">
      <div className="text-xl font-bold text-primary">Your Logo</div>
      <div className="flex items-center gap-4">
        <NavLink
          to="/signup"
          className={({ isActive }) =>
            `px-4 py-2 rounded-md transition-colors ${
              isActive
                ? "bg-primary text-white"
                : "text-foreground hover:bg-primary hover:text-white dark:text-white dark:hover:bg-primary"
            }`
          }
        >
          Signup
        </NavLink>
        <NavLink
          to="/login"
          className={({ isActive }) =>
            `px-4 py-2 rounded-md transition-colors ${
              isActive
                ? "bg-primary text-white"
                : "text-foreground hover:bg-primary hover:text-white dark:text-white dark:hover:bg-primary"
            }`
          }
        >
          Login
        </NavLink>
        <ThemeToggle />
      </div>
    </nav>
  );
}

export default Navbar;
