// APP.JS
// Вход регистрация

import React, { useState } from "react";
import LoginPage from "./LoginPage";
import RegistrationPage from "./RegistrationPage";
import "./styles.css";

function App() {
  const [isLoginPage, setIsLoginPage] = useState(true); // Управляем состоянием страницы

  return (
    <div className="App">
      {isLoginPage ? (
        <LoginPage onSwitchPage={() => setIsLoginPage(false)} />
      ) : (
        <RegistrationPage onSwitchPage={() => setIsLoginPage(true)} />
      )}
    </div>
  );
}

export default App;


// LoginPage.js

import React from "react";

function LoginPage({ onSwitchPage }) {
  return (
    <div className="page login">
      <header>
        <div className="header-content">
          <img src="logo.png" alt="DreamKeys Logo" className="logo" />
          <a href="#" className="back-btn" onClick={onSwitchPage}>
            ← назад
          </a>
        </div>
      </header>
      <main className="form-container">
        <div className="form-box">
          <h2>Вхід</h2>
          <form action="#">
            <input type="text" name="login" placeholder="Логін" required />
            <input
              type="password"
              name="password"
              placeholder="Пароль"
              required
            />
            <button type="submit" className="btn-primary">
              Увійти
            </button>
          </form>
          <p>
            <a href="#" onClick={onSwitchPage}>
              немає аккаунту? реєстрація
            </a>
          </p>
        </div>
        <div className="support">
          <h3>Тех. підтримка</h3>
          <div className="support-numbers">
            <span className="number red">099 *** ****</span>
            <span className="number green">093 *** ****</span>
            <span className="number yellow">096 *** ****</span>
          </div>
        </div>
      </main>
    </div>
  );
}

export default LoginPage;


// RegistrationPage.js

import React from "react";

function RegistrationPage({ onSwitchPage }) {
  return (
    <div className="page registration">
      <header>
        <div className="header-content">
          <img src="logo.png" alt="DreamKeys Logo" className="logo" />
          <a href="#" className="back-btn" onClick={onSwitchPage}>
            ← назад
          </a>
        </div>
      </header>
      <main className="form-container">
        <div className="form-box">
          <h2>Реєстрація</h2>
          <form action="#">
            <input type="text" name="login" placeholder="Логін" required />
            <input type="email" name="email" placeholder="E-mail" required />
            <input
              type="password"
              name="password"
              placeholder="Пароль"
              required
            />
            <button type="submit" className="btn-primary">
              Увійти
            </button>
          </form>
          <p>
            <a href="#" onClick={onSwitchPage}>
              є акаунт? вхід
            </a>
          </p>
        </div>
        <div className="support">
          <h3>Тех. підтримка</h3>
          <div className="support-numbers">
            <span className="number red">039 *** ****</span>
            <span className="number green">093 *** ****</span>
            <span className="number yellow">096 *** ****</span>
          </div>
        </div>
      </main>
    </div>
  );
}

export default RegistrationPage;





// Установка зависимостей
// npx create-react-app dreamkeys
// cd dreamkeys


// Личный кабинет

// APP.js

import React from 'react';
import Header from './Header';
import AdsSection from './AdsSection';
import MobileMenu from './MobileMenu';
import './styles.css';

function App() {
  return (
    <div className="App">
      <Header />
      <main>
        <AdsSection />
      </main>
      <MobileMenu />
    </div>
  );
}

export default App;


// Header.js

import React from 'react';

function Header() {
  return (
    <header>
      <div className="container">
        <div className="logo">DreamKeys</div>
        <div className="user-menu">
          {/* Замените путь на реальное изображение */}
          <img className="user-icon" src="path/to/your/user-image.jpg" alt="User Icon" />
          <span>(Ім'я користувача)</span>
        </div>
      </div>
    </header>
  );
}

export default Header;


// AdsSection.js

import React from 'react';

function AdsSection() {
  return (
    <div className="ads-section">
      <h2>Ваші оголошення</h2>
      <div className="ads-container">
        {/* Замените пути на реальные изображения объявлений */}
        <div className="ad-card">
          <img src="path/to/your/ad-image-1.jpg" alt="Ad Image" className="ad-image" />
          <div className="ad-price">170,000$</div>
        </div>
        <div className="ad-card">
          <img src="path/to/your/ad-image-2.jpg" alt="Ad Image" className="ad-image" />
          <div className="ad-price">100,000$</div>
        </div>
        <div className="ad-card">
          <img src="path/to/your/ad-image-3.jpg" alt="Ad Image" className="ad-image" />
          <div className="ad-price">200,000$</div>
        </div>
      </div>
    </div>
  );
}

export default AdsSection;


// MobileMenu.js

import React from 'react';

function MobileMenu() {
  return (
    <div className="mobile-menu">
      <span>Menu</span>
    </div>
  );
}

export default MobileMenu;


// Установка React

// npx create-react-app dreamkeys-personal-cabinet
// cd dreamkeys-personal-cabinet
