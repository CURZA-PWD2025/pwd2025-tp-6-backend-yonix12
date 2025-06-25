import axios from 'axios';

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});

export interface Recurso {
  id?: number;
  [key: string]: any;
}

const ApiService = {
  getAll: async <T extends Recurso>(endpoint: string): Promise<T[]> => {
    try {
      const response = await apiClient.get<T[]>(`/${endpoint}`);
      return response.data;
    } catch (error) {
      console.error(`Error fetching all ${endpoint}:`, error);
      throw error;
    }
  },

  getOne: async <T extends Recurso>(endpoint: string, id: number): Promise<T> => {
    try {
      const response = await apiClient.get<T>(`/${endpoint}/${id}`);
      return response.data;
    } catch (error) {
      console.error(`Error fetching ${endpoint} with id ${id}:`, error);
      throw error;
    }
  },

  create: async <T extends Recurso>(endpoint: string, data: Omit<T, 'id'>): Promise<T> => {
    try {
      const response = await apiClient.post<T>(`/${endpoint}`, data);
      return response.data;
    } catch (error) {
      console.error(`Error creating ${endpoint}:`, error);
      throw error;
    }
  },

  update: async <T extends Recurso>(endpoint: string, id: number, data: Partial<T>): Promise<T> => {
    try {
      const response = await apiClient.put<T>(`/${endpoint}/${id}`, data);
      return response.data;
    } catch (error) {
      console.error(`Error updating ${endpoint} with id ${id}:`, error);
      throw error;
    }
  },

  destroy: async (endpoint: string, id: number): Promise<void> => {
    try {
      await apiClient.delete(`/${endpoint}/${id}`);
    } catch (error) {
      console.error(`Error deleting ${endpoint} with id ${id}:`, error);
      throw error;
    }
  }
};

export default ApiService;
