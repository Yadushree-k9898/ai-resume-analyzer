import { configureStore } from '@reduxjs/toolkit';
import authReducer from '@/redux/slices/authSlice'; // Importing the authSlice

const store = configureStore({
  reducer: {
    auth: authReducer,  // Ensure the reducer is correctly mapped
  },
});

export default store;
