import axiosInstance from './axiosInstance';

// Signup API call
export const signupUser = (userData) => {
  return axiosInstance.post("/auth/register/", userData);
};

// Login API call
export const loginUser = (formData) => {
  return axiosInstance.post("/auth/login/", formData);
};
