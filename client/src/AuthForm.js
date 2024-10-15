import React, { useState } from 'react';
import './css/AuthForm.css'; // Импорт CSS

const AuthForm = () => {
  const [isLogin, setIsLogin] = useState(true); // Флаг для переключения между формами
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [username, setUsername] = useState('');

  const checkUser = async (arr) => {
    console.log(arr);
  };

  const registerUser = async (arr) => {
    console.log(arr);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (isLogin) {
      // Логика для авторизации
      checkUser([email, password]);
      console.log('Login with:', { email, password });
    } else {
      // Логика для регистрации
      registerUser([username, email, password]);
      console.log('Register with:', { email, password, username });
    }
  };

  return (
    <div className="auth-container">
      <h2>{isLogin ? 'Login' : 'Register'}</h2>
      <form onSubmit={handleSubmit}>
        {!isLogin && (
          <div>
            <label htmlFor="username">Username: </label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>
        )}
        <div>
          <label htmlFor="email">Email: </label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="password">Password: </label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">
          {isLogin ? 'Login' : 'Register'}
        </button>
      </form>
      <button onClick={() => setIsLogin(!isLogin)}>
        {isLogin ? 'Switch to Register' : 'Switch to Login'}
      </button>
    </div>
  );
};

export default AuthForm;