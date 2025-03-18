import { useEffect, useState } from "react";
import axios from "axios";
import { Sparkles, Mail, Phone, MapPin, Calendar, Briefcase, Globe, User } from "lucide-react";

const Profile = () => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [editMode, setEditMode] = useState(false);
  const [formData, setFormData] = useState({});

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const token = localStorage.getItem("token");
        const response = await axios.get("http://localhost:8000/auth/me/", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        setUser(response.data);
        setFormData(response.data);
      } catch (err) {
        setError("Failed to fetch user data", err);
      } finally {
        setLoading(false);
      }
    };
    fetchUser();
  }, []);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleUpdate = async () => {
    try {
      const token = localStorage.getItem("token");
      await axios.put("http://localhost:8000/auth/update/", formData, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setUser(formData);
      setEditMode(false);
    } catch (err) {
      setError("Failed to update profile", err);
    }
  };

  const handleDelete = async () => {
    if (!window.confirm("Are you sure you want to delete your account?")) return;

    try {
      const token = localStorage.getItem("token");
      await axios.delete("http://localhost:8000/auth/delete/", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      localStorage.removeItem("token");
      window.location.href = "/login";
    } catch (err) {
      setError("Failed to delete account", err);
    }
  };

  const getFieldIcon = (key) => {
    switch (key) {
      case "email":
        return <Mail className="h-4 w-4 text-indigo-500" />;
      case "phone":
      case "phone_number":
        return <Phone className="h-4 w-4 text-indigo-500" />;
      case "address":
        return <MapPin className="h-4 w-4 text-indigo-500" />;
      case "birth_date":
      case "date_joined":
        return <Calendar className="h-4 w-4 text-indigo-500" />;
      case "job_title":
        return <Briefcase className="h-4 w-4 text-indigo-500" />;
      case "website":
      case "linkedin":
        return <Globe className="h-4 w-4 text-indigo-500" />;
      default:
        return <User className="h-4 w-4 text-indigo-500" />;
    }
  };

  if (loading) return <p className="text-center text-gray-500">Loading...</p>;
  if (error) return <p className="text-center text-red-500">{error}</p>;

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-50 dark:bg-gray-950 px-4">
      <div className="w-full max-w-4xl relative z-10 p-6 md:p-8 rounded-xl shadow-lg border border-indigo-100 dark:border-indigo-900 bg-white dark:bg-gray-900 overflow-hidden">
        <div className="relative flex items-center justify-center md:justify-start gap-2 mb-8">
          <h2 className="text-2xl font-bold bg-gradient-to-r from-violet-600 via-indigo-600 to-purple-600 bg-clip-text text-transparent">
            Profile
          </h2>
          <Sparkles className="h-5 w-5 text-amber-400" />
        </div>
        <div className="relative">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-6">
            {Object.entries(user).map(([key, value]) =>
              key !== "password" ? (
                <div key={key} className="flex items-start space-x-3">
                  <div className="mt-1">{getFieldIcon(key)}</div>
                  <div className="flex-1 min-w-0">
                    <label className="text-sm font-semibold capitalize text-gray-700 dark:text-gray-300">
                      {key.replace(/_/g, " ")}
                    </label>
                    {editMode ? (
                      <input
                        type={key.includes("date") ? "date" : key === "email" ? "email" : "text"}
                        name={key}
                        value={formData[key] || ""}
                        onChange={handleChange}
                        className="w-full border rounded-md p-2 mt-1 dark:bg-gray-800 dark:text-white focus:outline-none focus:ring-2 focus:ring-indigo-500"
                      />
                    ) : (
                      <p className="text-gray-800 dark:text-gray-300 mt-1 truncate">
                        {value || "N/A"}
                      </p>
                    )}
                  </div>
                </div>
              ) : null
            )}
          </div>
        </div>
        <div className="relative mt-8 flex justify-end space-x-4">
          {editMode ? (
            <button
              onClick={handleUpdate}
              className="px-6 py-2 bg-green-500 text-white rounded-md hover:bg-green-600 transition text-center"
            >
              Save Changes
            </button>
          ) : (
            <button
              onClick={() => setEditMode(true)}
              className="px-6 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 transition text-center"
            >
              Edit Profile
            </button>
          )}
          <button
            onClick={handleDelete}
            className="px-6 py-2 bg-red-500 text-white rounded-md hover:bg-red-600 transition text-center"
          >
            Delete Account
          </button>
        </div>
      </div>
    </div>
  );
};

export default Profile;
