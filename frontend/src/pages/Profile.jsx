import { useEffect, useState } from "react";
import { Avatar, AvatarImage, AvatarFallback } from "@/components/ui/avatar";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { Mail, Phone, MapPin, Calendar } from "lucide-react";

const Profile = () => {
    const API_URL = import.meta.env.VITE_API_URL;
  const [ProfileData, setProfileData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`${API_URL}/auth/me/`); // Replace with actual API endpoint
        const data = await response.json();
        setProfileData(data);
      } catch (error) {
        console.error("Error fetching profile data:", error);
      }
    };

    fetchData();
  }, []);

  if (!ProfileData) return <p>Loading...</p>;

  return (
    <Card className="md:col-span-1 bg-white/50 dark:bg-gray-900/50 backdrop-blur-sm border-indigo-100/30 dark:border-indigo-800/30 shadow-md">
      <CardContent className="p-6 flex flex-col items-center">
        <div className="relative mb-4">
          <div className="absolute -inset-1 bg-gradient-to-r from-violet-600 to-indigo-600 rounded-full blur-sm opacity-70"></div>
          <Avatar className="h-24 w-24 border-2 border-white dark:border-gray-800">
            <AvatarImage src="/placeholder.svg?height=96&width=96" alt={ProfileData.name} />
            <AvatarFallback className="bg-gradient-to-br from-violet-500 to-indigo-600 text-white text-xl">
              {ProfileData.name
                .split(" ")
                .map((n) => n[0])
                .join("")}
            </AvatarFallback>
          </Avatar>
        </div>

        <h2 className="text-xl font-bold bg-gradient-to-r from-violet-600 to-indigo-600 bg-clip-text text-transparent mb-1">
          {ProfileData.name}
        </h2>

        <Badge className="mb-4 bg-indigo-100 text-indigo-700 dark:bg-indigo-900/30 dark:text-indigo-300 border-indigo-200 dark:border-indigo-800">
          {ProfileData.bio}
        </Badge>

        <div className="w-full space-y-3 text-sm">
          <div className="flex items-center">
            <Mail className="h-4 w-4 text-indigo-500 mr-2" />
            <span className="text-muted-foreground">{ProfileData.email}</span>
          </div>
          <div className="flex items-center">
            <Phone className="h-4 w-4 text-indigo-500 mr-2" />
            <span className="text-muted-foreground">{ProfileData.phone}</span>
          </div>
          <div className="flex items-center">
            <MapPin className="h-4 w-4 text-indigo-500 mr-2" />
            <span className="text-muted-foreground">{ProfileData.location}</span>
          </div>
          <div className="flex items-center">
            <Calendar className="h-4 w-4 text-indigo-500 mr-2" />
            <span className="text-muted-foreground">Member since {ProfileData.joinDate}</span>
          </div>
        </div>
      </CardContent>
    </Card>
  );
};

export default Profile;
