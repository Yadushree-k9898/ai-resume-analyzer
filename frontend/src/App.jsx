import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Provider } from "react-redux";
import store from "./redux/store";
import MainLayout from "./layout/MainLayout";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Dashboard from "./pages/Dashboard";
import Home from "./pages/Home";
import NotFound from "./pages/NotFound";
import JobRecommendations from "./pages/JobRecommendations";
import Profile from "./pages/Dashboard";
import ResumeAnalyzer from "./pages/ResumeAnalysis";
import { ThemeProvider } from "./context/ThemeContext";
import JobMatches from "./components/dashboard/JobMatches";
import ResumeUpload from "./components/resume/ResumeUpload";

const router = createBrowserRouter([
  {
    path: "/",
    element: <MainLayout />,
    children: [
      { index: true, element: <Home /> },
      { path: "dashboard", element: <Dashboard /> },
      { path: "profile", element: <Profile /> },
      { path: "job-recommendations", element: <JobRecommendations /> },
      { path: "job-matches", element: <JobMatches /> },
      { path: "resume-analyzer", element: <ResumeAnalyzer/> },
      { path: "resume-upload", element: <ResumeUpload/> },
      { path: "*", element: <NotFound /> },
    ],
  },
  { path: "/login", element: <Login /> },
  { path: "/signup", element: <Signup /> },
  { path: "*", element: <NotFound /> },
]);

const App = () => {
  return (
    <Provider store={store}>
      <ThemeProvider>
        <RouterProvider router={router} />
      </ThemeProvider>
    </Provider>
  );
};

export default App;
