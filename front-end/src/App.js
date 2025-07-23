import React, { useState, useEffect, useRef } from 'react';
import { io } from 'socket.io-client';
import './App.css'; // Optional: For custom styling

function App() {
    const [socket, setSocket] = useState(null);
    const [messages, setMessages] = useState([]);
    const [inputValue, setInputValue] = useState('');
    const MAX_MESSAGES = 2000; // Maximum number of messages to keep
    const messagesEndRef = useRef(null); // Reference for the messages container

    const connectSocket = () => {
        if (socket) {
            alert("Already connected to the WebSocket."); // Alert if already connected
            return; // Prevent creating a new connection
        }

        const newSocket = io('http://localhost:5000'); // Adjust the URL if needed
        setSocket(newSocket);

        newSocket.on('new_message', (message) => {
            addMessage(message);
        });

        newSocket.on('server_response', (response) => {
            addMessage(response);
        });
    };

    const disconnectSocket = () => {
        if (socket) {
            socket.disconnect();
            setSocket(null);
            // Messages will not be cleared on disconnect
        }
    };

    const addMessage = (message) => {
        setMessages((prevMessages) => {
            const updatedMessages = [...prevMessages, message];
            // Keep only the most recent MAX_MESSAGES
            return updatedMessages.slice(-MAX_MESSAGES);
        });
    };

    const sendMessage = () => {
        if (inputValue && socket) {
            socket.emit('client_message', inputValue);
            setInputValue(''); // Clear the input field
        }
    };

    const getADBVersion = () => {
        if (socket) {
            socket.emit('adb_version_check'); // Changed to emit adb_version_check
        } else {
            alert("Please connect to the WebSocket first."); // Alert if not connected
        }
    };

    const getDCMVersion = () => {
        if (socket) {
            socket.emit('dcm_version_check'); // Send the dcm_version_check message
        } else {
            alert("Please connect to the WebSocket first."); // Alert if not connected
        }
    };

    // Button styles
    const connectButtonStyle = {
        backgroundColor: socket ? '#005f00' : '#90ee90', // Darker green if connected, light green if not
        color: socket ? 'white' : 'black', // White text if connected
        padding: '10px 20px',
        marginRight: '10px',
        border: 'none',
        borderRadius: '5px',
        cursor: 'pointer',
    };

    const disconnectButtonStyle = {
        backgroundColor: socket ? '#b22222' : '#ffcccb', // Darker red if connected, light red if not
        color: socket ? 'white' : 'black', // White text if connected
        padding: '10px 20px',
        marginRight: '10px',
        border: 'none',
        borderRadius: '5px',
        cursor: 'pointer',
    };

    // Scroll to bottom effect
    useEffect(() => {
        const scrollToBottom = () => {
            if (messagesEndRef.current) {
                const { scrollHeight, clientHeight } = messagesEndRef.current;
                const isAtBottom = scrollHeight <= clientHeight + messagesEndRef.current.scrollTop + 1;
                if (isAtBottom) {
                    messagesEndRef.current.scrollTop = scrollHeight;
                }
            }
        };

        scrollToBottom();
    }, [messages]); // Run effect when messages change

    return (
        <div style={{ textAlign: 'center', padding: '20px' }}>
            <h1>Real-Time Messages</h1>
            <div style={{ marginBottom: '20px' }}>
                <button onClick={connectSocket} style={connectButtonStyle}>
                    {socket ? 'Connected' : 'Connect'}
                </button>
                <button onClick={disconnectSocket} style={disconnectButtonStyle}>
                    {socket ? 'Disconnect' : 'Disconnected'}
                </button>
                <button onClick={getADBVersion} style={{ padding: '10px 20px', marginRight: '10px' }}>
                    Get ADB Version
                </button>
                <button onClick={getDCMVersion} style={{ padding: '10px 20px' }}>
                    Get DCM Version
                </button>
            </div>
            <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '20px' }}>
                <input
                    type="text"
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)}
                    placeholder="Type a message"
                    style={{ marginRight: '10px', padding: '10px', width: '300px' }}
                />
                <button onClick={sendMessage} style={{ padding: '10px 20px' }}>
                    Send
                </button>
            </div>
            <div
                ref={messagesEndRef} // Attach the ref to the messages container
                style={{
                    border: '1px solid #ccc',
                    borderRadius: '5px',
                    padding: '10px',
                    width: '50%', // Adjusted width for a narrower window
                    height: '300px',
                    overflowY: 'scroll',
                    margin: '0 auto',
                    backgroundColor: '#f9f9f9',
                    textAlign: 'left', // Left justify text
                }}
            >
                <h3>Messages:</h3>
                <ul style={{ listStyleType: 'none', padding: 0 }}>
                    {messages.map((msg, index) => (
                        <li key={index} style={{ color: msg.color || 'black' }}>
                            {msg.text}
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default App;