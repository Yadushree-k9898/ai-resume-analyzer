// useAuth.js
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { loginUserThunk, signupUserThunk, logout, clearError } from "@/redux/slices/authSlice";

// Custom hook for authentication
const useAuth = () => {
  const dispatch = useDispatch();
  const { user, token, isLoading, error } = useSelector((state) => state.auth);

  const login = (formData) => {
    dispatch(loginUserThunk(formData)); // Trigger login
  };

  const signup = (userData) => {
    dispatch(signupUserThunk(userData)); // Trigger signup
  };

  const logoutUser = () => {
    dispatch(logout()); // Trigger logout
  };

  // Clear error message when component unmounts
  useEffect(() => {
    return () => {
      dispatch(clearError());
    };
  }, [dispatch]);

  return {
    user,
    token,
    isLoading,
    error,
    login,
    signup,
    logoutUser,
  };
};

export default useAuth;
