import React, { createContext, useState, useEffect } from 'react';

// Create context
export const DashboardContext = createContext();

// Dashboard provider component
export const DashboardProvider = ({ children }) => {
  const [dashboardData, setDashboardData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDashboardData = async () => {
      try {
        const response = await fetch('http://localhost:8000/dashboard/', {
          method: 'GET',
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`,
          },
        });
        const data = await response.json();
        setDashboardData(data);
      } catch (error) {
        console.error('Failed to fetch dashboard data', error);
      } finally {
        setLoading(false);
      }
    };
    fetchDashboardData();
  }, []);

  const updateDashboardData = (newData) => {
    setDashboardData(newData);
  };

  return (
    <DashboardContext.Provider value={{ dashboardData, loading, updateDashboardData }}>
      {children}
    </DashboardContext.Provider>
  );
};
