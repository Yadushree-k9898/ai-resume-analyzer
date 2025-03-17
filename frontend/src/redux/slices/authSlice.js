import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { signupUser as signupApi, loginUser as loginApi } from '@/api/authApi';

const API_URL = import.meta.env.VITE_API_URL;  // You have this set up correctly

// Async thunk for signup
export const signupUserThunk = createAsyncThunk(
  "auth/signupUser",  // Action name
  async (userData, { rejectWithValue }) => {
    try {
      const response = await signupApi(userData); // Correct API call
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response?.data?.detail || "Signup failed");
    }
  }
);

// Async thunk for login
export const loginUserThunk = createAsyncThunk(
  "auth/loginUser",  // Action name
  async (formData, { rejectWithValue }) => {
    try {
      const response = await loginApi(formData); // Correct API call
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response?.data?.detail || "Login failed");
    }
  }
);

const authSlice = createSlice({
  name: "auth",
  initialState: {
    user: null,
    token: localStorage.getItem("token") || null,
    isLoading: false,
    error: null,
  },
  reducers: {
    logout: (state) => {
      state.user = null;
      state.token = null;
      localStorage.removeItem("token");
    },
    clearError: (state) => {
      state.error = null;
    },
  },
  extraReducers: (builder) => {
    // Handle signup actions
    builder
      .addCase(signupUserThunk.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(signupUserThunk.fulfilled, (state, action) => {
        state.isLoading = false;
        state.user = action.payload;
      })
      .addCase(signupUserThunk.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload;
      });

    // Handle login actions
    builder
      .addCase(loginUserThunk.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(loginUserThunk.fulfilled, (state, action) => {
        state.isLoading = false;
        state.user = action.payload.user;
        state.token = action.payload.access_token;
      })
      .addCase(loginUserThunk.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload;
      });
  },
});

export const { logout, clearError } = authSlice.actions;
export default authSlice.reducer;
