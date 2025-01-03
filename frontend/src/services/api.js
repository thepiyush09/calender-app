import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

export const getCompanies = async () => {
  const response = await axios.get(`${API_BASE_URL}/companies`);
  return response.data;
};

export const getCommunicationMethods = async () => {
  const response = await axios.get(`${API_BASE_URL}/communication-methods`);
  return response.data;
};
