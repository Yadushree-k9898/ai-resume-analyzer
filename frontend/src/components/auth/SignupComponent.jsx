// import { useState } from "react";
// import { useNavigate } from "react-router-dom";
// import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
// import { Input } from "@/components/ui/input";
// import { Button } from "@/components/ui/button";
// import { Label } from "@/components/ui/label";
// import { Alert, AlertDescription } from "@/components/ui/alert";
// import { ExclamationTriangleIcon } from "@radix-ui/react-icons";

// const SignupComponent = () => {
//   const navigate = useNavigate();
//   const [formData, setFormData] = useState({
//     full_name: "",
//     email: "",
//     password: "",
//     phone_number: "",
//   });
//   const [error, setError] = useState(null);
//   const [isLoading, setIsLoading] = useState(false);

//   const handleChange = (e) => {
//     setFormData({ ...formData, [e.target.name]: e.target.value });
//   };

//   const handleSignup = async (e) => {
//     e.preventDefault();
//     setError(null);
//     setIsLoading(true);

//     try {
//       const response = await fetch(`${import.meta.env.VITE_API_URL}/auth/register/`, {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify(formData),
//       });

//       const data = await response.json();
//       if (!response.ok) throw new Error(data.detail);

//       navigate("/login", { state: { message: "Account created successfully! Please log in." } });
//     } catch (err) {
//       setError(err.message);
//     } finally {
//       setIsLoading(false);
//     }
//   };

//   return (
//     <div className="flex justify-center items-center min-h-screen bg-background p-4">
//       <Card className="w-full max-w-md shadow-lg border-border">
//         <CardHeader className="space-y-1">
//           <CardTitle className="text-2xl font-bold text-center">Create an account</CardTitle>
//           <CardDescription className="text-center">
//             Enter your information to get started
//           </CardDescription>
//         </CardHeader>
//         <CardContent>
//           <form onSubmit={handleSignup} className="space-y-4">
//             <div className="space-y-2">
//               <Label htmlFor="full_name">Full Name</Label>
//               <Input
//                 id="full_name"
//                 type="text"
//                 name="full_name"
//                 placeholder="John Doe"
//                 onChange={handleChange}
//                 required
//                 className="bg-background"
//               />
//             </div>
//             <div className="space-y-2">
//               <Label htmlFor="email">Email</Label>
//               <Input
//                 id="email"
//                 type="email"
//                 name="email"
//                 placeholder="name@example.com"
//                 onChange={handleChange}
//                 required
//                 className="bg-background"
//               />
//             </div>
//             <div className="space-y-2">
//               <Label htmlFor="password">Password</Label>
//               <Input
//                 id="password"
//                 type="password"
//                 name="password"
//                 placeholder="••••••••"
//                 onChange={handleChange}
//                 required
//                 className="bg-background"
//               />
//             </div>
//             <div className="space-y-2">
//               <Label htmlFor="phone_number">Phone Number</Label>
//               <Input
//                 id="phone_number"
//                 type="text"
//                 name="phone_number"
//                 placeholder="+1 (555) 123-4567"
//                 onChange={handleChange}
//                 className="bg-background"
//               />
//             </div>

//             {error && (
//               <Alert variant="destructive" className="border-destructive/50 text-destructive dark:border-destructive dark:text-destructive">
//                 <ExclamationTriangleIcon className="h-4 w-4" />
//                 <AlertDescription>{error}</AlertDescription>
//               </Alert>
//             )}

//             <Button type="submit" className="w-full" disabled={isLoading}>
//               {isLoading ? "Creating account..." : "Create account"}
//             </Button>
//           </form>
//         </CardContent>
//         <CardFooter className="flex flex-col space-y-4 mt-2">
//           <div className="text-sm text-center text-muted-foreground">
//             Already have an account?{" "}
//             <Button variant="link" className="p-0 h-auto font-normal" onClick={() => navigate("/login")}>
//               Sign in
//             </Button>
//           </div>
//         </CardFooter>
//       </Card>
//     </div>
//   );
// };

// export default SignupComponent;



import { useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { ExclamationTriangleIcon } from "@radix-ui/react-icons";

const SignupComponent = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    full_name: "",
    email: "",
    password: "",
    phone_number: "",
  });
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSignup = async (e) => {
    e.preventDefault();
    setError(null);
    setIsLoading(true);

    try {
      const response = await fetch(
        `${import.meta.env.VITE_API_URL}/auth/register/`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            full_name: formData.full_name.trim(),
            email: formData.email.trim(),
            password: formData.password,
            phone_number: formData.phone_number.trim() || null,
          }),
        }
      );

      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || "Unknown error");

      navigate("/login", {
        state: { message: "Account created successfully! Please log in." },
      });
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-background p-4">
      <Card className="w-full max-w-md shadow-lg border-border">
        <CardHeader className="space-y-1">
          <CardTitle className="text-2xl font-bold text-center">
            Create an account
          </CardTitle>
          <CardDescription className="text-center">
            Enter your information to get started
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSignup} className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="full_name">Full Name</Label>
              <Input
                id="full_name"
                type="text"
                name="full_name"
                placeholder="John Doe"
                onChange={handleChange}
                required
                className="bg-background"
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="email">Email</Label>
              <Input
                id="email"
                type="email"
                name="email"
                placeholder="name@example.com"
                onChange={handleChange}
                required
                className="bg-background"
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="password">Password</Label>
              <Input
                id="password"
                type="password"
                name="password"
                placeholder="••••••••"
                onChange={handleChange}
                required
                className="bg-background"
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="phone_number">Phone Number (Optional)</Label>
              <Input
                id="phone_number"
                type="text"
                name="phone_number"
                placeholder="+1 (555) 123-4567"
                onChange={handleChange}
                className="bg-background"
              />
            </div>

            {error && (
              <Alert
                variant="destructive"
                className="border-destructive/50 text-destructive dark:border-destructive dark:text-destructive"
              >
                <ExclamationTriangleIcon className="h-4 w-4" />
                <AlertDescription>{error}</AlertDescription>
              </Alert>
            )}

            <Button
              type="submit"
              className="w-full bg-primary hover:bg-primary/90 text-white"
              disabled={isLoading}
            >
              {isLoading ? "Creating account..." : "Create account"}
            </Button>
          </form>
        </CardContent>
        <CardFooter className="flex flex-col space-y-4 mt-2">
          <div className="text-sm text-center text-muted-foreground">
            Already have an account?{" "}
            <Button
              variant="link"
              className="p-0 h-auto font-normal text-primary hover:text-primary/80"
              onClick={() => navigate("/login")}
            >
              Sign in
            </Button>
          </div>
        </CardFooter>
      </Card>
    </div>
  );
};

export default SignupComponent;
