// API types based on OpenAPI spec
export interface User {
  id: number;
  username: string;
  email: string;
  score: number;
}

export interface LeaderboardEntry {
  rank: number;
  user: User;
}

export interface Token {
  access_token: string;
  token_type: string;
}

export interface LoginRequest {
  username: string;
  password: string;
}

export interface SignupRequest {
  username: string;
  password: string;
  email: string;
}

export interface AskRequest {
  question: string;
}

export interface AskResponse {
  response: string;
}

export interface UpdateProfileRequest {
  username?: string;
  email?: string;
  score?: number;
}

// Base URL from OpenAPI spec
const BASE_URL = 'http://localhost:8000/api';

// Helper function to get auth headers
const getAuthHeaders = (): HeadersInit => {
  const token = localStorage.getItem('token');
  return token ? { Authorization: `Bearer ${token}` } : {};
};

// Helper function to handle API responses
const handleResponse = async <T>(response: Response): Promise<T> => {
  if (!response.ok) {
    const error = await response.text();
    throw new Error(`API Error: ${response.status} - ${error}`);
  }
  return response.json();
};

// API functions
export const api = {
  // Authentication
  async login(credentials: LoginRequest): Promise<Token> {
    const response = await fetch(`${BASE_URL}/auth/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(credentials),
    });
    const token = await handleResponse<Token>(response);
    localStorage.setItem('token', token.access_token);
    return token;
  },

  async signup(userData: SignupRequest): Promise<Token> {
    const response = await fetch(`${BASE_URL}/auth/signup`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    });
    const token = await handleResponse<Token>(response);
    localStorage.setItem('token', token.access_token);
    return token;
  },

  // AI
  async askAI(question: AskRequest): Promise<AskResponse> {
    const response = await fetch(`${BASE_URL}/ai/ask`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...getAuthHeaders(),
      },
      body: JSON.stringify(question),
    });
    return handleResponse<AskResponse>(response);
  },

  // Leaderboard
  async getLeaderboard(): Promise<LeaderboardEntry[]> {
    const response = await fetch(`${BASE_URL}/leaderboard/`, {
      method: 'GET',
      headers: getAuthHeaders(),
    });
    return handleResponse<LeaderboardEntry[]>(response);
  },

  // User Profile
  async getProfile(): Promise<User> {
    const response = await fetch(`${BASE_URL}/user/profile`, {
      method: 'GET',
      headers: getAuthHeaders(),
    });
    return handleResponse<User>(response);
  },

  async updateProfile(updates: UpdateProfileRequest): Promise<User> {
    const response = await fetch(`${BASE_URL}/user/profile`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        ...getAuthHeaders(),
      },
      body: JSON.stringify(updates),
    });
    return handleResponse<User>(response);
  },

  // Logout
  logout(): void {
    localStorage.removeItem('token');
  },

  // Check if authenticated
  isAuthenticated(): boolean {
    return !!localStorage.getItem('token');
  },
};