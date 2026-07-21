import { createBrowserRouter } from "react-router-dom";

import AppLayout from "../components/layout/AppLayout";

import Home from "../pages/Home";
import Chat from "../pages/Chat";
import Upload from "../pages/Upload";
import About from "../pages/About";

export const router = createBrowserRouter([
  {
    path: "/",

    element: <AppLayout />,

    children: [
      {
        index: true,
        element: <Home />,
      },

      {
        path: "chat",
        element: <Chat />,
      },

      {
        path: "upload",
        element: <Upload />,
      },

      {
        path: "about",
        element: <About />,
      },
    ],
  },
]);
