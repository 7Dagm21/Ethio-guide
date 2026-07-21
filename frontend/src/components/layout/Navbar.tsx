import { Link, useLocation } from "react-router-dom";
import { Home, MessageSquare, UploadCloud, Info, Moon, Sun } from "lucide-react";
import { useTheme } from "../../app/ThemeProvider";

import "./Navbar.css";

export default function Navbar() {
  const location = useLocation();
  const { theme, toggleTheme } = useTheme();

  const navLinks = [
    {
      path: "/",
      label: "Home",
      icon: Home,
    },
    {
      path: "/chat",
      label: "Chatbot",
      icon: MessageSquare,
    },
    {
      path: "/upload",
      label: "Upload",
      icon: UploadCloud,
    },
    {
      path: "/about",
      label: "About",
      icon: Info,
    },
  ];

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="logo">
          <div className="logo-box">EG</div>

          <span>Ethio Gov AI</span>
        </Link>

        <div className="nav-links">
          {navLinks.map(({ path, label, icon: Icon }) => (
            <Link
              key={path}
              to={path}
              className={`nav-link ${
                location.pathname === path ? "active" : ""
              }`}
            >
              <Icon size={18} />

              <span>{label}</span>
            </Link>
          ))}
          <button onClick={toggleTheme} className="theme-toggle" aria-label="Toggle Theme">
            {theme === "light" ? <Moon size={20} /> : <Sun size={20} />}
          </button>
        </div>
      </div>
    </nav>
  );
}
