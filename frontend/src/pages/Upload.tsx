import { UploadCloud, FileText, ShieldCheck } from "lucide-react";

import "./Upload.css";

export default function Upload() {
  return (
    <div className="upload-page">
      <section className="upload-hero glass">
        <div className="upload-icon">
          <UploadCloud size={50} />
        </div>

        <h1>Upload Government Documents</h1>

        <p>
          Upload your passport, ID, or supporting documents. Ethio Gov AI will
          analyze and guide you through the process.
        </p>

        <button className="btn">Choose Document</button>
      </section>

      <section className="upload-features">
        <div className="feature-card glass">
          <FileText size={35} />

          <h3>Document Analysis</h3>

          <p>
            Extract important information from your documents automatically.
          </p>
        </div>

        <div className="feature-card glass">
          <ShieldCheck size={35} />

          <h3>Secure Processing</h3>

          <p>Your documents are processed securely.</p>
        </div>
      </section>
    </div>
  );
}
