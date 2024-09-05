
import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import io from 'socket.io-client';

const ChatContainer = styled.div`
  display: flex;
  flex-direction: column;
  height: 100%;
  background-color: ${props => props.theme.secondary};
  color: ${props => props.theme.text};
`;

const MessageList = styled.ul`
  list-style-type: none;
  padding: 20px;
  overflow-y: auto;
  flex-grow: 1;
`;

const MessageItem = styled.li`
  margin-bottom: 10px;
`;

const InputContainer = styled.div`
  display: flex;
  padding: 20px;
`;

const Input = styled.input`
  flex-grow: 1;
  padding: 10px;
  font-size: 16px;
  border: none;
  border-radius: 5px 0 0 5px;
`;

const SendButton = styled.button`
  padding: 10px 20px;
  font-size: 16px;
  background-color: ${props => props.theme.primary};
  color: white;
  border: none;
  border-radius: 0 5px 5px 0;
  cursor: pointer;
`;

function ChatWindow({ theme }) {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    const newSocket = io('http://localhost:3001');
    setSocket(newSocket);

    newSocket.on('chat message', (msg) => {
      setMessages(prevMessages => [...prevMessages, msg]);
    });

    return () => newSocket.close();
  }, []);

  const sendMessage = () => {
    if (inputValue && socket) {
      socket.emit('chat message', inputValue);
      setInputValue('');
    }
  };

  return (
    <ChatContainer theme={theme}>
      <MessageList>
        {messages.map((msg, index) => (
          <MessageItem key={index}>{msg}</MessageItem>
        ))}
      </MessageList>
      <InputContainer>
        <Input
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
          placeholder="Type a message..."
        />
        <SendButton onClick={sendMessage} theme={theme}>Send</SendButton>
      </InputContainer>
    </ChatContainer>
  );
}

export default ChatWindow;
