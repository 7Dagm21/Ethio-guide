import { useState, useEffect, useRef } from "react";

import { Send, Loader2, Bot, User } from "lucide-react";

import { chatApi } from "../services/api";

import "./Chat.css";

interface Message {
  id: number;

  text: string;

  sender: "bot" | "user";

  chunks?: number;
}

export default function Chat() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: 1,

      text: "Hello! I am your Ethio Gov AI assistant. How can I help you with your government service requirements?",

      sender: "bot",
    },
  ]);

  const [input, setInput] = useState("");

  const [isTyping, setIsTyping] = useState(false);

  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isTyping]);

  const handleSend = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!input.trim()) return;

    const userMessage: Message = {
      id: Date.now(),

      text: input,

      sender: "user",
    };

    setMessages((prev) => [...prev, userMessage]);

    setInput("");

    setIsTyping(true);

    try {
      const response = await chatApi.sendMessage(userMessage.text);

      setMessages((prev) => [
        ...prev,

        {
          id: Date.now(),

          text: response.answer,

          sender: "bot",

          chunks: response.sources?.length,
        },
      ]);
    } catch (error) {
      console.error("Chat error:", error);

      setMessages((prev) => [
        ...prev,

        {
          id: Date.now(),

          text: "Sorry, I couldn't process your request.",

          sender: "bot",
        },
      ]);
    } finally {
      setIsTyping(false);
    }
  };

  return (
    <div className="chat-page page-container">
      <div className="chat-header glass">
        <div>
          <h2>AI Assistant</h2>

          <p>Online | Document RAG Pipeline Active</p>
        </div>
      </div>

      <div className="chat-container glass">
        <div className="chat-messages">
          {messages.map((msg) => (
            <div key={msg.id} className={`message-wrapper ${msg.sender}`}>
              <div className="message-avatar">
                {msg.sender === "bot" ? <Bot size={20} /> : <User size={20} />}
              </div>

              <div className="message-content">
                <div className="message-bubble">{msg.text}</div>

                {msg.chunks && (
                  <div className="message-meta">
                    Retrieved from {msg.chunks} sources
                  </div>
                )}
              </div>
            </div>
          ))}

          {isTyping && (
            <div className="message-wrapper bot">
              <div className="message-avatar">
                <Bot size={20} />
              </div>

              <div className="message-bubble typing-indicator">
                <Loader2 className="spinner" size={16} />
                Retrieving information...
              </div>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>

        <form className="chat-input-form" onSubmit={handleSend}>
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask about passport requirements..."
            disabled={isTyping}
          />

          <button className="btn send-btn" disabled={isTyping || !input.trim()}>
            <Send size={18} />
          </button>
        </form>
      </div>
    </div>
  );
}
