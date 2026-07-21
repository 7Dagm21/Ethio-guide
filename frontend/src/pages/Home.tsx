import { Link } from "react-router-dom";
import { MessageSquare, UploadCloud, ArrowRight } from "lucide-react";

import "./Home.css";

export default function Home() {
  return (
    <div className="home-page page-container">
      {/* Hero Section */}
      <section className="hero glass">
        <h1>Navigate Ethiopian Government Services with AI</h1>

        <p>
          Your intelligent assistant for passport requirements, document
          validation, and seamless government service navigation.
        </p>

        <div className="hero-actions">
          <Link to="/chat" className="btn">
            <MessageSquare size={18} />
            Ask the Chatbot
          </Link>

          <Link to="/upload" className="btn secondary">
            <UploadCloud size={18} />
            Upload Document
          </Link>
        </div>
      </section>

      {/* Features */}
      <section className="features">
        <div className="feature-card glass">
          <div className="feature-icon-wrapper">
            <MessageSquare className="feature-icon" />
          </div>

          <h3>AI Chatbot</h3>

          <p>
            Instantly get answers about passport requirements, procedures, and
            government services using AI.
          </p>

          <Link to="/chat" className="feature-link">
            Try Chatbot
            <ArrowRight size={16} />
          </Link>
        </div>

        <div className="feature-card glass">
          <div className="feature-icon-wrapper">
            <UploadCloud className="feature-icon" />
          </div>

          <h3>Document Scanner</h3>

          <p>
            Upload documents and let AI extract information, validate
            requirements, and generate checklists.
          </p>

          <Link to="/upload" className="feature-link">
            Scan Document
            <ArrowRight size={16} />
          </Link>
        </div>
      </section>
    </div>
  );
}
