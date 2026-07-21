import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",

  headers: {
    "Content-Type": "application/json",
  },
});

export const chatApi = {
  sendMessage: async (question: string) => {
    const response = await api.post("/chat", {
      question,
    });

    return response.data;
  },
};

export const scannerApi = {
  processDocument: async (file: File) => {
    const formData = new FormData();

    formData.append("file", file);

    const response = await api.post(
      "/upload",

      formData,

      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      },
    );

    return response.data;
  },
};

export default api;
