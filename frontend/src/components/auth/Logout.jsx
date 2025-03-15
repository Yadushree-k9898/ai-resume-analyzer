import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { LogOut } from "lucide-react";

const Logout = () => {
  const navigate = useNavigate();
  
  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };
  
  return (
    <Button 
      variant="ghost" 
      className="flex items-center gap-2 text-muted-foreground hover:text-foreground transition-colors"
      onClick={handleLogout}
    >
      <LogOut size={16} />
      <span>Logout</span>
    </Button>
  );
};

export default Logout;